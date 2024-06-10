# NewGRF 编写教程

[返回主菜单](../../../readme.md)

## 目录

- [程序](./code_introduction.md)
  - [基本运算](./code_functions.md)
  - [引导块](./code_header.md)
  - [文本](./code_strings.md)
- [图像](./sprites_introduction.md)
  - [软件](./sprites_software.md)

- [Actions](./actions_introduction.md)

## 介绍

编写 NewGRF 有固定的流程。

NewGRF，即 New graphics resource files，是用于 Transport Tycoon、Transport Tycoon Deluxe、OpenTTD 等游戏的图像文件；当中可以包含自定义代码，因此也可以用来拓展游戏内容。所有的 GRF 都不能跳脱出游戏所划定的沙盒，因此相较于其他游戏的模组 GRF 的自由度较少；你可以将 NewGRF 理解为游戏模组。

OpenTTD NewGRF 的一个最大特点就是兼容性好。哪怕是使用过时技术、过时标准编写的 GRF，一般而言，只要文件没有损坏，OpenTTD 都可以正确读取 GRF 内容并加载其内容。
