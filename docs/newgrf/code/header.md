# 识别块（GRF Identifier）

如前文所说，OpenTTD 在读取 GRF 的时候会读取 GRF 识别符，即 ID。ID 与其他项目必须放在 NewGRF 代码的最前面。grf 块包含了这些项目。

```cpp
grf {
    grfid: "\00\00\00\00";                      // grf ID
    name: string(STR_GRF_NAME);                 // grf 名称
    desc: string(STR_GRF_DESC);                 // grf 介绍
    version: 0;                                 // grf 版本
    min_compatible_version: 0;                  // grf 最小兼容版本
    param 0 {                                   // 自定义参数
        my_param {                              // 参数名称
            type: int;                          // 参数种类
            name: string(STR_PARAM_0_NAME);     // 参数显示名称
            desc: string(STR_PARAM_0_DESC);     // 显示介绍
            min_value: 0;                       // 最小值
            max_value: 3;                       // 最大值
            def_value: 1;                       // 默认值
            names: {                            // 每一项的自定义名称
                0: string(STR_PARAM_0_OPTION_0);
                1: string(STR_PARAM_0_OPTION_1);
                2: string(STR_PARAM_0_OPTION_2);
                3: string(STR_PARAM_0_OPTION_3);
            };
        }
    }
}
```

## GRFID 注意事项

GRFID 可以是一个字符串，也可以是一个整数。可以在字符串中插入十六进制数。

使用字符串作为 GRFID 时，字符串必须用双引号括起来，且只能包含 ASCII 字符或以`\`开头的十六进制数。

| ID                        | 是否正确 | 原因                      |
|---------------------------|--------|---------------------------|
| `grf_id: "ABCD";`         | 正确     |                           |
| `grf_id: "baka";`         | 正确     |                           |
| `grf_id: "0000";`         | 正确     |                           |
| `grf_id: "ba\11\45";`     | 正确     |                           |
| `grf_id: "\11\45\14\19";` | 正确     |                           |
| `grf_id: "....";`         | 正确     |                           |
| `grf_id: "ABCD";`         | 正确     |                           |
| `grf_id: "____";`         | 正确     |                           |
| `grf_id: "ABCDE";`        | 错误     | 长度不正确（预期：4，实际：5） |
| `grf_id: "00\00";`        | 错误     | 长度不正确（预期：4，实际：3） |
| `grf_id: "琪露诺";`       | 错误     | 不可以使用非 ASCII 字符   |

| GRFID                      | 用途                                                  |
|----------------------------|-------------------------------------------------------|
| 00 00 00 00                | 保留（用于指示“不是 NewGRF”，如原版工业等）              |
| 00 00 00 01 .. FE FF FF FF | 普通 NewGRF                                           |
| FF 00 00 00 .. FF FF FF FF | 保留                                                  |
| FF "OT" 00 .. FF "OT" FF   | 额外基本图形 GRF                                      |
| FF "OT" 01                 | OpenGFX                                               |
| FF "OT" 11                 | NoGFX                                                 |
| FF "OTD"                   | OpenTTD 额外基本图形：openttdd.grf (OpenTTD 0.6 - 1.0) |
| FF "OTN"                   | NightGFX                                              |
| FF "OTT"                   | OpenTTD 额外基本图形：openttd.grf (OpenTTD >= 1.1)     |
| FF "OTW"                   | OpenTTD 额外基本图形：openttdw.grf (OpenTTD 0.6 - 1.0) |
| FF "OTz"                   | zBase                                                 |
| FF FF FF FF                | TTDPatch 额外基本图形                                 |
| FF .. .. ..                | 所有以“FF”开头的 GRFID 为系统保留 ID                  |

一共有 $256^4=4294967296$ 个可用的 GRF ID。
