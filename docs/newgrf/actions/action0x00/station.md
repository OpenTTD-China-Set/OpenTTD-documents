# 车站

| 序号 | 大小 | 版本 | 描述                               |
|------|------|------|------------------------------------|
| 08   | D    | 0.6  | 类别 ID                            |
| 09   | V    | 0.6  | 图像布局                           |
| 0A   | B/B* | 0.6  | 复制图像布局                       |
| 0B   | B    | 0.6  | 回调标志                           |
| 0C   | B    | 0.6  | 禁用站台数量掩码                   |
| 0D   | B    | 0.6  | 禁用站台长度掩码                   |
| 0E   | V    | 0.6  | 自定义布局                         |
| 0F   | B/B* | 0.6  | 从参数给定的车站 ID 复制自定义布局 |
| 10   | W    | 0.6  | 车站货物少量/大量阈值              |
| 11   | B    | 0.6  | 接触网杆设置                       |
| 12   | D    | 0.6  | 触发随机化的货物类别               |
| 13   | B    | 0.6  | 一般标志                           |
| 14   | B    | 0.6  | 接触网设置                         |
| 15   | B    | 0.6  | 列车是否可以通过车站格             |
| 16   | W    | 0.7  | 动画信息                           |
| 17   | B    | 0.7  | 动画速度                           |
| 18   | W    | 0.7  | 动画触发条件                       |
| 1A   | V    | 1.2  | 高级图像布局（带临时变量）         |
| 1B   |      |      | 预留                               |
| 1C   | W    | 14   | 车站名称指针                       |
| 1D   | W    | 14   | 类别名称指针                       |
| 1E   | V    | 15   | 车站图像布局标识                   |

## 车站类别（08）

新定义的车站物品需要划分到一个类别中。
类别采用 8 位标签。

| 模式 | ID          | 用途                                               | 备注                 |
|------|-------------|----------------------------------------------------|----------------------|
| DFLT | 44 46 4C 54 | 默认车站类型                                       |                      |
| WAYP | 57 41 59 50 | 路点，不接受乘客或货物，也不允许货物装卸、旅客乘降 |                      |
| *xxx | FF XX XX XX | 路点，不接受乘客或货物，也不允许货物装卸、旅客乘降 | 自 OpenTTD 15 起可用 |
| xxxx | XX XX XX XX | 普通车站类别                                       |                      |

自 OpenTTD 15 起，游戏会将所有第一个字节为 FF 的车站类别视为路点类别。
使用这些类别定义的车站将出现在路点建造窗口中，而不是车站建造窗口中。

## 车站名称（1C）

OpenTTD 14 提供了车站属性 1C，允许用新方式指定车站名称。
在 OTTD 14 以前，车站名称是使用特定的 Action0x04 编号实现的（0xC500—0xC5FF）。

1C 的数值是一个指向 Action0x04 的指针。这个 Action0x04 当中的文本将作为车站名称使用。
此处指定的 Action0x04 编号必须在 0xDC00—0xFFFF 区间内。

## 类别名称（1D）

1D 与 1C 极其相似。

OpenTTD 14 提供了车站属性 1D，允许用新方式指定类别名称。
在 OTTD 14 以前，车站名称是使用特定的 Action0x04 编号实现的（0xC400—0xC4FF）。

1D 的数值是一个指向 Action0x04 的指针。这个 Action0x04 当中的文本将作为类别名称使用。
此处指定的 Action0x04 编号必须在 0xDC00—0xFFFF 区间内。

### 样例

```cpp
strings<Stations, default, 0xDC00> // Action04
{
    /* 0xDC00 */ "My station class";
    /* 0xDC01 */ "My station name";
}

properties<Stations, 0x0001> // Action00
{
    {
        station_name_id:          0xDC01; // 1C
        class_name_id:            0xDC00; // 1D
    }
}
```

<script src="https://giscus.app/client.js"
        data-repo="openttd-china-set/openttd-documents"
        data-repo-id="R_kgDOLV0ztQ"
        data-category="Announcements"
        data-category-id="DIC_kwDOLV0ztc4Cf-oT"
        data-mapping="pathname"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="bottom"
        data-theme="preferred_color_scheme"
        data-lang="zh-CN"
        crossorigin="anonymous"
        async>
</script>
