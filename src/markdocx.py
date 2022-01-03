import argparse
import os
import sys

import yaml
from yaml import FullLoader

sys.path.append('..')

from src.parser.md_parser import md2html
import time

from src.provider.docx_processor import DocxProcessor

config: dict = {
    "version": "0.1.0"
}


# 生成资源文件目录访问路径
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.argv.append("-h")

    parser = argparse.ArgumentParser(description="markdocx - %s" % config["version"])
    parser.add_argument('input', help="Markdown file path")
    parser.add_argument('-o', '--output', help="Optional. Path to save docx file")
    parser.add_argument('-s', '--style',
                        help="Optional. YAML file with style configuration")
    parser.add_argument('-a', action="store_true",
                        help="Optional. Automatically open docx file when finished converting")
    args = parser.parse_args()
    docx_path = args.output if args.output is not None else args.input + ".docx"

    start_time = time.time()  # 记录转换耗时
    md2html(args.input, args.input + ".html")
    # 在打包成单文件exe后，直接以文件打开default_style.yaml会因为路径问题无法载入
    # Pyinstaller 可以将资源文件一起bundle到exe中，
    # 当exe在运行时，会生成一个临时文件夹，程序可通过sys._MEIPASS访问临时文件夹中的资源
    # https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile/13790741#13790741
    if not args.style:
        args.style = resource_path(os.path.join("config", "default_style.yaml"))

    with open(args.style, "r", encoding="utf-8") as file:
        conf = yaml.load(file, FullLoader)

    DocxProcessor(style_conf=conf) \
        .html2docx(args.input + ".html", docx_path)
    done_time = time.time()

    print("[SUCCESS] Convert finished in:", "%.4f" % (done_time - start_time), "sec(s).")
    print("[SUCCESS] Docx saved to:", os.path.abspath(docx_path))

    if args.a:
        os.startfile(os.path.abspath(docx_path))
