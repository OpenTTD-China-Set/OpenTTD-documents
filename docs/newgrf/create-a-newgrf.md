#### 8bpp 调色盘

如前文所说，DOS 调色盘包含的颜色相较于 Windows 调色盘更多。每张调色盘都有一定的 Reserved Range，即“保留范围”。在保留范围中的颜色有一定的作用，如动画和公司颜色等。

<!--在这里插入图片-->

### 阴影、比例和大小

游戏中的光照都是自右上至左下的；处理好阴影关系非常重要。

OpenTTD 游戏本身在比例方面并不严谨，所以比例需要自己调控。

### 图像细节——噪点

街边的砖墙、公园的瓷砖，我们能看到的东西都有材质。使用噪点便是模拟这些材质的一种方法。

### 绘制图像——以火车为例

### 图像在程序上的实现—— Spriteset 与 Templates

### 修复常见问题

#### NMLC 提示调色盘有问题

这种情况通常是因为在 spriteset 中设置的图像色彩深度和 NMLC 实际读取到的图像不一致；比如：spriteset 中设置颜色深度为 8bpp，但是实际图像为 32bpp，或者 spriteset 中设置的是 32bpp，但是实际图像为 8bpp（即索引模式）。\
这种问题通常有三种原因：

1. 想要使用 32bpp 图像，但是误使用 8bpp 图像；
2. 想要使用 8bpp 图像，但是误将图像转换为 32bpp；
3. 图像使用的色盘不是 DOS 或 Windows 色盘。

解决方法是通用的，都是转换图像的色盘。

最简单的方法是使用 Aseprite 或者 LibreSprite 转换色盘；使用 Photoshop 或 Gimp 也可以，但速度可能较慢。使用 Paint.Net 则完全不可行（按照作者个人经验前述第三种原因大多都是使用 PDN 导致的）。本教程中只演示使用 LibreSprite/Aseprite 的做法。
<!--这里要补充-->

#### 图像有偏移

图像偏移是非常常见的情况，解决起来也很简单。只需要在游戏中激活 NewGRF 开发者工具，使用开发工具提供的 Sprite 对齐器对齐后将偏移值导入至代码中即可。

#### 图像不完整/有白边

图像不完整或有白边是因为使用的 spriteset 中划定的图像范围没有完整覆盖实际图像。

#### NMLC 提示有 ANIM/WHIT 像素
