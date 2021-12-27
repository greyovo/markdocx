from bs4 import BeautifulSoup


def parse_list(item) -> []:
    print(item)




if __name__ == '__main__':
    with open('example.html', 'r', encoding="UTF-8") as html_file:
        html_str = html_file.read()
    soup = BeautifulSoup(html_str, 'html.parser')
    body_tag = soup.contents[2]
    tag_content_list: list = []
    for child in body_tag.children:
        if not child.string == "\n":
            print(child.name)

            # 判断是普通段落还是标题
            if child.name == "p":
                # todo
                pass
            if child.name == "h1" or child.name == "h2" or child.name == "h3" or child.name == "h4" or child.name == "h5":
                # todo
                pass

            for elem in child.contents:  # 遍历一个段落内的所有文字
                if elem.name is not None:  # 有字符样式的子串
                    print(elem.name, elem.string)
                elif not elem.string == "\n":  # 无字符样式的子串
                    print("plain", elem)


