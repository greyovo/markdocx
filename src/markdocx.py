import argparse
import os
import sys

from importlib import resources

import yaml
from yaml import FullLoader

sys.path.append('..')

from src.parser.md_parser import md2html
import time

from src.provider.docx_processor import DocxProcessor
from src.utils.yaml_utils import read_style_yaml

config: dict = {
    "version": "0.1.0"
}

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.argv.append("-h")

    parser = argparse.ArgumentParser(description="markdocx - %s" % config["version"])
    parser.add_argument('input', help="Markdown file path")
    parser.add_argument('-o', '--output', help="Optional. Path to save docx file")
    parser.add_argument('-s', '--style', help="Optional. YAML file with style configuration")
    parser.add_argument('-a', action="store_true",
                        help="Optional. Automatically open docx file when finished converting")

    args = parser.parse_args()

    start_time = time.time()  # 记录转换耗时

    md2html(args.input, args.input + ".html")
    docx_path = args.output if args.output is not None else args.input + ".docx"

    conf = None

    # 加载样式资源
    # fixme：在打包成exe后，default_style.yaml会因为路径问题无法载入，需要更换资源导入方式。
    #  Pyinstaller 可以将资源文件一起bundle到exe中，
    #  当exe在运行时，会生成一个临时文件夹，程序可通过sys._MEIPASS访问临时文件夹中的资源
    #  https://www.cnblogs.com/darcymei/p/9397173.html
    if args.style:
        with open(args.style, "r", encoding="utf-8") as file:
            conf = yaml.load(file, FullLoader)
    else:
        with resources.open_text('src', 'default_style.yaml') as file:
            content = file.read()
            conf = yaml.load(file, FullLoader)

    DocxProcessor(style_conf=conf) \
        .html2docx(args.input + ".html", docx_path)
    done_time = time.time()

    print("Convert finished in:", "%.4f" % (done_time - start_time), "sec(s).")
    i = os.path.abspath(docx_path).rfind("\\")
    print("Docx saved to:", os.path.abspath(docx_path), ".")

    if args.a:
        os.startfile(os.path.abspath(docx_path))
