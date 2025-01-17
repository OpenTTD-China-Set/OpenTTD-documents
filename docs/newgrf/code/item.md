# 物品块（Item）

物品块用来在 NewGRF 中新增或修改物品（载具、车站、房屋、物件〔Objects〕、全局变量等）。

一般而言，一个 Item 块中会包含两项内容：`properties`，即“属性”，和 `graphics`，即“图像”。前者可以粗略理解为“游戏中不能随时变化”的数据，后者可以理解为“可以编写代码使这项在游玩的时候改变”的数据。

需要注意的是，绝大多数时候 `graphics` 块也可以包含除图像以外的数据，如对于列车而言，可以在 `graphics` 块中重新定义列车的速度、功率、容量、长度等，不能简单理解为“`graphics` 只能包含图像”。

```cpp
item(<特性>, <名称> [, <ID>]){
  property {
    <property 块的内容>
  }
  graphics {
    <graphics 块的内容>
  }
}
```

火车还可以使用 `livery_override` 块，代码格式和 `graphics` 块类似，需要传递一个车厢 ID 参数。

```cpp
item(...) {
  property {...}
  graphics {...}
  // livery_override 块内容格式与 graphics 块内容格式相同
  livery_override(<车厢 ID>) {<livery_override 块的内容>}
}
```

## 参数详解

### 特性

可以在 OpenTTD 自带的 15 个特性中自由选择。

| 常量               | 特性       |
|--------------------|----------|
| FEAT_TRAINS        | 列车       |
| FEAT_ROADVEHS      | 道路车辆   |
| FEAT_SHIPS         | 船舶       |
| FEAT_AIRCRAFT      | 航空器     |
| FEAT_STATIONS      | 火车站     |
| FEAT_CANALS        | 运河与河流 |
| FEAT_BRIDGES       | 桥梁       |
| FEAT_HOUSES        | 房屋       |
| FEAT_GLOBALVARS    | 全局变量   |
| FEAT_INDUSTRYTILES | 工业地块   |
| FEAT_INDUSTRIES    | 工业       |
| FEAT_CARGOS        | 货物       |
| FEAT_SOUNDEFFECTS  | 声效       |
| FEAT_AIRPORTS      | 机场       |
| FEAT_SIGNALS       | 信号       |
| FEAT_OBJECTS       | 物件       |
| FEAT_RAILTYPES     | 铁路       |
| FEAT_AIRPORTTILES  | 机场地块   |
| FEAT_ROADTYPES     | 公路       |
| FEAT_TRAMTYPES     | 电车道     |
| FEAT_ROADSTOPS     | 汽车站     |

### 名称

item 块的名称。

```{note}
名称也可以用来代替数字 ID。如，事先已经定义一车厢 `item(FEAT_TRAINS, train_wagon, 1145)`
时，在需要引用这个车厢数字 ID 的时候可以不使用 `1145`，而是直接使用 `train_wagon`，
NMLC 会自动将 item 块的名称替换成对应的数字 ID。
这种做法有助于提升代码可读性，省去数字 ID 的记忆成本。
```

### ID

ID 为可选参数，只有正整数 ID 会被 NMLC 识别。如果没有特别指定 ID 则 NMLC 会在编译时自动分配一个 ID。

将 ID 指定为 `-1` 时 NMLC 也将在编译时自动分配一个 ID。

### 车厢 ID

`livery_override` 使用 `<车厢 ID>` 判断是否挂接到对应车厢。车厢 ID 可以使用物品名称，也可以使用数字 ID，更推荐前者。

当当前定义的列车机车挂载车厢 ID 对应的车厢时，游戏将会根据 `livery_override` 块中定义的内容修改挂接的车厢。

## Property 块

Property 块内容的格式如下：

```cpp
property {
  <项目 1>: <表达式 1>;
  <项目 2>: <表达式 2>;
  <项目 3>: <表达式 3>;
  /* 苹果香蕉梨 */
  <项目 n>: <表达式 n>;
}
```

Property 块中有一系列项目与其对应的表达式。每个项目通常对应物品的一项特征，如对于列车而言，`speed` 项目对应的表达式就决定了列车的速度上限。
一系列的项目与其对应的表达式聚合在一起就构成了 Property 块。

每种[特性](#特性)所拥有的项目都不同。具体可以参见 <https://newgrf-specs.tt-wiki.net/wiki/NML:Main>。

Property 块中的表达式一般而言**不可以在游戏进行时变动**，换言之，表达式必须在进入游戏之前就决定。

部分项目要求表达式必须在编译时就确定，也就是说**完全无法改动**。

也可以在表达式中使用变量或者 NewGRF 参数，可以使用的变量仅限于[附表一中所列变量](#附表一property-块表达式中可用的变量)。详细列表参见 <https://newgrf-specs.tt-wiki.net/wiki/NML:General#General_variables>。

### 样例：定义 Abuabah 牌电车的属性

```cpp
item (FEAT_ROADVEHS, abuabah_tram) {
  property {
    name:                 string(STR_NAME_HEREFORD_TRAM); // 电车所使用的名称
    climates_available:   ALL_CLIMATES;   // 电车在什么气候下可用
    introduction_date:    date(1940,1,1); // 电车最初可用日期
    speed:                60 km/h;        // 电车限速
  }
  graphics {...}
}
```

### 样例：根据 NewGRF 参数决定机车限速

```cpp
grf {
  /* 海狸尾巴…… */
  param 0 {
    param_higher_speed_limit {
    type: bool;
    bit: 0;
    def_value: 1;
    }
  }
}
item (FEAT_ROADVEHS, abuabah_tram) {
  property {
    /* 肉汁奶酪薯条…… */
    // 当启用“更高速度限制”参数时，将速度限制改为 80 km/h
    // 否则使用 60 km/h 的速度限制
    speed: param_higher_speed_limit ? 80 : 60 km/h;
  }
  graphics {...}
}
```

## Graphics 块

Graphics 块中有一系列项目与其对应的表达式。每个项目通常对应物品的一项特征，如对于列车而言，`default` 项目对应的表达式就决定了列车的默认图像。
一系列的项目与其对应的表达式聚合在一起就构成了 Graphics 块。

每种[特性](#特性)所拥有的项目都不同。具体可以参见 <https://newgrf-specs.tt-wiki.net/wiki/NML:Main>。

Graphics 块中的表达式一般而言**可以在游戏进行时变动**，表达式也可以是一个 [Switch 块](./switch.md)，
根据当前或其他物品的一些变量或属性来决定当前物品的某个数值。

Graphics 块块如其名，通常包含图像，但不仅限于图像。如列车的速度上限就可以在 Graphics 块中定义（载具的速度与一些其他项目可以同时在 property 与 graphics 块中定义）。
游戏会在恰当的时刻分析表达式所对应的数值，并使用新的数值来显示或更改某些项目，如游戏会在渲染行进中的列车时判断 `default` 项目表达式（可以是一个 [Switch 块](./switch.md)）的结果，并用这个结果来替换列车图像。

## Livery Override 块

Livery override 只适用于机车。虽然字面意义为“重载涂装”，实际上也可以重载除图像以外的项目，如车厢速度上限等。

Livery override 块的格式与 Graphics 块的格式几乎一致，唯一不同点在于本块需要额外提供一个车厢 ID。
当当前定义的列车机车挂载车厢 ID 对应的车厢时，游戏将会根据 `livery_override` 块中定义的内容修改挂接的车厢。

```cpp
item(FEAT_TRAINS, ...) {
  property {...}
  graphics {...}
  // livery_override 块内容格式除 <车厢 ID> 外与 graphics 块内容格式相同
  livery_override(<车厢 ID>) {<livery_override 块的内容>}
}
```

使用 livery override 可以做到 <u>JapanSet3: Trains</u>、<u>JP+ 主要私铁</u>或<u>中国包：火车</u>中使用单一种类车厢连接不同动车组车头可以显示不同图像的功能。
方法是在动车组车头的 livery override 块中规定某种车厢所使用的图像。

样例：

```cpp
item(FEAT_TRAINS, multiple_unit_wagon) {
  property {...}
  graphics {...}
}

item(FEAT_TRAINS, roast_potatoes) {
  property {...}
  graphics {...}
  livery_override(multiple_unit_wagon) {
    // 当 multiple_unit_wagon 连接至 roast_potatoes 上时使用 roast_potatoes 图像
    default: spriteset_roast_potatoes;
  }
}

item(FEAT_TRAINS, baked_beans) {
  property {...}
  graphics {...}
  livery_override(multiple_unit_wagon) {
    // 当 multiple_unit_wagon 连接至 baked_beans 上时使用 spriteset_baked_beans 图像
    default: spriteset_baked_beans;
  }
}
```

在上面这个例子中，`roast_potatoes` 与 `baked_beans` 是两种不同的机车。在挂载 `multiple_unit_wagon`
至这两种机车上时，游戏将会根据两机车 `livery_override` 块中得出的数值显示图像。在这个例子中，
挂载至 `roast_potatoes` 上时将使用 `spriteset_roast_potatoes`，而挂载至 `baked_beans` 上时将使用 `spriteset_baked_beans`

## 附表一：Property 块表达式中可用的变量

输出范围等参见 <https://newgrf-specs.tt-wiki.net/wiki/NML:General#General_variables>。

| 变量                    | 意义                                       |
|-------------------------|------------------------------------------|
| ttd_platform            | 当前 TTD 平台                              |
| ttdpatch_version        | TTDPATCH 版本                              |
| openttd_version         | OpenTTD 版本                               |
| current_palette         | 当前使用的调色盘                           |
| date_loaded             | 加载日期                                   |
| year_loaded             | 加载年份                                   |
| starting_year           | 当前存档起始日期                           |
| climate                 | 当前场景气候                               |
| game_mode               | 游戏模式（区分是在场景编辑器中还是在游戏中） |
| loading_stage           | NewGRF 加载阶段                            |
| difficulty_level        | 游戏难度                                   |
| desert_paved_roads      | 沙漠中铺装道路                             |
| second_rocky_tileset    | 额外岩石图像                               |
| train_width_32_px       | 列车在车库中的预览图像宽度是否为 32px      |
| traininfo_y_offset      | 列车在车库中的预览图像之 y 偏移值          |
| traffic_side            | 当前道路方向                               |
| freight_trains          | 列车货物重量倍数                           |
| plane_speed             | 飞机速度因子之分母                         |
| ttdpatch_flags          | ttdpatch 启用的 flags                      |
| base_sprite_2cc         | 双公司颜色的基本 sprite                    |
| base_sprite_foundations | 地基的基本 sprite                          |
| base_sprite_shores      | 海岸线的基本 sprite                        |
| map_type                | 地图长宽比较                               |
| map_min_edge            | 地图最短边长                               |
| map_max_edge            | 地图最宽边长                               |
| map_x_edge              | 地图 X 轴长度                              |
| map_y_edge              | 地图 Y 轴长度                              |
| map_size                | 地图格数                                   |
| long_bridges            | 是否启用长桥梁                             |
| gradual_loading         | 是否渐进装载货物                           |
| wagon_speed_limits      | 是否启用车厢限速                           |
| signals_on_traffic_side | 铁路信号是否在道路行进方向一侧             |
| electrified_railways    | 是否启用电气化铁路                         |
| dynamic_engines         | 是否启用动态机车                           |

以下变量在 OpenTTD 中固定为某数值，只在 TTDPatch 中有变化，无须在实际开发中使用。

- temperate_snowline
- bridge_speed_limits
- unified_maglev
- variable_runningcosts
- newtrains
- newrvs
- newships
- newplanes
- newhouses
- newindustries
- newcargos
- 256_persistent_registers
- inflation
- map_seed
