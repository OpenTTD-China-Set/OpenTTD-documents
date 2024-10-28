# 认识终端

```{caution}
我们日常见到的应用程序大部分都是图形化程序。这些程序有一个图形化界面，
大部分可以直接使用双击 exe 的方式打开。
nmlc 并不具有图形化界面，是一个控制台程序。双击 exe 的方法是绝对不行的，
必须使用终端打开 nmlc。
```

编译 GRF 必须使用终端。

可以使用下面的终端速查图查看使用的终端。

```{mermaid}
flowchart TD
  Start[开始]
  Start --> OS{操作系统}
  OS --> Windows
  Windows --> PowerShell
  Windows --> CMD
  Windows --> Git{是否有 Git}
  Git -->|是|GB[Git Bash]
  GB -..- Bash
  OS --> Linux
  Linux --> Bash & Zsh
  OS --> MacOS
  MacOS --> Version{系统版本}
  Version -->|Catalina 前|Bash
  Version -->|Catalina 后|Zsh
```

支持或使用 Bash、Git Bash 与 Zsh 的操作系统通常都附带有 [POSIX 环境](https://zh.wikipedia.org/wiki/%E5%8F%AF%E7%A7%BB%E6%A4%8D%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E6%8E%A5%E5%8F%A3)（[百度百科](https://baike.baidu.com/item/%E5%8F%AF%E7%A7%BB%E6%A4%8D%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E6%8E%A5%E5%8F%A3)）
必须的系统工具、组件等。Windows 并没有这些组件。

## 打开终端

### Windows

在 Windows 下，你可以通过 Windows+R 组合键打开“运行”界面，
输入 `cmd`、`powershell` 或 `sh`（Git Bash，需要事先安装 Git）打开终端。
使用 `cmd`、`powershell` 或 `bash` 在编写 GRF 时基本没有区别；
推荐使用 PowerShell 或者 Git Bash。

### MacOS

在 MacOS 下，你可以按 {kbd}`⌘`+{kbd}`空格` 打开搜索，随后输入“Terminal”打开终端。

### Linux[^basics]

大部分发行版支持使用 {kbd}`Ctrl`+{kbd}`Alt`+{kbd}`T` 打开终端。

[^basics]: ~~这个是基本功吧~~

## 基本功能

在终端中，我们可以通过输入“程序名称＋参数”的方式来执行程序，并传递一些额外的信息给程序。
当我们在终端中输入“程序名称 + 参数”时，终端会先找到指定的程序，然后将参数传递给程序。
参数是程序运行时所需的附加信息或选项，用于调整程序的行为。
程序接收这些参数，并根据参数执行相应的操作。
不同的程序支持的参数不同，
通常可以通过输入 `program_name --help` 来查看该程序支持的参数列表。

```bash
程序名称 参数1 参数2 ...
```

### 列出当前目录文件

```bash
# 输入
ls -l

# 输出
total 168
drwxr-xr-x  2 jeremy jeremy  4096 Sep 18 21:16  folder-1
drwxr-xr-x  7 jeremy jeremy  4096 Oct  7 21:24  folder-2
```

在这个例子中，`ls` 是程序名称，用于列出目录内容，`-l` 是参数，表示以详细列表的格式显示文件信息。

```{important}
CMD 不支持 ls，不过在 CMD 中可以使用 dir 命令列出当前目录下所有文件。
```

### 复制文件

```bash
cp source.txt destination.txt
```

这里 `cp` 是程序名称，用于复制文件，`source.txt` 和 `destination.txt` 是参数，分别表示源文件和目标文件。

### 执行脚本

```bash
python script.py arg1 arg2
```

在这个例子中，`python` 是程序名称，`script.py` 是要运行的脚本文件，`arg1` 和 `arg2` 是传递给脚本的参数。

### 切换目录

```bash
cd ../
```

在这个例子中，`cd` 是程序名称，`../` 是切换的目录。

<!--autocorrect: false-->

| 项目 | 意义           |
|------|----------------|
| ..   | 父目录         |
| .    | 当前目录       |
| /    | 根目录或分隔符 |

<!--autocorrect: true-->


```{note}
在使用命令的时候可以使用 {kbd}`q` 键左边的 {kbd}`tab` 键补全命令，加快打命令的速度。
```

```{important}
在 Windows 中切换盘符比较麻烦。PowerShell 支持输入 `cd C:\foo\bar` 直接切换，
但是在 CMD 中则必须使用 `C:` `D:` 这种“盘符＋冒号”的格式切换。

Git Bash 则是另一套规则，不同的盘在根目录下。
比如想要切换到 D 盘，就必须使用 `cd /d` 切换（注意不要打错）。

Linux 与 MacOS 由于没有盘符，不需要进行这样的操作。

```

假设你把你的工程文件放在 `C:\OpenTTD\GRF\` 目录下，主文件是 `my_grf.nml` ，你可以通过这些步骤编译 GRF：

```bash
# 切换到工作目录
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

## 相关视频

<iframe width="100%" height="400px" src="https://player.bilibili.com/player.html?isOutside=true&aid=251924452&bvid=BV1cY411s7Yt&cid=449705744&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

---

<iframe width="100%" height="400px" src="https://www.youtube-nocookie.com/embed/I4EWvMFj37g?si=gG17pnDUknivP-wd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<script src="https://giscus.app/client.js"
        data-repo="openttd-china-set/openttd-documents"
        data-repo-id="R_kgDOLV0ztQ"
        data-category="Announcements"
        data-category-id="DIC_kwDOLV0ztc4Cf-oT"
        data-mapping="pathname"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="bottom"
        data-theme="preferred_color_scheme"
        data-lang="zh-CN"
        crossorigin="anonymous"
        async>
</script>
