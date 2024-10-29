# Action0x00 物品特性

Action0x00 可以用来定义新的物品，或是修改现有物品的属性。
物品即为游戏中的载具、车站、物件（Object）等。
每项物品有独特的属性，你可以在子页面找到物品的属性列表与解释。

```{toctree}
:glob:
:titlesonly:

./action0x00/*
```

## 语法

Action0x00 在 yagl 中使用 `properties` 呈现。

```cpp
// 1145 在这里表示任意值
// 此处定义的为车站
properties<Stations, 0x1145> // Action00
{
    // instance_id: 0x1145
    // 具体属性与对应数值
    {
        class_id:                 "1145";
        station_name_id:          0x1145;
        can_train_enter_tile:     0x11;
        pylon_placement:          0x11;
        overhead_wire_placement:  0x11;
        little_lots_threshold:    0x1145;
        general_flags:            0x11;
        cargo_type_triggers:      0x11451145;
    }
}
```
