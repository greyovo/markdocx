# markdocx

将你的 markdown 文件转换为 MS Word（.docx）/ Convert your Markdown files to MS Word (.docx).

正在开发中 / Under development

## 测试阶段使用方法 

1. 需要 Python 3.0+ 环境
2. 安装依赖 `pip install -r requirements.txt`
3. 进入 `src/test`，终端执行命令：

```shell script
test_main.py input.md -o ouput.docx
```
其中 `-o` 参数是可选的，没有则保存到与 `input.md` 同目录位置、同名的 docx 文件。

如果是绝对路径，需要用英文(半角)双引号包起来，如

```shell script
test_main.py "D:/folder/input.md" -o "D:/folder/input.md"
```

## 已知问题

1. 行内的样式超过一个的句子会在解析时会被忽略，**不会**出现在最终word文件中。例如：
    ```markdown
    **又加粗又*斜体***
    <u>**又加粗又*斜体*又下划线**</u>
    ```
    请避免使用复合标记。
2. 代码块中如果有 `#` 或 `*` 等 markdown 行内标记的符号，有可能会被误识别为markdown文本而错误渲染，待解决。

## 段落样式 TODO

- [x] 普通段落
- [x] 大纲标题
- [x] 图片
- [x] 有序列表、无序列表、TODO List
- [x] 引用块
- [x] 表格
- [x] 超链接
- [x] 分割线，在docx中表现为分页符

## 行内样式 TODO 

- [x] 加粗、斜体、下划线
- [x] 上标、下标
- [x] 高亮文本

## 暂时无法实现
- LaTeX
- 脚注

