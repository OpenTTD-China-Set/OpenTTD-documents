# Action

GRF 是由“sprite”，即“图像”组成的，图像当中包括“伪图像”（pseudosprite）与“真图像”（realsprite）。
“伪图像”就是一般意义上的 NFO/YAGL 代码，
而“真图像”就是一般意义上的图像。
以下简称伪图像为“代码”。

Action 是代码的基本单元，
若要使用 grf-py、YAGL 或 NFO 编写 NewGRF 则必须了解 Action。[^nml]
NewGRF 可以包含 20 种 Action，
（0x00—0x14）
每种 Action 都有不同的作用。

```{mermaid}
flowchart TD
  subgraph 间接操纵
  NML
  end
  NML -->|聚合|Action
  Action -->|构成|NewGRF
  subgraph 直接操纵
  grf-py -->|聚合|Action
  yagl -->|呈现|Action
  NFO -->|呈现|Action
  end
  OpenTTD -->|"读取、加载"|NewGRF
```

[^nml]: NML 采用不同的代码组织方式，
不涉及 Action。

为了讲解简便，本教程中 Action 代码演示统一使用 YAGL 语言。你也可以访问 <https://www.tt-wiki.net> 以查看 NFO 样例[^examples]。

[^examples]: 大部分页面未有样例

```{important}
由于 YAGL 目前尚在开发中，尚有一些程序错误。建议定期更新 YAGL 以避免 GRF 出错。不过 YAGL 有严格的版本限制，因此在更新前请一定要做好代码备份。
```

```{important}
grf-py 目前尚在开发中，API 与特性随时可能变动。建议关注作者动态（<https://github.com/citymania-org/grf-py>）并定期更新。
```
