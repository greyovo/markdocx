from src.test.test_md2html import MarkdownParser
from src.test.test_html2docx import DocxProcessing

if __name__ == '__main__':
    md_path = "example.md"  # 你的md源文件路径
    html_path = "temp.html"  # 中途临时导出的HTML文件路径，可不修改
    docx_path = "example.docx"  # 最后生成的docx文件存放路径
    
    _ = MarkdownParser(md_path, html_path)
    _ = DocxProcessing(html_path, docx_path)
    print("All done.")
