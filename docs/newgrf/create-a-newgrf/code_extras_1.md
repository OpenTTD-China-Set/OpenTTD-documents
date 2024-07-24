# 拓展阅读 I

## YAGL、NFO 与 NML

在[代码介绍](./code_introduction.md#基本原理)中有介绍，**GRF 当中的所有内容其实都是图像**，其中包含“真图像”与“伪图像”。

### NFO

NFO 是最原始的 GRF 编写方式。使用NFO编写NewGRF无异于直接编写十六进制代码。

```txt
   63 * 20  06 0A 02 08 08 02 10 0B 02 18 09 02 20 16 02 28 17 02 38 FF
   64 * 136 00 06 01 01 00 0D 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   00 00 00 00 00 00 00 00 09 11 00 00 F6 09 00 00 F8 09 00 00 00 00 00 00 08 11 00 00 F5 09 00 00
   F7 09 00 00 00 00 00 00 31 11 00 00 F6 09 00 00 F8 09 00 00 00 00 00 00 30 11 00 00 F5 09 00 00
   F7 09 00 00 00 00 00 00
```

### YAGL

YAGL 是 UnicycleBloke 开发的 GRF 语言。其本质上与 NFO 无异，但是可读性更优，易于理解。

```cpp
modify_next // Action06
{
    // modification(value, num_bytes, offset, add?);
    modification(parameter[0x0A], 2, 8, false);
    modification(parameter[0x08], 2, 16, false);
    modification(parameter[0x0B], 2, 24, false);
    modification(parameter[0x09], 2, 32, false);
    modification(parameter[0x16], 2, 40, false);
    modification(parameter[0x17], 2, 56, false);
}
properties<Bridges, 0x0000> // Action00
{
    // instance_id: 0x0000
    {
        bridge_layout:
        {
            table<0x00>
            {
                0x00000000 0x00000000 0x00000000 0x00000000 0x00000000 0x00000000 0x00000000 0x00000000
                0x00000000 0x00000000 0x00000000 0x00000000 0x00000000 0x00000000 0x00000000 0x00000000
                0x00001109 0x000009F6 0x000009F8 0x00000000 0x00001108 0x000009F5 0x000009F7 0x00000000
                0x00001131 0x000009F6 0x000009F8 0x00000000 0x00001130 0x000009F5 0x000009F7 0x00000000
            }
        };
    }
}
```

### NML

NML 是一种高级 NewGRF 语言，带有翻译支持。NML 类似于其他任意编程语言，除了某些地方有 OpenTTD 特色限制，并且没有子例程。
NML 带有翻译支持，采用易于翻译者使用的文件格式。翻译并不要求译者自己了解 NML，只需要了解翻译格式就可以。

NML 与 NFO/YAGL 最大的不同点

## 中国包的工作流程

中国包正式启动于 2023 年 7 月 19 日。
