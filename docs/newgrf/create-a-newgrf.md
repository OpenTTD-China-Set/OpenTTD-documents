# NewGRF 编写教程

编写 NewGRF 有固定的流程。

NewGRF，即 New graphics resource files，是用于 Transport Tycoon、Transport Tycoon Deluxe、OpenTTD 等游戏的图像文件；当中可以包含自定义代码，因此也可以用来拓展游戏内容。所有的 GRF 都不能跳脱出游戏所划定的沙盒，因此相较于其他游戏的模组 GRF 的自由度较少；你可以将 NewGRF 理解为游戏模组。

OpenTTD NewGRF 的一个最大特点就是兼容性好。哪怕是使用过时技术、过时标准编写的 GRF，一般而言，只要文件没有损坏，OpenTTD 都可以正确读取 GRF 内容并加载其内容。

## 程序

如果想要编写程序，最好自己有一些编程基础。\
编写 NewGRF 最好准备一台电脑。

我们推荐使用 NML 来编写 NewGRF。当然，你也可以使用 grf-py 和 yagl。强烈不建议使用 NFO 编写 GRF。\
如果你不知道如何使用终端，我建议你先阅读下面的[认识终端](#编译认识终端)章节。

### 下载与安装 NML

可以使用多种方式来安装 nmlc。推荐使用 pip 或者 scoop 安装 nml。

- pip

```bash
pip3 install nml
```

- scoop（仅 Windows，支持自动更新）

```powershell
scoop bucket add openttd-bucket https://github.com/wensimehrp/openttd-bucket
scoop install openttd-bucket/nml
```

- 手动安装（以 Windows 为例）
  - 在 GitHub 或 `openttd.org` 下载 NML；
  - 下载完成后将 nml 放置到你指定的文件夹（如 `C:\tools\nml`）；
  - 打开控制面板或按 Win+Q 搜索 env，选择“编辑系统的环境变量”或“编辑账户的环境变量”并编辑 PATH 环境变量；注意不要删除任何环境变量！
  - 将放置的路径添加到 PATH。

如果选择手动安装，你也可以选择不将`nmlc`的路径加入 PATH 中并在编译时手动指定编译器路径。

安装完以后可以在终端内执行以下命令来查看 nml 版本

```powershell
nmlc --version
```

如果汇报了正确版本，恭喜你，你已经成功安装了 nml，跨过了第一道门槛。

由于 NML 目前尚在开发中，尚有一些程序错误，我们建议定期更新 NML 以避免 GRF 出错。

### 基本原理

不严谨地说，GRF 可以分为程序和图像两部分。图像是显示的内容，程序控制显示的内容。

在读取的时候，游戏先读取 GRF 识别符——你可以看作是 GRF 的“身份证”——以及 GRF 设置，读取其中的 GRF 编号、图像信息、可用参数（设置）等，然后开始读取剩余的部分。

GRF 中的所有内容实际上都是“图像”，只不过这些图像包括“pseudo-sprites”（伪图像）与“realsprites”（真图像）。“伪图像”即为代码，“真图像”即为“真正看到的图像”与重着色图像这个特例。为了讲解简便，后文统一以“代码”指代“伪图像”，“图像”指代“真图像”。整个 GRF 就是由图像构成的。

加载完成后，你就可以玩到 GRF 中的各种载具与建筑了。

### 制作身份证

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

### 编译——认识终端

编译 GRF 必须使用终端。

在 Windows 下，你可以通过 Windows+R 组合键打开“运行”界面，然后输入`cmd`或`powershell`打开终端。在我们的场景下，使用`cmd`和`powershell`基本没有区别；推荐使用 PowerShell。

进入终端后，使用`cd`命令可以切换目录；使用`dir`或者`ls`（仅 PowerShell）可以列出当前目录下的所有文件。在使用命令的时候可以使用`q`键左边的`tab`键补全命令，加快打命令的速度。

如果不知道某个命令如何使用，可以在打完之后加`--help`参数；或者，如果使用 PowerShell，可以使用`man`命令来查询使用手册，如：

```powershell
nmlc --help
man nmlc
```

优先使用`<命令> --help`，在报错之后再尝试`man <命令>`。

假设你把你的工程文件放在`C:\OpenTTD\GRF\`目录下，主文件是`my_grf.nml`，你可以通过这些步骤编译 GRF：

```powershell
cd C:\OpenTTD\GRF
# 可选项，使用ls命令来查询当前目录的所有文件
ls
# 编译 GRF
nmlc my_grf.nml
```

| 命令   | 作用                         | 备注                        |
|--------|----------------------------|----------------------------|
| `cd`   | 改变工作目录                 | 即“Change directory”        |
| `ls`   | 列出当前工作目录下的所有文件 | 即“List”，仅 PowerShell 可用 |
| `dir`  | 列出当前工作目录下的所有文件 | 即“Directory”               |
| `man`  | 获取帮助                     | 即“Manual”                  |
| `nmlc` | 编译 NML 语言                | 需要事前安装                |

### 基本运算

nml 支持以下运算符：

```powershell
算术运算符：+, -, *, /, %
比特运算符：&, |, ^, &&, ||, <<, >>
比较运算符：==, !=, <=, >=, <, >
三元运算符：? :
```

此外，还有一些函数：

```powershell
三角函数：sin(),cos(),tan(),asin(),acos(),atan()
平方根：sqrt()
绝对值：abs()
四舍五入：round()
取整：int()
```

## 图像

图像是玩家直接看到的部分，是 GRF 的核心，因此保证图像绘制美观正确是制作 GRF 的首要任务。

GRF 的图像有两个技术指标，分别是 bpp（每像素比特数）与 EZ（高清）。

bpp 越高，可用的颜色就越丰富。8bpp 代表每像素 8 比特，即一共有 $2^{8} = 256$ 种可用颜色；32bpp 代表每像素 32 比特，即一共有 $2^{32} = 4,294,967,296$ 种可用颜色（RGBA 模式，包括透明度）。

EZ 则有 Normal（普通）、2 倍和 4 倍之分。2 倍是将一个像素缩小到原来的四分之一，即 1/(2×2)；4 倍是将一个像素缩小到原先的十六分之一，即 1/(4×4)。玩家对颜色通常不敏感，因此主要考虑的技术指标是 EZ 与否。为了与游戏美术风格拟合，我们推荐绘制 8bpp Normal EZ 的图像。

使用 8bpp 的时候还须注意调色盘问题。原 TTD（运输大亨豪华版）有 DOS 与 Windows 两个版本，两个平台所支持的色彩不同，在 Windows 平台下需要分配一定的调色盘空间给系统 API 使用，因此 Windows 调色盘相较于 DOS 调色盘所支持的颜色要少。OpenTTD 作为 TTD 的继承者自然是两种调色盘都支持。我们推荐在绘制 8bpp 图像的时候使用 DOS 调色盘，原因如前文所说，DOS 调色盘支持的颜色更多。

总结如下：

| 技术        | 难易度 | 效果         | 备注                     |
|-------------|--------|--------------|--------------------------|
| 颜色        |        |              |                          |
| 8bpp        | ★      | 类似原版画风 | 有可能会遇到色盘编译问题 |
| 32bpp       | ★★     | 更加灵活     | 需要编写额外代码         |
| 缩放        |        |              |                          |
| Normal Zoom | ★      | 类似原版画风 |                          |
| 2x          | ★★★★   | 两者之间     | 需要编写额外代码         |
| 4x          | ★★★★★  | 高清画风     | 需要编写额外代码         |

通常而言，使用 2x 或 4x 的话会同时使用 32bpp。

### 软件

如果要绘制原版画风的图像，可以选用一些像素画软件：

| 名称        | 推荐程度 | 价格 | 备注                |
|-------------|----------|------|---------------------|
| Aseprite    | ★★★      | ¥70  | 学习版众多          |
| LibreSprite | ★★       | 免费 | Aseprite 的开源版本 |
| Paint.Net   | ★        | 免费 | 操作较繁杂          |
| Photoshop   | 不推荐   | 收费 |                     |
| gimp        | 不推荐   | 免费 |                     |

如果要绘制高清图像，普通的像素画软件就不够用了：

| 名称                   | 推荐程度 | 价格 | 备注   |
|------------------------|----------|------|--------|
| Paint.Net              | ★★       | 免费 |        |
| Photoshop              | ★★★      | 收费 |        |
| gimp                   | ★★       | 免费 |        |
| gorender + magicavoxel | /        | 免费 | 三渲二 |
| 其他 3D 建模软件       | /        | /    | 三渲二 |

很大一部分高清图像都是渲染出来的，而不是手绘出来的。\
往后绘图部分的教程都以 Aseprite 为使用的程序。

```powershell
# 可以使用scoop来下载绘图程序！
scoop bucket add extras
# LibreSprite
scoop install extras/libresprite
# pdn
scoop install extras/paint.net
# gimp
scoop install extras/gimp
# gorender + magicavoxel
scoop bucket add openttd-bucket https://github.com/wensimehrp/openttd-bucket
scoop install extras/magicavoxel
scoop install openttd-bucket/gorender
```

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
