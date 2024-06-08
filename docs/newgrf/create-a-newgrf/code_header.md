# 制作身份证

[返回目录](./catalogue.md)\
[返回介绍](./code_introduction.md)

如前文所说，OpenTTD 在读取 GRF 的时候会读取 GRF 识别符，即 ID。ID 与其他项目必须放在 NewGRF 代码的最前面。grf 块包含了这些项目。

```cpp
grf {
    grfid: "\00\00\00\00";
    name: string(STR_GRF_NAME);
    desc: string(STR_GRF_DESC);
    version: 0;
    min_compatible_version: 0;
}
```
