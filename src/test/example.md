# 你好，Markdown

如您所见，# 号开头即为标题，从一级到六级。

## 文字格式

`Markdown` 是当下流行文档书写语言，旨在通过简单的语法实现对常见格式的支持。

标准 Markdown 支持 **粗体** 和 *斜体* 文本，部分实现支持 ~~删除线~~。下划线则需通过内嵌 HTML 实现，<u>像是这样</u>。

还有上标 X^2^ 和下标 Y~3~，将文字==高亮==起来，属于扩展格式，手动支持了。

## 段落格式

### 代码块

```cpp
int main() {
    cout << "hello world" << endl;
    return 0;
}
```

### LaTex 演示

$$
y=\sin(x)
$$

### 列表项

使用数字和减号来实现有序和无序列表：

1. 第一项
    1. sub1
    2. sublist2
2. 第二项

无序列表二级

- 第一项
    - sub1
    - sublist2
- 第二项

此外，还有清单列表：

- [ ] 未选择
- [x] 已选择

### 引用块

> 请随意编辑这个文件，您总是可以在[这里](https://docs.taio.app/#/cn/editor/hello-markdown)找到在线版本。
> 
> 这是引用块的第二段

## 分割线

分割线前的内容

---

后面的内容

## 链接和图片

使用中括号包裹标题，小括号包裹内容：[Taio 官网](https://taio.app/cn/)

![本地图片1](assets/small_img.png)

![](assets/windows11.png)


![网络图片]("https://p1.itc.cn/q_70/images01/20210608/2de4b5a9f4db46ee83b1081dc557929e.jpeg")

## 表格

| Name  | Age  | Sex    |
| ----- | ---- | ------ |
| Jack  | 22   | male   |
| Grace | 33   | female |
| Tom   |      |        |
