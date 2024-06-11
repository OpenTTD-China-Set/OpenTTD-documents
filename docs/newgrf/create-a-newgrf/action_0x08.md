# Action0x08 GRF 基本信息

[返回目录](./catalogue.md)\
[返回介绍](./actions_introduction.md)

Action0x08 当中定义了 GRF 的识别符、GRF 使用的标准的版本、GRF 名称与介绍。其中，名称与介绍部分已经被 Action0x14 部分替代，但仍建议不要盲目去除。

```cpp
// 这是一段真实代码
grf                                           // Action08 关键字
{
    grf_id: "DP0\x01";                        // GRF ID（GRF 识别符）
    version: GRF8;                            // GRF 所使用的标准之版本，如 GRF7、GRF8
    name: "Japan Set3: Tracks ...";           // GRF 名称
    description: "Japan Set3: Tracks ...";    // GRF 介绍
}
```

## 附录 I: GRF 标准

| 版本 | 兼容性     | TTDPatch 对应版本                                   | OpenTTD 兼容性          |
|------|------------|-----------------------------------------------------|-------------------------|
| GRF8 | GRF2..GRF8 | 不支持                                              | OpenTTD 1.2 (r23159)1.2 |
| GRF7 | GRF2..GRF7 | 2.5 beta 1 或更高                                   | OpenTTD 0.6             |
| GRF6 | GRF2..GRF6 | 2.0.1 alpha 13 或更高                               | OpenTTD 0.6             |
| GRF5 | GRF2..GRF5 | 2.0r1 Stable TTDPatch + TTDPatch 2.0.1 alphas 至 12 | OpenTTD 0.6             |
| GRF4 | GRF2..GRF4 | 2.0 Stable TTDPatch                                 | OpenTTD 0.6             |
| GRF1 | GRF0..GRF1 | 1.9.1 alpha 28 或更高                               | 不支持                  |
| GRF0 | GRF0       | 1.9.1 alphas 至 27                                  | 不支持                  |

请不要使用 GRF0 与 GRF1，并尽可能使用 GRF8。GRF8 是最新的 GRF 技术标准。除非需要支持 TTDPatch，否则请不要使用其他版本。

另行参阅：

- [Action0x14 额外信息（仅 OpenTTD）](./action_0x14.md)
