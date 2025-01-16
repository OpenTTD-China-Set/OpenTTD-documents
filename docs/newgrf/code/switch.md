# 切换块（Switch）

Switch 块读取一些数值，根据给定的算式计算数值，再根据计算的结果返回一定的数值。

```cpp
switch(<特性>, <范围>, <名称>, [可选参数,] <匹配表达式>) {
  <匹配数值1>: <返回值1>; // 当匹配表达式计算结果为 <匹配数值 1> 时返回 <返回值 1>
  <匹配数值2>: <返回值2>; // 当匹配表达式计算结果为 <匹配数值 2> 时返回 <返回值 2>
  default: <默认返回值>; // 匹配表达式的计算结果不匹配以上任何一条，返回 <默认返回值>
}
```

| 项目       | 效用                                                           |
|----------|--------------------------------------------------------------|
| 特性       | Switch 块的特性。只有在规定特性之后才可以使用这个特性对应的变量 |
| 范围       | Swtich 块的范围。可以规定读取当前实体父级项目的变量             |
| 名称       | Switch 块的名称                                                |
| 可选参数   | 调用 Switch 块时的可选参数                                     |
| 匹配表达式 | Switch 块匹配所使用的表达式，将计算表达式的结果                 |
| 匹配数值   | 匹配使用的数值                                                 |
| 返回值     | 匹配成功后的返回值                                             |
| 默认返回值 | 所有条目匹配不成功时的返回值                                   |

在这其中，`数值n: 返回值n` 与 `default: 默认返回值` 都是可选的。
可以将 Switch 块写成这种形式：

```cpp
switch(<特性>, <范围>, [可选参数,] <匹配表达式>) {
  return;
}
```

此时 Switch 块将会返回匹配表达式的计算结果。

## 调用

Switch 块通常在 item 的 graphics 部分或者其他 switch 块中调用。需要注意的是，无法在 spritelayout 中调用 Switch 块。

调用方式与其他编程语言中调用函数的方式类似。

```cpp
// 这个 Switch 只会返回数值 1
switch (FEAT_TRAINS, SELF, example_switch_2, 1){return;}

// 这个 Switch 会调用 example_switch_2
switch (FEAT_TRAINS, SELF, example_switch_1, 123123){
  default: example_switch_2();
}

item (FEAT_TRAINS, foo) {
  property {
    /* 我是代码…… */
  }
  graphics {
    a: example_switch_1(); // 调用 Switch，注意需要加括号
  }
}
```

此时，游戏在评估 graphics 块中 a 所对应的项目时，会先调用 `example_switch_1`，根据这个 Switch 块的结果，再直接返回一个数值或调用其他 Switch 块。
在这个例子中，a 所得到的数值就是 `example_switch_2` 匹配表达式计算值，即为 `1`。

## 参数详解

### 特性

可以在 OpenTTD 自带的 15 个[^features]特性中自由选择。

| 常量               | 特性                    |
|--------------------|-----------------------|
| FEAT_TRAINS        | 列车                    |
| FEAT_ROADVEHS      | 道路车辆（路面电车、公车） |
| FEAT_SHIPS         | 船舶                    |
| FEAT_AIRCRAFT      | 航空器                  |
| FEAT_STATIONS      | 火车站                  |
| FEAT_CANALS        | 运河与河流              |
| FEAT_BRIDGES       | 桥梁                    |
| FEAT_HOUSES        | 房屋                    |
| FEAT_GLOBALVARS    | 全局变量                |
| FEAT_INDUSTRYTILES | 工业地块                |
| FEAT_INDUSTRIES    | 工业                    |
| FEAT_CARGOS        | 货物（没有特有变量）      |
| FEAT_SOUNDEFFECTS  | 声效（没有特有变量）      |
| FEAT_AIRPORTS      | 机场                    |
| FEAT_SIGNALS       | 信号                    |
| FEAT_OBJECTS       | 物件                    |
| FEAT_RAILTYPES     | 铁路                    |
| FEAT_AIRPORTTILES  | 机场地块                |
| FEAT_ROADTYPES     | 公路                    |
| FEAT_TRAMTYPES     | 电车道                  |
| FEAT_ROADSTOPS     | 汽车站                  |

除了货物与声效之外，每种特性都有对应的独特变量。

### 范围

`范围` 一项可以设置的值只有 `SELF` 与 `PARENT`，并且决定当前读取什么实体的变量，如在使用
`FEAT_TRAINS` 时，如果将范围设置成 `SELF`，那么后方表达式中读取的就是当前车厢的有关变量。相对应地，
当范围设置为 `PARENT` 时，后方表达式中读取的就是整列车的有关变量。

有时候将范围设置为 `PARENT` 也可以访问当前特性一般而言所不能访问的变量，如在编写车站 Switch 的时候，
将范围设置为 `PARENT` 可以读取车站所属城镇的相关变量。

### 可选参数

可选参数的格式比较奇怪：

```cpp
swtich (FEAT_TRAINS, SELF, abuabah, a, b, c, a + b + c) {return;}
```

可以指定多于一个的可选参数。列出的可选参数可以在后面的表达式中、匹配数值中，或是返回值中使用。
这个例子就在表达式使用了这些可选参数：这个 Switch 块会返回三个可选参数 `a`、`b`、`c` 之和。

在调用的时候必须在括号中正确列出参数。
上列 Switch 块 `abuabah` 的调用方式即为：

```cpp
...: abuabah(1,2,3); // 1 对应 a，2 对应 b，3 对应 c
```

### 匹配表达式

游戏调用 Switch 时会计算匹配表达式的结果，再根据表达式的结果执行操作。
可以在匹配表达式中使用所有[基本运算符](./functions.md#基本运算)与当前特性对应的变量。

#### 变量

Switch 只可以读取变量，无法修改变量（寄存器另当别论）。
读取的变量与当前游戏状态相关。

所有 Switch，无论特性如何，都可以读取全局变量，如当前时间日期、场景气候类型。
每个特性除了通用变量之外还可以读取特性所对应的变量（货物、声效除外）。

举例来说，假设我现在想要规定一辆机车在 1950 年前的涂装是 A，1951 年至 1980 年的涂装为 B，1981 年后的涂装为 C，就可以这样写：

```cpp
switch (FEAT_TRAINS, SELF, switch_livery, current_year) { // current_year 是一个全局变量，会返回当前游戏年份
  0..1950: spriteset_livery_a; // 在 0 年至 1950 年这个范围内返回 spriteset_livery_a
  1951..1980: spriteset_livery_b; // 在 1951 年至 1980 年这个范围内返回 spriteset_livery_a
  default: spriteset_livery_c; // 默认情况下返回 spriteset_livery_c
}

item (FEAT_TRAINS, example_engine){
  property{
    /* 我是红薯地瓜…… */
  }
  graphics {
    default: switch_livery(); // 调用 switch_livery 块来决定机车使用的图像
  }
}
```

又比如说，我想根据当前货物装载比例来显示不同的图像：

```cpp
// 这里的 cargo_count（货物装载量）与 cargo_capacity（车厢货物容量）都是列车特有的变量
// 使用 cargo_capacity 除 cargo_count 会得到一个浮点数，而 NML 对于浮点数的支持极差，
// 因此在这里计算完之后再乘以 100，得到百分比
switch (FEAT_TRAINS, SELF, switch_livery, cargo_count / cargo_capacity * 100) {
  0: spriteset_empty; // 在完全没有货物的时候返回 spriteset_empty
  1..50: spriteset_half_full; // 在装载比例为 1%-50% 的时候返回 spriteset_half_full
  default: spriteset_full; // 默认情况下返回 spriteset_full
}

item (FEAT_TRAINS, example_wagon){
  property{
    /* 我是红薯地瓜…… */
  }
  graphics {
    default: switch_livery(); // 调用 switch_livery 块来决定这列车使用的图像
  }
}
```

这样子做就可以在车厢完全没有任何货物的时候不显示任何货物，在有货物以及满载的时候显示不同的图像，指示货物的装载程度。

当然，这个 Switch 块给除载具（列车、道路载具、船舶、航空器）以外的其他物品用是完全行不通的。
其他物品无法访问 `cargo_count` 与 `cargo_capacity` 这两个变量。在尝试编译的时候 nmlc 也会报错。

#### 寄存器

```{warning}
寄存器属高级功能，一般而言不需要使用。
```

前文所提“Switch 只可以读取变量，无法修改变量”不适用于寄存器。寄存器允许临时存储一个计算好的数值，可以随意修改或者调用。

### 匹配数值

匹配数值是一个表达式，必须在编译时就得出，因此不可以在其中使用变量或寄存器。
可以规定匹配数值的范围，最大值与最小值之间用 `..` 隔开，如 `1..3` 就可以匹配到 1、2、3 三个数。

| 匹配数值                             | 是否可行 | 原因                                                                 |
|--------------------------------------|--------|----------------------------------------------------------------------|
| `date(2025, 01, 15)`                 | 可行     | date() 是一个函数，接受三个参数，返回一个数值，可以在编译时计算得出结果 |
| `1`                                  | 可行     | 1 就是 1，可以在编译时计算得出结果                                    |
| `1..max(114, 514)`                   | 可行     |                                                                      |
| `current_date`                       | 不可行   | 不可以使用变量                                                       |
| `cargo_count / cargo_capacity * 100` | 不可行   | 不可以使用变量                                                       |

### 返回值

返回值与 Swtich 中的匹配表达式类似。返回值也是一个表达式，可以在其中使用变量、之前指定的可选参数、寄存器等。
返回值也可以是 `spriteset`、`spritelayout` 与 `spritegroup`（样例请看[匹配表达式—变量](#变量)小节）。

默认返回值是返回值的一个特例，游戏只会在匹配表达式计算结果不符合任何一个匹配数值的时候返回默认返回值。

返回变量的例子：

```cpp
switch (FEAT_TRAINS, SELF, switch_livery, current_year) {
  0..1950: 0; // 在 0 年与 1950 年之间返回 1
  default: current_year % 4; // 在 1950 年之后返回当前年份模 4 的结果
}
```

[^features]: 截至 2025 年 1 月 15 日。更详细的特性列表可以参阅 <https://newgrf-specs.tt-wiki.net/wiki/Action0#Feature>
