# Item 块

[返回目录](./catalogue.md)\
[返回介绍](./code_introduction.md)

Item 块是 NewGRF 中一切新增内容之根源，从载具——火车、汽车——到建筑物——车站、物件，一切新增内容都需要先在 Item 块中定义后才可以使用。\
一般而言，一个 Item 块中会包含两项内容：properties，即“属性”，和 callbacks，即“回调函数”。你可以粗略地将前者理解为“游戏中不能随时变化”的数据，将后者理解为“可以写代码在游玩的时候改变”的数据。

```bash
item(FEAT_TRAINS)
```
