import markdown

from src.parser.ext_md_syntax import ExtMdSyntax


def md2html(in_path: str, out_path: str):
    with open(in_path, "r", encoding="utf-8") as input_file:
        text = input_file.read()

    html = markdown.markdown(text, extensions=[ExtMdSyntax(), 'tables'])

    with open(out_path, 'w', encoding="UTF-8") as html_file:
        html_file.write("""<head><meta charset="utf-8"></head>\n<body>\n""")
        html_file.write(html)
        html_file.write("</body>")


if __name__ == '__main__':
    md2html("example.md", "example.html")
