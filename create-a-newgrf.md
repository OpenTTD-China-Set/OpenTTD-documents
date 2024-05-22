# NewGRF 编写教程

编写NewGRF有固定的流程。

## 程序

我们推荐使用NML来编写NewGRF。

### NML的下载与安装

可以使用多种方式来安装nmlc

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
 - 将放置的路径添加到PATH。

安装完以后可以在终端内执行以下命令来查看nml版本
```
nml --version
```
如果汇报了正确版本，恭喜你，你已经成功安装了nml，跨过了第一道门槛。