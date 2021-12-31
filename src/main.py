import argparse
import os
import sys

from src.parser.md_parser import md2html
import time

from src.provider.docx_processor import DocxProcessor
from utils.yaml_utils import read_style_yaml

config: dict = {
    "version": "0.1.0"
}

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.argv.append("-h")

    parser = argparse.ArgumentParser(description="markdocx - %s" % config["version"])
    parser.add_argument('input', help="Markdown file path")
    parser.add_argument('-o', '--output', help="Optional. Path to save docx file")
    parser.add_argument('-s', '--style', default="./config/default_style.yaml",
                        help="Optional. YAML file with style configuration")
    parser.add_argument('-a', action="store_true",
                        help="Optional. Automatically open docx file when finished converting")
    # todo 通过yaml自定义样式文件

    args = parser.parse_args()

    start_time = time.time()  # 记录转换耗时

    md2html(args.input, args.input + ".html")
    docx_path = args.output if args.output is not None else args.input + ".docx"

    DocxProcessor(style_conf=read_style_yaml(args.style)) \
        .html2docx(args.input + ".html", docx_path)
    done_time = time.time()

    print("Convert finished in:", "%.4f" % (done_time - start_time), "sec(s).")
    i = os.path.abspath(docx_path).rfind("\\")
    print("Docx saved to:", os.path.abspath(docx_path), ".")

    if args.a:
        os.startfile(os.path.abspath(docx_path))
