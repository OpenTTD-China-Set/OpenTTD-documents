# 智障也能看懂的找扩展包教程与推荐和介绍

*WenSim, Mikhail, Feb.21, 2024*

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

请记住这个网址 - https://bananas.openttd.org

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

### NewGRF技术
----------

NewGRF这个名字听起来或许有点儿拗口。其实它是由两部分——“New”和“GRF”——拼接在一起的。“New”代表“新”，而“GRF”代表“Graphics file”，即“图像文件”。在OpenTTD问世之前，TTDPatch（你可以将他看作是OpenTTD的父辈）加入了NewGRF功能，允许玩家自行编制游戏扩展。

在NewGRF的发展过程中，玩家社区开发了一些程序与方法以编制NewGRF。目前，可以用于编制NewGRF的语言有四种：

- NFO
- NML (NewGRF Meta Language)
- YAGL (Yet Another GRF Language)
- Python (使用 grf-py)

NML与grf-py是基于NFO的。

NFO是最早用来编制GRF的。1995年的TTD当中的GRF文件便是采用NFO编制。它的特点如下：

- 完整性：NFO文件可以记录一个GRF中所有的信息；
- 易读性：NFO文件将GRF文件转化为可读的文字与方位信息，在一定程度上提升了可读性，但是还是需要一定的经验才可以流畅阅读。

