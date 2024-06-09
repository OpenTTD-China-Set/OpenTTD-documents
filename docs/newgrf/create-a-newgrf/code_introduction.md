# 程序

[返回目录](./catalogue.md)

- [基本运算](./code_functions.md)
- [引导块](./code_header.md)
- [Item 块](./code_item.md)

如果想要编写程序，最好自己有一些编程基础。\
编写 NewGRF 最好准备一台电脑。

我们推荐使用 NML 来编写 NewGRF。当然，你也可以使用 grf-py 和 yagl。强烈不建议使用 NFO 编写 GRF。\
如果你不知道如何使用终端，我建议你先阅读下面的[认识终端](#认识终端)章节。

## 下载与安装 NML

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

> [!IMPORTANT]
> 由于 NML 目前尚在开发中，尚有一些程序错误，我们建议定期更新 NML 以避免 GRF 出错。

## 基本原理

不严谨地说，GRF 可以分为程序和图像两部分。图像是显示的内容，程序控制显示的内容。

在读取的时候，游戏先读取 GRF 识别符——你可以看作是 GRF 的“身份证”——以及 GRF 设置，读取其中的 GRF 编号、图像信息、可用参数（设置）等，然后开始读取剩余的部分。

GRF 中的所有内容实际上都是“图像”，只不过这些图像包括“pseudo-sprites”（伪图像）与“realsprites”（真图像）。“伪图像”即为代码，“真图像”即为“真正看到的图像”与重着色图像这个特例。为了讲解简便，后文统一以“代码”指代“伪图像”，“图像”指代“真图像”。整个 GRF 就是由图像构成的。

加载完成后，你就可以玩到 GRF 中的各种载具与建筑了。

## 认识终端

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
