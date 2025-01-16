# 物品块（Item）

Item 块是 NewGRF 中一切新增内容之根源，从载具——火车、汽车——到建筑物——车站、物件，一切新增内容都需要先在 Item 块中定义后才可以使用。\
一般而言，一个 Item 块中会包含两项内容：properties，即“属性”，和 callbacks，即“回调函数”。你可以粗略地将前者理解为“游戏中不能随时变化”的数据，将后者理解为“可以编写代码使这项在游玩的时候改变”的数据。

## 载具的 Item 块

我们以载具为例，详细介绍 Item 块。

一个 Item 块的结构如下：

```cpp
item(FEAT_TRAINS, <名称>, <ID>) {
    property {
        a: 100;
        b: 200;
        ...
    }
    graphics {
        a: 100;
        b: 200;
    }
}
```

由于 Properties 不是可变的，而 Graphics 是可变的，因此在指定 Property 的值时，所指定的数值（或者表达式）必须在编译时就得到确定结果。也就是说不可以使用 Switch 块。而 Graphics 的数值是可变的，因此使用 Switch 块也没关系。

```bash
item(FEAT_TRAINS)
```
