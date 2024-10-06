# 调色盘

调色盘是 OpenTTD 图像当中一个至关重要的概念。
如果没有选择正确的调色盘，
轻则图像显示错误[^act14]，重则无法编译。

NewGRF 的调色盘主要分为三种：

* 8bpp Windows
* 8bpp DOS
* 32bpp（真彩色）

8bpp 即为“每像素 8 比特”，“32bpp”即为“每像素 32 比特”。
每像素比特数越大，可以记录的颜色就越多。
但在 OpenTTD 中，8bpp 有其独特的作用，
因此除非需要制作真实画风 NewGRF，
或需要如重着色（如公司颜色）等特性时，
尽量使用 8bpp 调色盘。

[^act14]: 对于未设置 Action0x14 调色盘额外信息的老旧 GRF 尤其如此。

## 8bpp

在 OpenTTD 中有两种类型的 8bpp 调色盘，
分别是“Windows”调色盘与“DOS”调色盘。
两者理论上都可以使用 256 种颜色，
但 Windows 调色盘需要留出部分颜色索引供系统 API 使用，
因此实际可用颜色较 DOS 调色盘少。

Under construction

## 32bpp

Under construction

## 蒙版

Under construction

## 转换调色盘

Under construction