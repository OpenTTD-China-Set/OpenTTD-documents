# Action0x08 GRF 基本信息

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

GRF ID 必须使用英文双引号括起来，且只能包含 ASCII 字符或以`\x`开头的十六进制数。

| ID   | 是否正确                      | 原因                      |
|------|-------------------------------|---------------------------|
| 正确 | `grf_id: "ABCD";`             |                           |
| 正确 | `grf_id: "baka";`             |                           |
| 正确 | `grf_id: "0000";`             |                           |
| 正确 | `grf_id: "ba\x11\x45";`       |                           |
| 正确 | `grf_id: "\x11\x45\x14\x19";` |                           |
| 正确 | `grf_id: "....";`             |                           |
| 正确 | `grf_id: "ABCD";`             |                           |
| 正确 | `grf_id: "____";`             |                           |
| 错误 | `grf_id: "ABCDE";`            | 长度不正确（预期：4，实际：5） |
| 错误 | `grf_id: "00\x00";`           | 长度不正确（预期：4，实际：3） |
| 错误 | `grf_id: "琪露诺";`           | 不可以使用非 ASCII 字符   |

## GRF 标准

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
