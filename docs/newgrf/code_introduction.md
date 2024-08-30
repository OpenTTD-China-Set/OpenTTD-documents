# 程序

编写 NewGRF 有固定的流程。

NewGRF，即 New graphics resource files，是用于 Transport Tycoon、Transport Tycoon Deluxe、OpenTTD 等游戏的图像文件；当中可以包含自定义代码，因此也可以用来拓展游戏内容。所有的 GRF 都不能跳脱出游戏所划定的沙盒，因此相较于其他游戏的模组 GRF 的自由度较少；你可以将 NewGRF 理解为游戏模组。

OpenTTD NewGRF 的一个最大特点就是兼容性好。哪怕是使用过时技术、过时标准编写的 GRF，一般而言，只要文件没有损坏，OpenTTD 都可以正确读取 GRF 内容并加载其内容。

如果想要编写程序，最好自己有一些编程基础。\
编写 NewGRF 最好准备一台电脑。

我们推荐使用 NML 来编写 NewGRF。当然，你也可以使用 grf-py 和 yagl。强烈不建议使用 NFO 编写 GRF。\
如果你不知道如何使用终端，我建议你先阅读“使用终端”。

## 下载与安装 NML

可以使用多种方式来安装 nmlc。推荐使用 pip 或者 scoop 安装 nml。

- pip

  ```bash
  pip3 install nml
  ```

- scoop（仅 Windows，支持自动更新）

  请注意 Scoop 在部分地区可能访问较慢

  ```bash
  scoop bucket add openttd-bucket https://github.com/wensimehrp/openttd-bucket
  scoop install openttd-bucket/nml
  ```

- 手动安装（以 Windows 为例）

  在 GitHub 或 `openttd.org` 下载 NML；
  下载完成后将 nml 放置到你指定的文件夹（如 `C:\tools\nml`）；
  打开控制面板或按 Win+Q 搜索 env，选择“编辑系统的环境变量”或“编辑账户的环境变量”并编辑 PATH 环境变量；注意不要删除任何环境变量！
  将放置的路径添加到 PATH。

  如果选择手动安装，你也可以选择不将`nmlc`的路径加入 PATH 中并在编译时手动指定编译器路径。

- Git clone（不安装，便携版）

  ```bash
  git clone https://github.com/OpenTTD/nml
  python3 nmlc
  ```

  这种方式直接从仓库拉取 NML 源码，并手动执行其中的 NMLC 入口点。

安装完以后可以在终端内执行以下命令来查看 nml 版本

```bash
nmlc --version
```

如果汇报了正确版本，恭喜你，你已经成功安装了 nml，跨过了第一道门槛。

```{important}
由于 NML 目前尚在开发中，尚有一些程序错误，我们建议定期更新 NML 以避免 GRF 出错。
```
