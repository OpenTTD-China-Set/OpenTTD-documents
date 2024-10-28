# 翻译

翻译是将文本从一个语言转换为另一种语言的过程。
不管是将中文翻译成英文，还是将英文翻译成中文，翻译的目标都是一致的：
给读者带来准确无误的文本，保证绝大多数人都可以理解。

## 翻译 NewGRF

翻译 NewGRF 的方式取决于 NewGRF 本身是如何编写的。

| 语言                          | 方式                                 |
|-------------------------------|--------------------------------------|
| NML                           | 在 Lang 文件夹当中加入对应的语言文件 |
| grf-py，使用了 string manager | 在 Lang 文件夹当中加入对应的语言文件 |
| grf-py，未使用 string manager | 手动修改代码                         |
| NFO                           | 手动编写 Action4                     |
| YAGL                          | 手动编写 Action4                     |
| M4NFO                         | 手动编写 Action4                     |

这里仅介绍前两种情况下编写翻译的方式。

### 认识 grflangid

```txt
## grflangid 0x01
# plural 0

...
```

上文当中的“grflangid”可以拆分为三个部分：“grf”、“lang”、“id”。其作用是指示语言 ID。
如“英式英语”是 0x01，而“简体中文”就是 0x56。
如果 grflangid 设置错了，玩家就完全无法看到翻译了：翻译跑到其他的语言去了[^language_id]。

[^language_id]: 曾经有一位在 TTDPatch 时代开发中国铁路机车 GRF 的仁兄抄荷兰机车 GRF 的代码抄错了，
忘了把荷兰语的 ID 改成简体中文的 ID，导致把语言切换成荷兰语才可以看到中文。

### 复数形式与格形式

一些语言有复数形式，如在英语中，“train”（火车）的复数形式是“trains”，“property”（属性）的复数形式是“properties”。
中文没有名词的复数形式，在大多数情况下翻译可以忽略使用复数。

### 控制符号

控制符号可以用以控制文本颜色、插入变量、插入另一段文本等。

````{caution}
不正确使用控制符号、盲目使用机翻有很大概率导致输出的文本让人难以理解。
一个反面样例：
```text
原文：
{BLACK}{}Production needs {WHITE}per unit{BLACK} of tobacco:{}* 1 worker{}{}Production {WHITE}per unit{BLACK} of tobacco:{}* 1 unit of cigars

Production needs per unit of tobacco:
* 1 worker
Production per unit of tobacco:
* 1 unit of cigars

==========================================

修正前：
生产需求 {WHITE}每包{BLACK} 烟叶:{}* 1 工人{}{}生产 {WHITE}每包{BLACK} 烟叶:{}* 1 盒雪茄

生产需求 每包 烟叶：
* 1 工人
生产 每包 烟叶：
* 1 盒雪茄

==========================================

修正后：
{WHITE}每单位{BLACK}烟叶生产需求：{}* 1 位工人{}{}{WHITE}每单位{BLACK}烟叶产品：{}* 1 单位雪茄

每单位烟叶生产需求：
* 1 位工人
每单位烟叶产品：
* 1 单位雪茄
```
````

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
