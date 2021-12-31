import argparse
import sys

from test import MarkdownParser
from test import DocxProcessing
import time

config: dict = {
    "version": "0.1.0"
}

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('markdocx: type "-h" for help.')
        exit(0)

    parser = argparse.ArgumentParser(description="markdocx - %s" % config["version"])
    parser.add_argument('input', help="Markdown file path")
    parser.add_argument('-o', '--output', help="Optional. Path to save docx file")
    # parser.add_argument('-s', '--style', help="你的样式文件，yaml") todo 通过yaml自定义样式文件

    args = parser.parse_args()

    start_time = time.time()  # 记录转换耗时
    MarkdownParser(args.input, args.input + ".html")
    docx_path = args.output if args.output is not None else args.input + ".docx"
    DocxProcessing(args.input + ".html", docx_path)
    done_time = time.time()

    print("Convert finished in:", "%.4f" % (done_time - start_time), "sec(s)")
    print("Docx saved to:", docx_path)
