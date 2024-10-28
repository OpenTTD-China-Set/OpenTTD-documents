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
