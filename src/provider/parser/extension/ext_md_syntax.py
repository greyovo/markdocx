from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree

from markdown.inlinepatterns import SimpleTagInlineProcessor
from markdown.extensions import Extension


class ExtMdSyntax(Extension):
    def extendMarkdown(self, md):
        # ==高亮文本==
        md.inlinePatterns.register(SimpleTagInlineProcessor(r'()==(.+?)==', 'highlight'), 'highlight', 175)
        # ~下标~
        md.inlinePatterns.register(SimpleTagInlineProcessor(r'()~(.+?)~', 'sub'), 'sub', 1)
        # 删除线
        md.inlinePatterns.register(SimpleTagInlineProcessor(r'()~~(.+?)~~', 'strike'), 'strike', 2)
        # ^上标^
        md.inlinePatterns.register(SimpleTagInlineProcessor(r'()\^(.+?)\^', 'sup'), 'sup', 188)
