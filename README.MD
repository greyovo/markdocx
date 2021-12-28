# markdocx

将你的 markdown 文件转换为 MS Word（.docx）/ Convert your Markdown files to MS Word (.docx).

正在开发中 / Under development

## 测试阶段使用方法 

1. 需要 Python 2.7+ 环境
2. 安装依赖 `pip install -r requirements.txt`
3. 打开 `src/test/test_main.py`，根据注释修改里面的路径
4. 运行上述 `test_main.py` 

## 已知问题

1. 行内的样式超过一个的句子会在解析时会被忽略，不会出现在最终word文件中。例如：
    ```markdown
    **又加粗又*斜体***
    <u>**又加粗又*斜体*又下划线**</u>
    ```
    请避免使用复合标记。
2. 待补充。

## 段落 TODO 
- [x] 普通段落
- [x] 大纲标题
- [x] 图片
- [ ] 有序列表、无序列表、TODO List
- [ ] 引用块
- [ ] 表格
- [ ] 超链接
- [ ] 分割线
- [ ] 脚注，可能实现不了
- [ ] LaTeX，可能实现不了

## 内联语法 TODO 

- [x] 加粗、斜体、下划线
- [x] 上标、下标
- [x] 高亮文本
- [ ] 行内 LaTeX，可能实现不了

