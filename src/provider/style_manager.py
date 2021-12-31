import docx
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import *
from docx.oxml.ns import qn
from docx.shared import Inches, RGBColor, Pt
from docx.styles import style
from docx.styles.style import _ParagraphStyle, BaseStyle


class StyleManager:

    def __init__(self, doc: Document, yaml_conf: dict):
        self.styles = doc.styles
        self.style_conf = yaml_conf

    def init_styles(self):
        # 设置heading
        for i in range(1, 5):
            self.set_style("Heading%d" % i, "Heading %d" % i,
                           self.style_conf["h%d" % i],
                           WD_STYLE_TYPE.PARAGRAPH,
                           )
        # 设置正文
        self.set_style("Normal", "Normal",
                       self.style_conf["normal"], WD_STYLE_TYPE.PARAGRAPH)

    # 通用的样式设置
    def set_style(self, style_name: str,
                  base_style_name: str,
                  style_conf: dict,
                  style_type: docx.enum.style,
                  quick_style: bool = True):
        new_style: _ParagraphStyle = self.styles.add_style(style_name, style_type)
        new_style.base_style = self.styles[base_style_name]
        new_style.quick_style = True

        # ##### 字体相关 #####
        font_conf = style_conf["font"]
        # 设置字体、颜色、大小
        new_style.font.name = font_conf["default"]  # 只设置name是设置西文字体
        new_style.font.size = Pt(font_conf["size"])
        new_style._element.rPr.rFonts.set(qn('w:eastAsia'), font_conf["east-asia"])  # 要额外设置中文字体
        new_style.font.color.rgb = RGBColor(0, 0, 0).from_string(font_conf["color"])
        # 加粗、斜体、下划线、删除线
        new_style.font.bold = "bold" in list(font_conf["extra"])
        new_style.font.italic = "italic" in list(font_conf["extra"])
        new_style.font.underline = "underline" in list(font_conf["extra"])
        new_style.font.strike = "strike" in list(font_conf["extra"])

        # ##### 段落相关 #####
        # 设置缩进、段前/段后空格、段内行距
        new_style.paragraph_format.first_line_indent(
            Pt(int(font_conf["size"]) * int(style_conf["first-line-indent"]))
        )
        new_style.paragraph_format.space_before = Pt(style_conf["space"]["before"])
        new_style.paragraph_format.space_after = Pt(style_conf["space"]["after"])
        new_style.paragraph_format.line_spacing = style_conf["line-spacing"]

        # 去除段落前面左上角的黑点
        new_style.paragraph_format.keep_together = False
        new_style.paragraph_format.keep_with_next = False

        # 其他
        new_style.quick_style = quick_style  # 显示在快捷样式窗口上
        return
