from src.test.test_md2html import MarkdownParser
from src.test.test_html2docx import DocxProcessing
import time
import argparse

if __name__ == '__main__':
    start_time = time.time()
    md_path = "example.md"  # 你的md源文件路径
    html_path = "example.html"  # 中途临时导出的HTML文件路径，可不修改
    docx_path = "example.docx"  # 最后生成的docx文件存放路径

    # md_path = "note_demo.md"  # 你的md源文件路径
    # html_path = "note_demo.html"  # 中途临时导出的HTML文件路径，可不修改
    # docx_path = "note_demo.docx"  # 最后生成的docx文件存放路径

    _ = MarkdownParser(md_path, html_path)
    _ = DocxProcessing(html_path, docx_path)

    done_time = time.time()
    print("All done. Time cost:", "%.4f" % (done_time - start_time), "sec")
    # ===============

