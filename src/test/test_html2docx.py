# noinspection PyProtectedMember
#

from bs4 import BeautifulSoup

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.styles.style import _ParagraphStyle
from docx.text.paragraph import Paragraph
from docx.enum.text import *
from docx.oxml.ns import qn

from docx.shared import Inches, RGBColor

enable_debug: bool = False

document = Document()

def debug(*args):
    print(*args) if enable_debug else None


def init_styles():
    styles = document.styles

    # 正文
    normal = styles['Normal']
    normal.font.name = "Calibri"  # 只设置name是设置西文字体
    normal._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')  # 要额外设置中文字体

    # 各级标题
    # 直接对heading的样式设置是不生效的，需要新建一个同名样式覆盖
    for i in range(1, 5):
        new_style: _ParagraphStyle = styles.add_style('Heading%d' % i, WD_STYLE_TYPE.PARAGRAPH)
        new_style.base_style = styles['Heading %d' % i]
        new_style.quick_style = True
        new_style.font.name = "Times New Roman"  # 只设置name是设置西文字体
        new_style._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')  # 要额外设置中文字体
        new_style.font.color.rgb = RGBColor(0, 0, 0)


# h1, h2, ...
def add_heading(content: str, tag: str):
    level: int = int(tag.__getitem__(1))
    p = document.add_paragraph(content, style="Heading%d" % level)
    return p


# bold, italic, strike...
def add_run(p: Paragraph, content: str, char_style: str = "plain"):
    debug("[%s]:" % char_style, content)
    run = p.add_run(content)
    run.bold = (char_style == "strong")
    run.italic = (char_style == "em")
    run.underline = (char_style == "u")
    run.font.strike = (char_style == "strike")
    run.font.subscript = (char_style == "sub")
    run.font.superscript = (char_style == "sup")
    run.font.highlight_color = WD_COLOR_INDEX.YELLOW if char_style == "highlight" else None

    if char_style == "code":
        run.font.name = "Consolas"

    # TODO 引用块
    # TODO 有序列表、无序列表、TODO列表


# TODO 图片
def add_picture(p: Paragraph, pic_src: str):
    debug("[pic] [src]:", pic_src)

    pass


# TODO 表格
def add_table(p: Paragraph, pic_src: str):
    pass


# TODO 分割线
def add_split_line(p: Paragraph):
    pass


# TODO 超链接
def add_link(p: Paragraph, content: str, src: str):
    debug("[text]:", content, "[src]:", src)
    run = p.add_run(content)


class DocxProcessing:
    def __init__(self, html_path: str, docx_path: str):
        # 打开HTML
        with open(html_path, 'r', encoding="UTF-8") as html_file:
            html_str = html_file.read()
        soup = BeautifulSoup(html_str, 'html.parser')
        body_tag = soup.contents[2]
        tag_content_list: list = []
        para: Paragraph
        # 初始化样式
        init_styles()
        # 逐个写到word中
        for child in body_tag.children:
            if not child.string == "\n":
                debug(child.name)

                # 判断是普通段落还是标题
                if child.name == "p":
                    para = document.add_paragraph(style="Normal")

                    for elem in child.contents:  # 遍历一个段落内的所有文字
                        if elem.name == "a":
                            add_link(para, elem.string, elem["href"])
                        elif elem.name == "img":
                            add_picture(para, elem["src"])
                        elif elem.name is not None:  # 有字符样式的子串
                            add_run(para, elem.string, elem.name)
                        elif not elem.string == "\n":  # 无字符样式的子串
                            add_run(para, elem)

                if child.name == "h1" or child.name == "h2" or \
                        child.name == "h3" or child.name == "h4" or child.name == "h5":
                    para = add_heading(child.string, child.name)

        document.save(docx_path)
        print("docx saved to:", docx_path)


if __name__ == '__main__':
    _ = DocxProcessing("example.html", "example.docx")
