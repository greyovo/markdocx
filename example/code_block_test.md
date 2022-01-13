> “const型数据小结” 见书本P274，9.6.6

如果`const`关键字不涉及到指针，我们很好理解，下面是涉及到指针的情况：

```cpp
int b =  500;
// * 在const右，所指向的内容不能动
const int * a = &b;              // [1] 指针指向的b为常量，不能通过*a修改b的值
int const * a = &b;              // [2] 与[1]一样
// * 在const左，指针不能动
int * const a = &b;              // [3] 指针本身是常量，不能a++
// const 前后都有 *
const int * const a = &b;        // [4] 指针本身和指向的内容均为常量
```


如果一个成员函数的不会修改数据成员，那么最好将其声明为`const`，因为`const`成员函数中不允许对数据成员进行修改，如果修改，编译器将报错，这大 大提高了程序的健壮性。

若某对象由const修饰，如

```cpp
class A {
public:
    int val;
    int getValue() const;
    void setValue();
}

const A a;
a.getValue(); // 可以
a.setValue(); // 不行，不能调用非const修饰的成员函数（静态成员函数除外）
```

1. ALLO
2. sadasd

A paokkksl;

6. Apples
7. Oranges
8. Pears

A paokkksl;

1. Apples
2. Oranges
3. Pears