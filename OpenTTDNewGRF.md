# 智障也能看懂的找扩展包教程与推荐和介绍

*WenSim, Mikhail, Feb.21, 2024*\
*INDEV*

## 前言

OpenTTD 提供了许多扩展包。这其中有：

- Baseset
    - 基本图形集
    - 基本音乐集
    - 基本音效集
- NewGRF
    - 游戏中的主要扩展
- 游戏脚本（Game Script, GS）
- AI

其中大多数扩展包被托管在 BaNaNaS 上。BaNaNaS 是一个在线内容托管服务，由 OpenTTD 官方团队运营。请注意，**由于所有人都可以自由地在此服务器上上传内容，请务必要做好内容辨析。**

## 如何寻找扩展包？

请记住这个网址 - https://bananas.openttd.org。\
如前文所说，BaNaNaS托管了大部分的NewGRF，自然其也提供了便利的查找功能。

### 其他方法

tt-forums是早期NewGRF的集散地，也是OpenTTD开发论坛（之一）。你可以在Graphics-developments板块下找到NewGRF。

另外还有韩国玩家社区等，由于知名度过低，不表。

## 扩展包推荐与介绍

最后更新日期：2024-02-22 UTC

### 目录

1. 载具类
    - 列车
    - 路面车辆
    - 航空器
    - 船舶
2. 工业类
    - FIRS系
    - 其他
3. 车站类
4. 轨道与道路类
    - 轨道
    - 道路
    - 特殊
5. 图形替换类
    - 高清
    - 像素
6. 景观美化类
    - 房屋
    - 物件/物体
7. 其他

- 主要扩展包家族介绍
- 特别推荐列表
- NewGRF技术

### 载具类
----------

载具类是OpenTTD NewGRF当中体量最大的类别。其中又以火车拓展包数量最多。

### 工业类
----------

#### 1.1 FIRS（FIRS系）

FIRS是Andythenorth开发的工业扩展套装。由于其有中文翻译，在中文玩家社区内较为热门。

#### 1.2 AXIS（FIRS系）

AXIS是基于FIRS的工业拓展套装，相较于FIRS其拥有更复杂的产业链，对于多人游戏和想要挑战自己的玩家是一个可以尝试的选择。

AXIS由Emperor Jake开发。

#### 1.3 PIRS（FIRS系）

#### 1.4 AIRS（FIRS系）

AIRS，即Ages of Industries，是另一个基于FIRS的工业拓展套装。其基于北美的产业体系设计。AIRS最大的特点是加入了基于年份和时间的产业链。玩家在当中必须时刻关注新工业与新技术的发展。同时，在使用AIRS的时候工业会经常开张与倒闭。

AIRS偏经营向，对于多人游戏和挑战玩家是一个不错的选择。但是，AIRS目前可能比较不稳定。

AIRS由不知道谁开发。<!--这里要改-->

#### 2. Real Industries

#### 3. OpenGFX+ Industries

#### 3.1 OpenGFX+ Industries Manpower

#### 4. ECS系

#### 5. YETI系

### 车站类
----------

#### 1. AuzStations

#### 2. Kiwitree Stations

#### 3. ISR（工业车站补充套装）

#### 4. JapanSet Stations

#### 5. OpenGFX+ Stations

#### 6. OpenGFX2 Stations

#### 7. ChinaSet: Platform and Stations

#### 8. Hungarian Stations

#### 9. Timberwolf's Stations

### 轨道与道路类
----------

> 关于道路类，这里仅讨论OpenTTD 1.10 中加入的NRT道路。对于图形替换的道路包，如American Road Replacement Set，由于其并不可以与NRT道路共存，故指南中不会涉及。

#### 1. U&Ratt 1.0

U&Ratt是OpenTTD中迄今为止最大最完备的道路拓展包。

U&Ratt由Ufiby开发。

#### 2. RattRoad

RattRoad是自OpenTTD 1.10以来加入道路种类起较早出现的道路拓展包。

RattRoad由？？？开发。

#### 2.1 JFRattRoad

JFRattRoad是RattRoad的一个分支。其最大特色是有中文翻译。

JFRattRoad由John Franklin翻译制作。

#### 3. CZTR Roads

#### 4. Quast65's Tramtracks

### 图形替换类
----------

### 景观美化类
----------

### 其他
----------

#### 1. DisablerGRF

禁用东西的GRF，在不想要游戏中的某功能时尤其有用。由Gwyd开发。

#### 2. SmallMan

（在14.0之后已无必要，由Gwyd开发）

#### 3. Greenscreen

绿幕GRF，为内容创作者设计。

Greenscreen由WenSim开发。

### 主要扩展包家族介绍
----------

#### 1. OpenGFX+系

#### 2. JapanSet系

#### 2.1 JapanSet+系

#### 3. KoreanGRF系

#### 4. Andythenorth的GRF以及其衍生分支

#### 5. ChinaSet（中国包）

#### 6. xUSSR系

#### 7. Auz系

#### 8. CZTR系

### 特别推荐列表
----------


### NewGRF技术
----------

NewGRF这个名字听起来或许有点儿拗口。其实它是由两部分——“New”和“GRF”——拼接在一起的。“New”代表“新”，而“GRF”代表“Graphics file”，即“图像文件”。在OpenTTD问世之前，TTDPatch（你可以将他看作是OpenTTD的父辈）加入了NewGRF功能，允许玩家自行编制游戏扩展。

在NewGRF的发展过程中，玩家社区开发了一些程序与方法以编制NewGRF。目前，可以用于编制NewGRF的语言有四种：

- NFO
- NML（NewGRF Meta Language）
- YAGL（Yet Another GRF Language）
- Python（使用 grf-py）
- m4

另外也有一些工具可以用于编写NewGRF：

- grfcodec（NFO使用的编译器）
    - nforenum（语法规范程序）
- nmlc（NML使用的编译器）
- yagl（YAGL语言使用的编译器）
- grf-py
- TrueGRF
- grf2html（已过时，用于生成文档）
- GRFMaker（已过时）

NML与grf-py是基于NFO的。

NFO是最早用来编制GRF的语言。1995年的TTD当中的GRF文件便是采用NFO编制。它的特点如下：

- 完整性：NFO文件可以记录一个GRF中所有的信息；
- 易读性：NFO文件将GRF文件转化为可读的文字与方位信息，在一定程度上提升了可读性，但是还是需要一定的经验才可以流畅阅读。

在开发GRF的过程当中，玩家社区逐渐意识到NFO本身的局限性。NFO不支持扩展的列表，语法复杂难懂，源文件中的错误也难以被编译器检查出来。社区的开发者迫切需要一种可拓展、兼容性好的语言来替代NFO。在这种情形下，开发者拿出了两种方案：m4与NML。

### m4

m4是一种语言。常用于编写车站。

### NML

NML，即NewGRF Meta Language，是一种基于NFO与python的C风格NewGRF开发语言。NML提供了许多为开发者提供便利的特性：

- 可模块化。与 NFO 不同，NML 允许使用单独的语言文件和自定义标签文件。此外，它还支持预定义的精灵和模板。此外，它还支持预定义的精灵和模板，开发人员可以轻松地重复使用它们，而无需重新定义精灵。
- 多语言支持。使用 NFO 为中文和日文等使用 Unicode 字符的语言添加翻译非常困难（例如，JapanSet 甚至没有日文翻译），而 NML 简化了整个过程。
- 格式化。NML 是一种 C 风格语言。与 NFO 相比，它具有更好的可读性。

大多数“现代“NewGRF都是基于NML的。NML是目前NewGRF开发人员最常用的语言。

### GRF是如何被开发出来的？

GRF的开发通常由目的出发。以中国包（新国铁包）的开发为例，流程如下：

- 选取目标
    - 国铁机车
    - 国铁站台
    - ……
- 选取使用的工具
    - vox & MagicaVoxel（图像）
    - NML & nmlc（代码）
    - python（自动化）
- 满足**GRF的需求**
    - 代码
    - 图像
- 满足目标

这个时候，GRF的开发就已经完成了，但是我们还想更好一点儿，于是——

- 选取许可证
- 上传至官方内容分发服务器

于是你就可以在你最爱的水果商店里面找到新鲜出炉的GRF了 :-)