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
- scoop（仅 Windows）
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
