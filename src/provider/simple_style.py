import docx

from docx.enum.style import WD_STYLE_TYPE


class _Simple_Style:
    style_name: str
    base_style_name: str
    style_type: WD_STYLE_TYPE = WD_STYLE_TYPE.PARAGRAPH

    font_default: str = "Times New Roman"
    font_east_asia: str = "宋体"
    font_size: str = 14
    font_color: str = "000000"

    bold: bool = False
    italic: bool = False
    underline: bool = False
    strike: bool = False

    first_line_indent: int = 0
    line_spacing: int = 0
    space_before: int = 0
    space_after: int = 0

    def __init__(self,
                 style_name: str,  # 样式名称
                 base_style_name: str,  # 基于的样式
                 style_type: docx.enum.style,  # 是段落还是列表或是其他类型
                 conf: dict):  # 具体的dict数据
        self.style_name = style_name
        self.base_style_name = base_style_name
        self.style_type = style_type

        try:
            self.font_default = conf["font"]["default"]
            self.font_size = conf["font"]["size"]
            self.font_east_asia = conf["font"]["east-asia"]
        except ValueError:
            print(("[YAML ERROR]:", style_name,
                   "Error occurred in setting font style and has been set to:"),
                  self.font_default, self.font_east_asia, self.font_size)

        # 颜色有指定时检查，不指定默认黑色
        if conf["font"].get("color") is not None:
            try:
                # 尝试进行转换为16进制数，并且是否符合RGB大小
                hex_num = int(str(conf["font"]["color"]), 16)
                if 0 <= hex_num <= 0xFFFFFF:
                    self.font_color = conf["font"]["color"]
                else:
                    raise ValueError
            except ValueError:
                print("[YAML ERROR]:", style_name,
                      "font-color value isn't a hex or not in range [0, FFFFFF] and "
                      "has been default to black(000000).")

        # 加粗、斜体、下划线、删除线
        self.font_bold = "bold" in list(conf["font"]["extra"])
        self.font_italic = "italic" in list(conf["font"]["extra"])
        self.font_underline = "underline" in list(conf["font"]["extra"])
        self.font_strike = "strike" in list(conf["font"]["extra"])

        if conf.get("first-line-indent"):
            self.first_line_indent = conf["first-line-indent"]
        if conf.get("line-spacing"):
            self.line_spacing = conf["line-spacing"]
        if conf.get("space"):
            if conf.get("space").get("before"):
                self.space_before = conf["space"]["before"]
            if conf.get("space").get("after"):
                self.space_after = conf["space"]["after"]
