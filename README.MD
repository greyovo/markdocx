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

如果是路径包含文件夹，需要用英文(半角)双引号包起来，如

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

## 样式 TODO

- [x] 普通段落
- [x] 大纲标题
- [x] 图片
- [x] 有序列表、无序列表、TODO List
- [x] 引用块
- [x] 表格
- [x] 超链接
- [x] 分割线，在docx中表现为分页符
- [x] 加粗、斜体、下划线
- [x] 行内代码
- [x] 上标、下标
- [x] 高亮文本


## 未来计划

- [x] 使用 yaml 导入样式参数，方便自定义样式
- [ ] 提供 GUI
 
## 暂时无法实现
- LaTeX
- 脚注


## YAML 格式

```yaml
font:
  default: 西文字体，默认 [Times New Roman]
  east-asia: 中文字体，默认 [宋体]
  size: 字体大小，默认 [12]，单位：pt
  color: RGB颜色 16 进制值，必须是字符串，默认 ["000000"] 纯黑色
  extra: 额外的样式，默认不添加这些样式。支持下列样式，有则生效，无则忽略
  - bold 加粗
  - italic 斜体
  - underline 下划线
  - strike 删除线
first-line-indent: 首行缩进，默认 [0]，单位：倍
line-spacing: 行距，默认 [1.2] 单位：倍，表示行距设置为 1.2 倍行高，
space:
  before: 段前空格，默认 [0] pt
  after: 段后空格，默认 [0] pt
```

