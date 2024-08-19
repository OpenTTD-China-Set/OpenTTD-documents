# 图像

图像是玩家直接看到的部分，是 GRF 的核心，因此保证图像绘制美观正确是制作 GRF 的首要任务。

在 GRF 中，除了有 pseudosprite 之外，还有 realsprite 与 recoloursprite。Realsprite 是“真正看到的图像”，而 Recoloursprite 则是一系列颜色索引，用来指代重新着色的对象与目标。

## Realsprite

GRF 的图像有两个技术指标，分别是 bpp（每像素比特数）与 EZ（高清）。

bpp 越高，可用的颜色就越丰富。8bpp 代表每像素 8 比特，即一共有 $2^{8} = 256$ 种可用颜色；32bpp 代表每像素 32 比特，即一共有 $2^{32} = 4,294,967,296$ 种可用颜色（RGBA 模式，包括透明度）。

EZ 则有 Normal（普通）、2 倍和 4 倍之分。2 倍是将一个像素缩小到原来的四分之一，即 1/(2×2)；4 倍是将一个像素缩小到原先的十六分之一，即 1/(4×4)。玩家对颜色通常不敏感，因此主要考虑的技术指标是 EZ 与否。为了与游戏美术风格拟合，我们推荐绘制 8bpp Normal EZ 的图像。

使用 8bpp 的时候还须注意调色盘问题。原 TTD（运输大亨豪华版）有 DOS 与 Windows 两个版本，两个平台所支持的色彩不同，在 Windows 平台下需要分配一定的调色盘空间给系统 API 使用，因此 Windows 调色盘相较于 DOS 调色盘所支持的颜色要少。OpenTTD 作为 TTD 的继承者自然是两种调色盘都支持。我们推荐在绘制 8bpp 图像的时候使用 DOS 调色盘，原因如前文所说，DOS 调色盘支持的颜色更多。

总结如下：

| 技术        | 难易度 | 效果         | 备注                     |
|-------------|--------|--------------|--------------------------|
| 颜色        |        |              |                          |
| 8bpp        | ★      | 类似原版画风 | 有可能会遇到色盘编译问题 |
| 32bpp       | ★★     | 更加灵活     | 需要编写额外代码         |
| 缩放        |        |              |                          |
| Normal Zoom | ★      | 类似原版画风 |                          |
| 2x          | ★★★★   | 两者之间     | 需要编写额外代码         |
| 4x          | ★★★★★  | 高清画风     | 需要编写额外代码         |

通常而言，使用 2x 或 4x 的话会同时使用 32bpp。

## 重着色图像（Recoloursprite）

在 NewGRF 当中新定义的重着色图像固定为 $8*256=2048$ 字节，即约 2kiB 的大小。如前文所述，重着色图像是一系列颜色索引，用来指代重新着色的对象与目标，所以“制作”重着色图像不需要绘图。
以下是一种在 NML 当中定义重着色图像的方式：

```cpp
spriteset(my_recoloursprite){
    recolour_sprite {
        0x01: 0x01;
        2: 3;
        3..0x05: 6;
        0x06..10: 0x07..11
    }
}

```

重着色图像可以用于节省图像数量与大小，在需要一些极其相似但是又有细微差别——如颜色——的图像时大有帮助，如不同颜色的矿物，黑色是煤炭，而棕色是铁矿石，绿色是铜矿石，等等。