import docx

from docx.enum.style import WD_STYLE_TYPE


# 中文的字号转 pt 方法
def _zihao_to_pt(chn_name: str):
    chn_name = chn_name.strip()
    pt_mapping = {
        "初号": 42,
        "小初": 36,
        "一号": 26,
        "小一": 24,
        "二号": 22,
        "小二": 18,
        "三号": 16,
        "小三": 15,
        "四号": 14,
        "小四": 12,
        "五号": 10.5,
        "小五": 9,
        "六号": 7.5,
        "小六": 6.5,
        "七号": 5.5,
        "八号": 5,
    }
    if pt_mapping.get(chn_name):
        return pt_mapping[chn_name]
    else:
        print("[YAML ERROR]:", chn_name,
              "不是一种规范的字号称呼。(中文语境下，字号最大是'初号'，最小是'八号')。")


class SimpleStyle:
    style_name: str
    base_style_name: str
    style_type: WD_STYLE_TYPE = WD_STYLE_TYPE.PARAGRAPH

    font_default: str = "Times New Roman"
    font_east_asia: str = "宋体"
    font_size: float = 14
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
                 conf: dict,  # 具体的样式数据，从yaml反序列化而来
                 style_type: docx.enum.style = WD_STYLE_TYPE.PARAGRAPH  # 是段落还是列表或是其他类型
                 ):
        self.style_name = style_name
        self.base_style_name = base_style_name
        self.style_type = style_type

        try:
            self.font_default = conf["font"]["default"]
            self.font_east_asia = conf["font"]["east-asia"]
            if str(conf["font"]["size"]).isdigit():
                self.font_size = conf["font"]["size"]
            else:  # 如果是以中文形式给出的字号，进行转换
                self.font_size = _zihao_to_pt(conf["font"]["size"])
        except ValueError:
            print(("[YAML ERROR]:", style_name,
                   "Error occurred in setting font style and has been set to:"),
                  self.font_default, self.font_east_asia, str(self.font_size) + "pt")

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
        if conf.get("font").get("extra"):
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
