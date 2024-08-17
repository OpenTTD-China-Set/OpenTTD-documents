# 认识终端

编译 GRF 必须使用终端。

在 Windows 下，你可以通过 Windows+R 组合键打开“运行”界面，然后输入`cmd`或`powershell`打开终端。在我们的场景下，使用`cmd`和`powershell`基本没有区别；推荐使用 PowerShell。

进入终端后，使用`cd`命令可以切换目录；使用`dir`或者`ls`（仅 PowerShell）可以列出当前目录下的所有文件。在使用命令的时候可以使用`q`键左边的`tab`键补全命令，加快打命令的速度。

如果不知道某个命令如何使用，可以在打完之后加`--help`参数；或者，如果使用 PowerShell，可以使用`man`命令来查询使用手册，如：

```bash
nmlc --help
man nmlc
```

优先使用`<命令> --help`，在报错之后再尝试`man <命令>`。

假设你把你的工程文件放在`C:\OpenTTD\GRF\`目录下，主文件是`my_grf.nml`，你可以通过这些步骤编译 GRF：

```bash
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

>[!TIPS]
> 除了 PowerShell、CMD 之外，还可以使用 Bash。你可以通过安装 Git 以在 Windows 上使用 Bash。
