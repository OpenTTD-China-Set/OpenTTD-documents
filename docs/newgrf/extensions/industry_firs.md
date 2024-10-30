# 工业——FIRS 及其衍生拓展

FIRS（FIRS Industry Replacement Set[^ra]）是一个进阶工业拓展包，
由 Andythenorth 创作，
旨在替代和扩展原版游戏中的工业系统。
FIRS 的工业系统相较原版更加复杂多样，经济系统也更加丰富，具有挑战性。

[^ra]: 这是一个[递归缩写](https://zh.wikipedia.org/zh-hans/%E9%80%92%E5%BD%92%E7%BC%A9%E5%86%99)（[百度百科](https://baike.baidu.com/item/%E9%80%92%E5%BD%92%E7%BC%A9%E5%86%99/2216444)）

## 原版 FIRS

目前 FIRS 最新版是 4.15.1[^outdated]。FIRS 当中包含：

- 83 种货物
- 78 种产业
- 5 种经济体系

[^outdated]: 版本号可能过时，不过 <https://grf.farm/firs/latest.html> 永远指向 FIRS 最新版页面。

### 原版特色

“供应物资”机制

: 玩家可以通过向初级产业提供工业或农业物资的方式提升产量。

图像美观

: FIRS 内置一套 FIRS 景观物品，在运输的同时也可以造景。

动态图像

: 所有产业建筑有无雪和有雪两种图像，在模拟[季节变化](./graphics_replacement.md#opengfx-landscape)时
图像可以动态变化。

产业永远不倒闭

: 与原版不同，使用 FIRS 时产业建筑永远不会倒闭。

你可以访问 <https://grf.farm/firs/latest.html> 查看更多信息。

## AXIS

AXIS 即 Another eXtreme Industry Set，相较于 FIRS，其货物、工业建筑更多，
由 EmperorJake 根据 FIRS 代码开发。

AXIS 是 XIS（eXtreme Industry Set）的继任者。后者是 FIRS 3 Extreme 经济的扩展，
虽然结合了其他经济元素，内容丰富，但体系较为混乱，代码限制多，货物过于通用。
AXIS 修复了 XIS 的一些缺点。
提供两种不同的经济体系，
“钢铁都市”基于 FIRS 4“钢铁城”；
“热带天堂”并不基于某一特定经济模式，不过结合了 FIRS 的“炎热国家”和“热带基础”经济体系等。

两种经济体系都增加了大量的货物产业链，并削弱了经济体系中港口的作用，将部分工业链条独立出来。
“热带天堂”经济体系更注重于食品生产，并更适合热带地图。

需要注意的是，AXIS 使用了所有可用的货物类型槽（64 个），
因此 AXIS 与其他所有工业 GRF 都不兼容。

AXIS 添加了一些新的货物类型，但应当与大多数较新的载具包兼容。

<https://github.com/EmperorJake/AXIS>

## AIRS

AIRS（Age of Industries Replacement Set）同样基于 FIRS 4 代码，由 andysine 开发。
AIRS 基于特定的区域和历史经济（北美）。
在使用 AIRS 时，游戏产业链会随时间推移逐渐复杂，最终达到一个半现实的经济体系。

随着时间推移，玩家需要调整货物网络，以应对生产变化与货物、需求的变化。
建设加工厂是 AIRS 的重要部分，加工厂成本也经过调整，显著降低。

<https://www.tt-forums.net/viewtopic.php?t=90529>

作者同时提供了 The Greenest Valley（翠绿谷）与 Mountains and Prairies（山脉和草原）两个场景，
均使用了 AIRS。

<https://www.tt-forums.net/viewtopic.php?t=90703> （翠绿谷）\
<https://www.tt-forums.net/viewtopic.php?t=90531> （山脉和草原）
