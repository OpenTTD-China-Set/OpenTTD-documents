# Action0x14

Action0x14 常被用来提供额外信息。由于提供的是“额外信息”，因此即使手动去除也不会影响 GRF 的读取等，但是使用体验会大打折扣。\
这里的额外信息包括：

- GRF 版本
- GRF 最小兼容版本
- GRF 名称和介绍的翻译
- GRF 包含的参数数目
- 每个参数的介绍与名称
- 参数介绍与名称的翻译
- 使用的调色盘

```cpp
// 这是一段真实代码
// 来自 JPTracks-weMOD
optional_info                                             // action14 关键字
{
    INFO:                                                 // INFO 块
    {
        NAME: zh_CN, "样例 GRF";                           // GRF 标题翻译
        DESC: zh_CN, "这是一个样例 GRF 的 Action0x14 部分";  // GRF 介绍翻译
        VRSN: [ 0x01 0x00 0x00 0x00 ];                    // GRF 版本
        MINV: [ 0x01 0x00 0x00 0x00 ];                    // GRF 最低兼容版本
        NPAR: [ 0x0B ];                                   // 参数数量
        PALS: [ 0x44 ];                                   // 使用的调色盘
        PARA:                                             // 参数定义
        {
            0x00000000:                                   // 十六进制，下标为 0 的第一个参数
            {
                NAME: default, "Mode";                    // 默认文本
                DESC: default, "Select track mode.";      // 默认文本
                NAME: zh_CN, "轨道模式";                   // 翻译
                DESC: zh_CN, "选择轨道模式。";              // 翻译
                LIMI: [ 0x00 0x00 0x00 0x00 0x04 0x00 0x00 0x00 ];  // 参数数值限制
                DFLT: [ 0x00 0x00 0x00 0x00 ];                      // 参数默认值
                VALU:                                               // 每一项使用的文本
                {
                    0x00000000: default, "Automatic (Japanese/International)";
                    0x00000001: default, "International";
                    0x00000002: default, "German";
                    0x00000003: default, "British";
                    0x00000004: default, "North American";
                    0x00000000: zh_CN, "自动 (日本/国际)";
                    0x00000001: zh_CN, "国际";
                    0x00000002: zh_CN, "德国";
                    0x00000003: zh_CN, "英国";
                    0x00000004: zh_CN, "北美";
                }
            }
            0x00000002:
            {
                NAME: default, "Finescale tracks";
                DESC: default, "Use narrower track sprites.";
                NAME: zh_CN, "更窄轨道图形";
                DESC: zh_CN, "启用后将使用更窄的轨道图形。";
                TYPE: [ 0x01 ];                           // 参数种类
                LIMI: [ 0x00 0x00 0x00 0x00 0x01 0x00 0x00 0x00 ];
                DFLT: [ 0x01 0x00 0x00 0x00 ];
            }
        }
    }
}
```

Action0x14 当中定义的参数可以被其他的 Actions 使用。如 Action0x0D。
