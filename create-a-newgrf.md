# NewGRF 编写教程

编写NewGRF有固定的流程。

## 程序

我们推荐使用NML来编写NewGRF。当然，你也可以使用grf-py和yagl。强烈不建议使用nfo编写GRF。

### NML的下载与安装

可以使用多种方式来安装nmlc。推荐使用pip或者scoop安装nml。

- pip
```bash
pip3 install nml
```
- scoop（仅 Windows）
```bash
scoop bucket add openttd-bucket https://github.com/wensimehrp/openttd-bucket
scoop install openttd-bucket/nml
```
- 手动安装（以Windows为例）
 - 在GitHub或openttd.org下载nmlc；
 - 下载完成后将nml放置到你中意的文件夹（如C:\tools\nml）；
 - 搜索env，编辑PATH；
 - 将放置的路径添加到PATH。

安装完以后可以在终端内执行以下命令来查看nml版本
```
nml --version
```
如果汇报了正确版本，恭喜你，你已经成功安装了nml，跨过了第一道门槛。

### 基本原理

GRF可以分为程序和图像两方面。图像是显示的内容，程序控制显示的内容。

在读取的时候，游戏先读取GRF识别符——你可以看作是GRF的“身份证”，读取其中的GRF编号、图像信息、可用参数（设置）等，然后开始读取剩余的部分。

### 基本运算

nml支持以下运算符：

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
