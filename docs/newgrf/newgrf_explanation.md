# NewGRF 简介

NewGRF 是 OpenTTD 的核心组件。玩家可以利用 NewGRF 添加载具等。

## NewGRF 可以做什么

```{note}
原作者：FLHerne » 2013-03-14 12:31\
原标题：Re: Graphics sets confusing\
原链接：[TT-Forums](https://www.tt-forums.net/viewtopic.php?p=1070084#p1070084)
```

NewGRFs aren't necessarily just 'art packages'; they can do a lot beyond just visual stuff, and many don't even contain any art at all.
Depending on the grf, they can do all sorts of things:

- Add vehicle types. (probably the most common).\
  These often have more features than the default vehicles, for example:

  - Support for non-default cargo types
  - Speed limits for wagons, not just locomotives
  - Support for 'autorefitting' (refitting in stations).
  - Different graphics depending on date, or the type of wagons being pulled, etc.
  - Maximum ranges for aircraft.
  - Trams (the default vehicles don't include any).

  Most vehicle sets can be used together, but not that they might not be 'balanced' - the running costs and maximum speeds might make vehicles from one set always preferable. Many such sets disable the default vehicles.
  There's a slight variant:
  - Modify the existing vehicles directly, changing the stats or introduction dates.

  There aren't many of these, and they can be problematic when used with other grfs affecting the default vehicles.

- Modify infrastructure.

  - Add new types of town buildings.

    Mostly just for aesthetics, but it's possible for such sets to control the rate of town growth.
    These can be used together, but sets trying to do 'clever stuff', e.g. TaI, won't be able to do that when used with others.

  - Add station types.

    These are mostly just artistic. Some display the amount and type of cargo waiting, which can be useful.
    All can be used together, I think.

  - Add new types of railway.

    This includes types of track with speed limits, or third-rail electrified tracks, or narrow gauge.
    Most such grfs remove the default game's Monorail and Maglev tracks.
    These can be used together to some extent, but there's a quite restrictive limit on the number of different track types that can be defined. If you use a combination of sets that between them define >16 types of track, it won't work properly.

  - Change the appearance of roads.

    No gameplay effect; some sets might display different road graphics depending on date.
    These can't be used together. Also, they don't alter the road surface on bridges.
    A variation on this are tramtrack grfs, these change the appearance of tramways.*

  - Change the bridge types.

    These replace the default bridge types, and can have slightly more types of bridges than normal.
    They can't be used together. Also, the road surface on the bridges doesn't change to match roadsets; some bridge grfs have alternate versions to match various roadsets.

  - Replace airport and dock graphics; allow rotatable airports.

    For dock graphics, last one in the list wins. I don't know what happens with airports.

- Modify industries and cargotypes

  GRFs can modify the properties of the default industries and cargos, or define additional or replacement ones.
  These often have different mechanics to the default ones, for example FIRS has a 'supply' mechanic, and ECS and TaI both have a 'stockpiling' system. Never use multiple industry grfs together unless they're specifically designed to work as a group.

- Modify the landscape.

  - Change the appearance of landscape tiles.What it says on the tin, really. For obvious reasons, one such grf at a time.
  - Add NewObjects.
    Purely for looking at, they add buildable tiles under the Landscaping toolbar. Harbour walls, trees, wind turbines, flocks of seagulls...
    These can all be used together.

- Modify basecosts.
  Change the price of terraforming, building, bribes...
  The effects of these are cumulative, IIRC

*Of course, you can't build tramways at all without a grf that defines some trams.

There are one-off (so far) grfs that do other stuff. Someone remind me if I forgot any significant categories, please.

Remember that a single grf can do any combination of these things - for example, several sets that add rail stations also replace dock and shipyard graphics, some townsets replace road and bridge graphics, there's one trainset (NARS) that actually defines a cargotype and has been known to conflict with ECS industries. Most are reasonably self-contained, though.

### 关系图

```{mermaid}
flowchart TD
  NewGRF --> ae[Add extra contents]

  ae -----> Vehicles
  Vehicles --> au[Vehicle autorefitting]
  Vehicles ---> Trains
  Vehicles ---> Ships
  Vehicles ----> Planes
  Vehicles ----> rv[Road Vehicles]

  ae --> Industries
  Industries -.-> md

  ae ---> rp[Replace graphics]
  rp --> Landscape
  rp --> Seas

  ae ----> infra[Infrastructure]
  infra --> Bridges
  infra ---> Rails
  infra ---> Roads
  infra ----> Stations
  infra ----> tb[Town Buildings]

  NewGRF ---> ch[Change game mechanic]
  ch --> md[Modify cargo payments]
  ch ---> st[Modify station rating algorithms]
  ch ---> bc[Modify basic costs]
```

## NewGRF 是什么

NewGRF 当中的“New”（新）指代的是“自定义”的新，不是由游戏提供的“旧”图形资源文件。

不严谨地说，一个 GRF 可以分为程序和图像两部分。图像是显示的内容，程序控制显示的内容。

在读取的时候，游戏先读取 GRF 识别符——你可以看作是 GRF 的“身份证”——以及 GRF 设置，读取其中的 GRF 编号、图像信息、可用参数（设置）等，然后开始读取剩余的部分。

```{important}
GRF 中的所有内容实际上都是“图像”，只不过这些图像包括“pseudo-sprite”（伪图像）与“realsprite”（真图像）。“伪图像”即为代码，“真图像”即为“真正看到的图像”与重着色图像这个特例。为了讲解简便，后文统一以“代码”指代“伪图像”，“图像”指代“真图像”。整个 GRF 就是由图像构成的。这也是为什么你会在一些技术板块中看到“这个 Sprite 如何如何”。
```

加载完成后，你就可以玩到 GRF 中的各种载具与建筑了。

### 关系图

```{mermaid}
flowchart TD
  NewGRF --> Sprite
  Sprite --> pseudo-sprite
  Sprite --> realsprite
  subgraph "NML 部分整合的部分"
    realsprite --> image
    realsprite --> recoloursprite
  end
  subgraph "NML 已整合的部分（无需编写 Action）"
    pseudo-sprite --> actions
    actions --> action0x01
    actions --> action0x02
    actions --> many_actions[...]
  end
```
