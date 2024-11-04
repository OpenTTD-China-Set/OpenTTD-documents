# OpenTTD 社区文档

```{toctree}
:caption: 货物分配
:hidden:
:glob:

docs/game/cargodist/*

```

```{toctree}
:caption: 游戏拓展介绍
:hidden:
:glob:

如何寻找拓展 <docs/newgrf/extensions_introduction>
NewGRF 简介 <docs/newgrf/newgrf_explanation.md>
docs/newgrf/extensions/*
docs/newgrf/extensions/main/*
```

```{toctree}
:caption: NML NewGRF 开发
:hidden:
:glob:

NewGRF 开发简介 <docs/newgrf/code_introduction.md>
docs/newgrf/code/terminal.md
docs/newgrf/code/*
docs/newgrf/code/extras/*
```

```{toctree}
:caption: Action
:hidden:
:glob:

Action 简介 <docs/newgrf/actions_introduction.md>
docs/newgrf/actions/*
```

```{toctree}
:caption: 绘制图像
:hidden:
:glob:

图像简介 <docs/newgrf/sprites_introduction.md>
docs/newgrf/sprites/*
```

```{toctree}
:caption: 其他开发
:hidden:
:glob:

目录 <docs/newgrf/extras_introduction.md>
docs/newgrf/extras/*
```

```{toctree}
:caption: 其他
:hidden:

许可证 <license.md>
文档说明 <readme.md>
编写指南 <contributing.md>
```

```{toctree}
:caption: 外部链接
:hidden:
:titlesonly:

OpenTTD GitHub 页面 <https://github.com/openttd/openttd>
OpenTTD 百科 <https://wiki.openttd.org>
文档 GitHub 页面 <https://github.com/openttd-china-set/openttd-documents>
百度贴吧 <https://tieba.baidu.com/f?kw=openttd>
JGRPP 中文百科 <https://jgrzh.readthedocs.io/>
```

本系列文档是由志愿者维护的 OpenTTD 中文社区文档。
包含关于 OpenTTD 游戏的一系列说明，
如游戏特性解释、游戏拓展推荐、游戏拓展开发等。

本系列文档是社区文档，虽然挂靠在“OpenTTD-China-Set”名下，实际上没有官方“组织”或“机构”，更没有“编写委员会”。
俗话说：“众人拾柴火焰高”，在这里，我希望所有有能力的读者都可以[参与编写](https://github.com/openttd-china-set/openttd-documents)，
以为中文玩家提供更好的 OpenTTD 游戏体验。

本系列文档主要由 WenSim 编写。在编写的过程中参考了 [TT Wiki](https://tt-wiki.net)、
[OpenTTD Wiki](https://wiki.openttd.org/en/)、
[Zyliety 的系列专栏](https://www.bilibili.com/read/readlist/rl743422)等。
衷心感谢在编写过程中提供帮助的所有人。

## 向导

拓展包大大提高了 OpenTTD 的游戏体验。
你可以在[如何寻找拓展](docs/newgrf/extensions_introduction.md)及附属章节
找到 NewGRF、baseset（基本集）推荐列表。

哪怕对于游戏老手，NewGRF 也是一个难懂的概念。[NewGRF 简介](docs/newgrf/newgrf_explanation.md)章节
介绍了 NewGRF 的作用与定义。

OpenTTD 的主要拓展形式——NewGRF 结构复杂，初学者不易懂；
虽然有[半官方性质的教程](https://www.tt-wiki.net/wiki/NMLTutorial)，英语编写的教程也不易懂。
你可以阅读 [NML NewGRF 开发](docs/newgrf/code_introduction.md)及附属章节，
了解 NewGRF 的基本属性与开发要素。

NewGRF 当中最主要的内容是多样的图像。不过，NewGRF 的图像标准复杂，
“色彩深度”、“EZ”等概念在其他游戏中特别少见。
[图像简介](docs/newgrf/sprites_introduction.md)及附属章节
介绍了 NewGRF 图像的标准以及绘制技巧。

Action 是 NewGRF 的基本单元。
如果想要使用 grf-py 或 yagl 开发 NewGRF 则必须对 Action 有一定了解。
[Action 简介](docs/newgrf/actions_introduction.md)及附属章节中
详细介绍了每个 Action 的作用，以及如何使用 Action 构建 NewGRF。

---

如果本系列文档对你有帮助，请在 [GitHub](https://github.com/openttd-china-set/openttd-documents) 上
给本项目点一个 Star，也还请宣传本项目。
