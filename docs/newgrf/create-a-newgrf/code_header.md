# 制作身份证

[返回目录](./catalogue.md)\
[返回介绍](./code_introduction.md)

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

对应 Actions:

- [Action0x14](./action_0x14.md)
- [Action0x08](./action_0x08.md)
