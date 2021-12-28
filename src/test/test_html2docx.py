# noinspection PyProtectedMember
#
import io
import os
from urllib.request import urlopen

from bs4 import BeautifulSoup
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import *
from docx.oxml.ns import qn
from docx.shared import Inches, RGBColor
from docx.styles.style import _ParagraphStyle
from docx.text.paragraph import Paragraph
from docx.text.run import Run

enable_debug: bool = True
enable_image_desc: bool = True  # 是否显示图片的描述，即 `![desc](src/img)` 中 desc的内容

document: Document = Document()


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

    # TODO 代码块样式
    if char_style == "code":
        run.font.name = "Consolas"

    # TODO 引用块
    # TODO 有序列表、无序列表、TODO列表


def add_picture(elem):
    p: Paragraph = document.add_paragraph()
    p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    run: Run = p.add_run()

    img_src: str

    if elem["src"] != "":
        img_src = elem["src"]
        debug("[local image]:", img_src)
        run.add_picture(img_src, width=Inches(5.8))
    else:
        img_src = elem["title"]
        # if img_src.startswith("http"):
        debug("[remote image]:", img_src)
        image_bytes = urlopen(img_src).read()
        data_stream = io.BytesIO(image_bytes)
        run.add_picture(data_stream, width=Inches(5.8))

    # 如果选择展示图片描述，那么描述会在图片下方显示
    # TODO 图片描述的显示样式设置
    if enable_image_desc and elem["alt"] != "":
        desc_p: Paragraph = document.add_paragraph(elem["alt"], style="Caption")
        desc_p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER


# TODO 表格
def add_table(p: Paragraph, pic_src: str):
    pass


# TODO 分割线
def add_split_line(p: Paragraph):
    pass


# TODO 超链接
def add_link(p: Paragraph, text: str, src: str):
    debug("[link]:", text, "[src]:", src)
    run = p.add_run(text)


def add_paragraph(children: [], parent_paragraph: Paragraph = None):
    """
    :type children: list
    一个段落内的元素（包括图片）。根据有无样式来划分，组成一个列表。
    有样式文字如加粗、斜体、图片、等。
    如`I am plain _while_ he is **bold**`将转为：
    ["I am plain", "while", "he is", "bold"]

    :param parent_paragraph
    父级段落，一般可能是引用块(blockquote)。此时的新段落的样式继承父段落的样式，设置为None
    """
    style = "Normal" if parent_paragraph is None else None
    p: Paragraph = document.add_paragraph(style=style)
    for elem in children.contents:  # 遍历一个段落内的所有元素
        if elem.name == "a":
            add_link(p, elem.string, elem["href"])
        elif elem.name == "img":
            add_picture(elem)
        elif elem.name is not None:  # 有字符样式的子串
            add_run(p, elem.string, elem.name)
        elif not elem.string == "\n":  # 无字符样式的子串
            add_run(p, elem)


# from docx.enum.style import WD_STYLE
def add_blockquote(children: []):
    block: Paragraph = document.add_paragraph(style="Comment Text")
    add_paragraph(children, block)


class DocxProcessing:
    def __init__(self, html_path: str, docx_path: str):
        # 打开HTML
        with open(html_path, 'r', encoding="UTF-8") as html_file:
            html_str = html_file.read()
        soup = BeautifulSoup(html_str, 'html.parser')
        body_tag = soup.contents[2]
        para: Paragraph
        # 初始化样式
        init_styles()
        # 逐个写到word中
        for sub_item in body_tag.children:
            if not sub_item.string == "\n":
                debug(sub_item.name)

                # 判断是普通段落还是标题
                if sub_item.name == "p" or sub_item.name == "blockquote":
                    add_paragraph(sub_item)
                if sub_item.name == "blockquote":
                    add_blockquote(sub_item)

                if sub_item.name == "h1" or sub_item.name == "h2" or \
                        sub_item.name == "h3" or sub_item.name == "h4" or sub_item.name == "h5":
                    para = add_heading(sub_item.string, sub_item.name)

        document.save(docx_path)
        print("docx saved to:", docx_path)


if __name__ == '__main__':
    _ = DocxProcessing("example.html", "example.docx")

    os.startfile("example.docx")
