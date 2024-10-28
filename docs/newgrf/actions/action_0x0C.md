# Action0x0C 注释

在 YAGL 中，注释是`ignore`块。该块当中的所有内容都会被 OpenTTD 忽略，但是仍然会存在于 GRF 中。

```{note}
`ignore`块中的内容会被写入到 GRF 中，而以`//`/`/*`/`#`开头的 CPP/C/Bash 风格注释则会被编译器忽略。
```

## 样例

```cpp

ignore
{
    "OpenTTD 不读取我，哈哈哈哈


    还可以多行注释
    一定不要忘记最后有分号！
    ";
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
