import markdown

from provider.parser.extension.ext_md_syntax import ExtMdSyntax


class MarkdownParser:
    def __init__(self, in_path: str, out_path: str):
        with open(in_path, "r", encoding="utf-8") as input_file:
            text = input_file.read()

        html = markdown.markdown(text, extensions=[ExtMdSyntax(), 'tables'])

        with open(out_path, 'w', encoding="UTF-8") as html_file:
            html_file.write("""<head><meta charset="utf-8"></head>\n<body>\n""")
            html_file.write(html)
            html_file.write("</body>")
            # print("temp HTML saved to:", out_path)


if __name__ == '__main__':
    _ = MarkdownParser("example.md", "example.html")
