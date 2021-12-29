import docx
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import *
from docx.oxml.ns import qn
from docx.shared import Inches, RGBColor, Pt
from docx.styles import style
from docx.styles.style import _ParagraphStyle, BaseStyle


class StyleManager:

    def __init__(self, doc: Document, style_conf: dict):
        self.styles = doc.styles
        self.style_conf = style_conf

    def init_styles(self):
        # 正文
        normal = self.styles['Normal']
        normal.font.name = "Times New Roman"  # 只设置name是设置西文字体
        normal._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')  # 要额外设置中文字体
        normal.paragraph_format.space_after = Pt(5)
        normal.paragraph_format.space_before = Pt(5)
        normal.paragraph_format.line_spacing = 1.15

        # 各级标题
        # 直接对heading的样式设置是不生效的，需要新建一个同名样式覆盖
        self.init_heading()

        # 引用块
        blockquote: style = self.styles.add_style("Block Quote", WD_STYLE_TYPE.PARAGRAPH)
        # blockquote.base_style = styles["Normal"]
        blockquote.font.name = "Times New Roman"  # 只设置name是设置西文字体
        blockquote._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')  # 要额外设置中文字体
        # blockquote.font.color.rgb = RGBColor(255, 0, 0)
        blockquote.font.italic = True

        # 图片描述
        caption: style = self.styles["Caption"]
        caption.font.name = "Times New Roman"  # 只设置name是设置西文字体
        caption._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')  # 要额外设置中文字体
        caption.font.color.rgb = RGBColor(0, 0, 0)
        caption.font.bold = False

    def init_heading(self):
        for i in range(1, 5):
            conf = self.style_conf["h%d" % i]
            new_style: _ParagraphStyle = self.styles.add_style('Heading%d' % i, WD_STYLE_TYPE.PARAGRAPH)
            new_style.base_style = self.styles['Heading %d' % i]
            new_style.quick_style = True
            new_style.font.name = conf["font"]["default"]  # 只设置name是设置西文字体
            new_style._element.rPr.rFonts.set(qn('w:eastAsia'), conf["font"]["eastern"])  # 要额外设置中文字体
            new_style.font.color.rgb = RGBColor(0, 0, 0)
            # 去除段落前面左上角的黑点
            new_style.paragraph_format.keep_together = False
            new_style.paragraph_format.keep_with_next = False

    # 通用的样式设置
    def init_style(self, name: str, detail: dict, style_type: docx.enum.style, quick_style: bool):
        pass
