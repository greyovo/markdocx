# import markdown2
#
# html = markdown2.markdown_path('example.md',
#                                extras=["footnotes", "strike", "numbering", "tables", "break-on-newline"])
#
# with open('example.html', 'w', encoding="UTF-8") as html_file:
#     html_file.write("""<head><meta charset="utf-8"></head>\n<body>\n""")
#     html_file.write(html)
#     html_file.write("</body>")
#     print("saved to example.html done.")

import markdown

from provider.parser.extension.ext_md_syntax import ExtMdSyntax

with open("example.md", "r", encoding="utf-8") as input_file:
    text = input_file.read()

html = markdown.markdown(text, extensions=[ExtMdSyntax(), 'tables'])

with open('example.html', 'w', encoding="UTF-8") as html_file:
    html_file.write("""<head><meta charset="utf-8"></head>\n<body>\n""")
    html_file.write(html)
    html_file.write("</body>")
    print("saved to example.html done.")
