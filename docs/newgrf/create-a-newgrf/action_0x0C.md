# Action0x0C 注释

[返回目录](./catalogue.md)\
[返回介绍](./actions_introduction.md)

在 YAGL 中，注释是`ignore`块。该块当中的所有内容都会被 OpenTTD 忽略，但是仍然会存在于 GRF 中。

>[!IMPORTANT]
> `ignore`块中的内容会被写入到 GRF 中，而以`//`/`/*`/`#`开头的 CPP/C/Bash 风格注释则会被编译器忽略。

## 样例

```cpp

ignore
{
    "OpenTTD 不读取我，哈哈哈哈


    还可以多行注释
    一定不要忘记最后有分号！
    ";
}

```
