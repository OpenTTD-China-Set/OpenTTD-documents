# 软件

如果要绘制原版画风的图像，可以选用一些像素画软件：

| 名称        | 推荐程度 | 价格 | 备注                |
|-------------|----------|------|---------------------|
| Aseprite    | ★★★      | ¥70  | 学习版众多          |
| LibreSprite | ★★       | 免费 | Aseprite 的开源版本 |
| Paint.Net   | ★        | 免费 | 操作较繁杂          |
| Photoshop   | 不推荐   | 收费 |                     |
| gimp        | 不推荐   | 免费 |                     |

如果要绘制高清图像，普通的像素画软件就不够用了：

| 名称                   | 推荐程度 | 价格 | 备注   |
|------------------------|----------|------|--------|
| Paint.Net              | ★★       | 免费 |        |
| Photoshop              | ★★★      | 收费 |        |
| gimp                   | ★★       | 免费 |        |
| gorender + magicavoxel | /        | 免费 | 三渲二 |
| 其他 3D 建模软件       | /        | /    | 三渲二 |

很大一部分高清图像都是渲染出来的，而不是手绘出来的。\
往后绘图部分的教程都以 Aseprite 为使用的程序。

```powershell
# 可以使用scoop来下载绘图程序！
scoop bucket add extras
# LibreSprite
scoop install extras/libresprite
# pdn
scoop install extras/paint.net
# gimp
scoop install extras/gimp
# gorender + magicavoxel
scoop bucket add openttd-bucket https://github.com/wensimehrp/openttd-bucket
scoop install extras/magicavoxel
scoop install openttd-bucket/gorender
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
