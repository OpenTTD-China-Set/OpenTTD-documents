# NewGRF 编写教程

编写 NewGRF 有固定的流程。

## 程序

我们推荐使用 NML 来编写 NewGRF。当然，你也可以使用 grf-py 和 yagl。强烈不建议使用 nfo 编写 GRF。

### NML 的下载与安装

可以使用多种方式来安装 nmlc。推荐使用 pip 或者 scoop 安装 nml。

- pip
```bash
pip3 install nml
```
- scoop（仅 Windows，支持自动更新）
```bash
scoop bucket add openttd-bucket https://github.com/wensimehrp/openttd-bucket
scoop install openttd-bucket/nml
```
- 手动安装（以 Windows 为例）
 - 在 GitHub 或 openttd.org 下载 nmlc；
 - 下载完成后将 nml 放置到你中意的文件夹（如 C:\tools\nml）；
 - 搜索 env，编辑 PATH；
 - 将放置的路径添加到 PATH。

安装完以后可以在终端内执行以下命令来查看 nml 版本
```
nml --version
```
如果汇报了正确版本，恭喜你，你已经成功安装了 nml，跨过了第一道门槛。

由于NML目前尚在开发中，尚有一些程序错误，我们建议定期更新NML以避免GRF出错。

### 基本原理

GRF 可以分为程序和图像两方面。图像是显示的内容，程序控制显示的内容。

在读取的时候，游戏先读取 GRF 识别符——你可以看作是 GRF 的“身份证”，读取其中的 GRF 编号、图像信息、可用参数（设置）等，然后开始读取剩余的部分。

### 基本运算

nml 支持以下运算符：

- 算术运算符：`+, -, *, /, %`
- 比特运算符：`&, |, ^, &&, ||, <<, >>`
- 比较运算符：`==, !=, <=, >=, <, >`
- 三元运算符：`? :`

此外，还有一些函数：

- 三角函数：`sin(),cos(),tan(),asin(),acos(),atan()`
- 平方根：`sqrt()`
- 绝对值：`abs()`
- 四舍五入：`round()`
- 取整：`int()`

## 图像

图像是玩家直接看到的部分，是 GRF 的核心，因此保证图像绘制美观正确是制作 GRF 的首要任务。

GRF 的图像有两个技术指标，分别是bpp（每像素比特数）与EZ（高清）。bpp越高，可用的颜色就越丰富。8bpp代表每像素8比特，即一共有2<sup>8</sup> = 256种可用颜色；32bpp代表每像素32比特，即一共有2<sup>32</sup> = 4,294,967,296种可用颜色（RGBA模式，包括透明度）。EZ则有Normal（普通）、2倍和4倍之分。2倍是将一个像素缩小到原来的四分之一，即1/(2×2)；4倍是将一个像素缩小到原先的十六分之一，即1/(4×4)。玩家对颜色通常不敏感，因此主要考虑的技术指标是EZ与否。为了与游戏美术风格拟合，我们推荐绘制8bpp Normal EZ的图像。

使用8bpp的时候还须注意调色盘问题。原TTD（运输大亨豪华版）有DOS与Windows两个版本，两个平台所支持的色彩不同，在Windows平台下需要分配一定的调色盘空间给系统API使用，因此Windows调色盘相较于DOS调色盘所支持的颜色要少。OpenTTD作为TTD的继承者自然是两种调色盘都支持。我们推荐在绘制8bpp图像的时候使用DOS调色盘，原因如前文所说，DOS调色盘支持的颜色更多。

### 软件

如果要绘制原版画风的图像，可以选用一些像素画软件：

- Aseprite（推荐，Steam有售，¥70，学习版众多）
- LibreSprite（推荐，Aseprite的GPL开源版本，免费）
- Paint.Net（推荐，免费，操作较繁杂）
- Photoshop（不推荐，收费）
- gimp（不推荐，开源）

如果要绘制高清图像，普通的像素画软件就不够用了：

- Paint.Net（推荐）
- Photoshop（推荐）
- gimp（不推荐，免费）
- gorender + magicavoxel（三渲二）
- 其他3D建模软件（三渲二）

很大一部分高清图像都是渲染出来的，而不是手绘出来的。\
往后绘图部分的教程都以Aseprite为使用的程序。

### 认识游戏比例与大小

### 绘制图像——以火车为例

