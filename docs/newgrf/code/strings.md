# 文本（String）

```{note}
这里主要是对 LNG 语言文件的介绍。OpenTTD 游戏本体（与改版）也使用相同的语言文件和格式。
```

```{caution}
YAGL 使用不同的语言格式，一些关键字与 LNG 语言文件有所出入。如要了解，请查看下方的章节
```

LNG 语言文件遵循一套简单明了的格式。其格式如下：

```none
##grflangid 0x01                # 语言代码（简体中文为 0x56）
##plural 0                      # 复数形式（中文可省略）
##gender 0                      # 性别（中文可省略）

STR_STRING_0        :字符串一    # 定义字符串
str_string_1        :字符串二    # 也可以使用小写
```

我们建议在给字符串命名的时候遵循统一的格式，最好将所有字符串以`STR`开头以避免常量冲突。\
关键字也可以取不同的前缀，如 JP+ Shinkansen 和 JP+ Major Private Companies 就采用了`LV`这个前缀代表用于表示涂装的字符串。

## 编写语言文本：正确使用 LNG 文件

LNG 文件易于使用。在使用 NML 编写 GRF 的时候，在默认情况下，NML 会从 根目录下的`lang`文件夹中读取所有的文本。一般而言，英语是默认文本。如果缺少`english.lng`文件则 nmlc 会报错。
一般而言，必须要在编写好`english.lng`之后，再编写其他语言文件（包括中文）。

## custom_tags.txt：LNG 的宏

你可以使用`custom_tags.txt`来为文本文件创建“宏”，就像这样：

```bash
# custom_tags.txt
# 我们可以在这里定义一些常用的东西，比如 GRF 名称和版本号
VERSION :1.14.514
DATE    :2023/02/31
URL     :https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

而在 LNG 文件里面，就可以这样使用

```bash
##grflangid 0x56

STR_GRF_NAME    :示例 GRF {VERSION}
STR_GRF_DESC    :示例 GRF {VERSION}，写于 {DATE}
STR_GRF_URL     :{URL}
```

采用`custom_tags.txt`管理这些标签，有助于时刻保持语言文件更新并且可以节省劳力。经过 NMLC 处理后，以上文本就会变成：

```bash
##grflangid 0x56

STR_GRF_NAME    :示例 GRF 1.14.514
STR_GRF_DESC    :示例 GRF 1.14.514，写于 2023/02/31
STR_GRF_URL     :https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

>[!IMPORTANT]
> nmlc 无法正确处理`custom_tags.txt`中包含的语言关键字。如，你如果定义了`COLOUR:{WHITE}`则在最终的文本里会原模原样地输入，而不会将你
> 的文本变成白色。

## 其他事项

在编写语言文件的时候，由于作者不可能同时精通多门语言（你给我找一个精通八国语言的过来），因此和翻译者维持良好的关系非常重要。

## LNG 语言文件使用的关键字

| 关键字      | 作用                                                               |
|-------------|------------------------------------------------------------------|
| （空）        | 写做`{}`，用来新建一行。                                             |
| NBSP        | Non-breaking space，即“不换行空格”。                                 |
| {           | 一个左大括号，写做`{{}`                                             |
| COPYRIGHT   | 版权标志（©）                                                        |
| TRAIN       | 火车标志                                                           |
| LORRY       | 卡车标志                                                           |
| BUS         | 巴士标志                                                           |
| PLANE       | 飞机标志                                                           |
| SHIP        | 轮船标志                                                           |
| TINYFONT    | 转换为小字体                                                       |
| BIGFONT     | 转换为大字体                                                       |
| BLUE        | 转换为蓝色文本                                                     |
| SILVER      | 转换为银色文本                                                     |
| GOLD        | 转换为金色文本                                                     |
| RED         | 转换为红色文本                                                     |
| PURPLE      | 转换为紫色文本                                                     |
| LTBROWN     | 转换为淡棕色文本                                                   |
| ORANGE      | 转换为橙色文本                                                     |
| GREEN       | 转换为绿色文本                                                     |
| YELLOW      | 转换为黄色文本                                                     |
| DKGREEN     | 转换为深绿色文本                                                   |
| CREAM       | 转换为奶油色文本                                                   |
| BROWN       | 转换为棕色文本                                                     |
| WHITE       | 转换为白色文本                                                     |
| LTBLUE      | 转换为淡蓝色文本                                                   |
| GRAY        | 转换为灰色文本                                                     |
| DKBLUE      | 转换为深蓝色文本                                                   |
| BLACK       | 转换为黑色文本                                                     |
| PUSH_COLOUR | 自 OpenTTD 1.10 之后可用，TTDPatch 不可用。将当前颜色推入颜色栈中。   |
| POP_COLOUR  | 自 OpenTTD 1.10 之后可用，TTDPatch 不可用。将当前颜色自颜色栈中移除。 |

## YAGL 使用的关键字

基本字符串关键字：

| 编号 | 参数数目 | 名称         | 简介                                                                    |
|------|----------|--------------|-------------------------------------------------------------------------|
| 0x01 | 01       | x-off        | X offset in next byte of string (variable space)                        |
| 0x0D | 00       | new-line     | 换行                                                                    |
| 0x0E | 00       | small-font   | 切换为小号字体                                                          |
| 0x0F | 00       | large-font   | 切换为大号字体                                                          |
| 0x1F | 02       | xy-offs      | X and Y offsets in next two bytes of string                             |
| 0x22 | 00       | dq           | Double quote                                                            |
| 0x7B | 00       | sd           | Print signed dword                                                      |
| 0x7C | 00       | sw           | Print signed word                                                       |
| 0x7D | 00       | sb           | Print signed byte                                                       |
| 0x7E | 00       | uw           | Print unsigned word                                                     |
| 0x7F | 00       | sd-currency  | Print dword in currency units                                           |
| 0x80 | 00       | substring1   | Print substring (text ID from stack)                                    |
| 0x81 | 02       | substring2   | Print substring (text ID in next 2 bytes of string)                     |
| 0x82 | 00       | d-m-year     | Print date (day, month, year) (based on year 1920)                      |
| 0x83 | 00       | m-year       | Print short date (month and year) (based on year 1920)                  |
| 0x84 | 00       | sw-speed     | Print signed word in speed units                                        |
| 0x85 | 00       | discard      | Discard next word from stack                                            |
| 0x86 | 00       | rotate       | Rotate down top 4 words on stack                                        |
| 0x87 | 00       | sw-litres    | Print signed word in litres                                             |
| 0x88 | 00       | blue         | 蓝色                                                                    |
| 0x89 | 00       | lt-gray      | 淡灰色                                                                  |
| 0x8A | 00       | gold         | 金色（淡橙色）                                                            |
| 0x8B | 00       | red          | 红色                                                                    |
| 0x8C | 00       | purple       | 紫色                                                                    |
| 0x8D | 00       | gray-green   | 绿灰色                                                                  |
| 0x8E | 00       | orange       | 橙色                                                                    |
| 0x8F | 00       | green        | 绿色                                                                    |
| 0x90 | 00       | yellow       | 黄色                                                                    |
| 0x91 | 00       | lt-green     | 淡绿色                                                                  |
| 0x92 | 00       | red-brown    | 红棕色                                                                  |
| 0x93 | 00       | brown        | 棕色                                                                    |
| 0x94 | 00       | white        | 白色                                                                    |
| 0x95 | 00       | lt-blue      | 淡蓝色                                                                  |
| 0x96 | 00       | dk-gray      | 深灰色                                                                  |
| 0x97 | 00       | mauve        | 紫灰色                                                                  |
| 0x98 | 00       | black        | 黑色                                                                    |
| 0x99 | 01       | switch-cc    | 转换为 company colour that follows in next byte (enabled by enhancegui) |
| 0x9A | 00       | ext          | Prefix for extended format code, eg. {ext uw-tonnes}                    |
| 0x9E | 00       | euro         | Euro character                                                          |
| 0x9F | 00       | Y-umlaut     | Capital Y umlaut                                                        |
| 0xA0 | 00       | scroll-up    | Scroll button up                                                        |
| 0xAA | 00       | scroll-down  | Scroll button down                                                      |
| 0xAC | 00       | tick         | Tick mark                                                               |
| 0xAD | 00       | x            | X mark                                                                  |
| 0xAF | 00       | scroll-right | Scroll button right                                                     |
| 0xB4 | 00       | train        | Train symbol                                                            |
| 0xB5 | 00       | truck        | Truck symbol                                                            |
| 0xB6 | 00       | bus          | Bus symbol                                                              |
| 0xB7 | 00       | plane        | Plane symbol                                                            |
| 0xB8 | 00       | ship         | Ship symbol                                                             |
| 0xB9 | 00       | super-1      | Superscript -1                                                          |
| 0xBC | 00       | small-up     | Small scroll button up                                                  |
| 0xBD | 00       | small-down   | Small scroll button down                                                |

拓展字符串关键字：

| 编号 | 参数数目 | 名称           | 简介                                                                                            |
|------|----------|----------------|-------------------------------------------------------------------------------------------------|
| 0x00 | 00       | 64-currency0   | Display 64-bit value from stack in currency units                                               |
| 0x01 | 00       | 64-currency1   | Display 64-bit value from stack in currency units                                               |
| 0x02 | 00       | ignore-colour  | Ignore next colour byte. Multiple instances will skip multiple colour bytes.                    |
| 0x03 | 02       | push-w         | WORD Push WORD onto the 文本 ref stack                                                          |
| 0x04 | 01       | unprint-b      | BYTE Un-print the previous BYTE characters.                                                     |
| 0x05 | 00       | internal5      | For internal use only. Not valid in GRF files.                                                  |
| 0x06 | 00       | b-hex          | Print byte in hex                                                                               |
| 0x07 | 00       | w-hex          | Print word in hex                                                                               |
| 0x08 | 00       | d-hex          | Print dword in hex                                                                              |
| 0x09 | 00       | internal9      | For internal use only. Usage in NewGRFs will most likely crash TTDPatch.                        |
| 0x0A | 00       | internalA      | For internal use only. Usage in NewGRFs will most likely crash TTDPatch.                        |
| 0x0B | 00       | 64-hex         | Print 64-bit value in hex                                                                       |
| 0x0C | 00       | station        | Print name of station with id in next 文本 refstack word                                        |
| 0x0D | 00       | uw-tonnes      | Print unsigned word in tonnes                                                                   |
| 0x0E | 01       | gender         | Set gender of string, NewGRF internal ID in next byte. Must be first in a string.               |
| 0x0F | 01       | case           | Select case for next substring, NewGRF internal ID in next byte                                 |
| 0x10 | 01       | list-value     | Begin choice list value, NewGRF internal ID in next byte                                        |
| 0x11 | 00       | list-default   | Begin choice list default                                                                       |
| 0x12 | 00       | end-list       | End choice list                                                                                 |
| 0x13 | 01       | gender-list    | Begin gender choice list, stack offset of substring to get gender from in next byte             |
| 0x14 | 00       | case-list      | Begin case choice list                                                                          |
| 0x15 | 01       | plural-list    | Begin plural choice list, stack offset of value to get plural for in next byte                  |
| 0x16 | 00       | dw-date        | Print dword as date (day, month, year) (based on year 0)                                        |
| 0x17 | 00       | dw-short-date  | Print dword as short date (month and year) (based on year 0)                                    |
| 0x18 | 00       | uw-hp          | Print unsigned word in horse power                                                              |
| 0x19 | 00       | uw-volume      | Print unsigned word as short volume                                                             |
| 0x1A | 00       | uw-weight      | Print unsigned word as short weight                                                             |
| 0x1B | 00       | dw-cargo-long  | Use two words to print an amount of cargo (long form: '10 bags of mail').                       |
| 0x1C | 00       | dw-cargo-short | Use two words to print an amount of cargo (short form: '10 bags').                              |
| 0x1D | 00       | dw-cargo-tiny  | Use two words to print an amount of cargo (tiny form: '10').                                    |
| 0x1E | 00       | uw-cargo-type  | Print unsigned word as name of a cargo type.                                                    |
| 0x1F | 00       | push-colour    | Push current colour onto colour stack. Use this if you need to switch colour and restore later. |
| 0x20 | 00       | pop-colour     | Pop last colour from colour stack. Use this to restore previous colour.                         |
| 0x21 | 00       | uw-force-value | Print unsigned dword from stack as force.                                                       |

使用关键字的样例：

```text
    name: "Ridiculous Town Names {ext push-colour}{blue}1.2.3{ext pop-colour}";
```

## 语言代码

| ID     | 语言                     | 语法格 | 性别形式 | 复数形式 |
|--------|--------------------------|--------|----------|----------|
| 0C     | Chinese  (Traditional)   |        |          | 1        |
| **56** | **Chinese (Simplified)** |        |          | **1**    |

| ID | language               | cases                                 | genders                   | plural form |
|----|------------------------|---------------------------------------|---------------------------|-------------|
| 00 | English (US)           |                                       |                           |             |
| 01 | English (GB)           |                                       |                           |             |
| 02 | German                 |                                       | m w n p                   |             |
| 03 | French                 |                                       | m m2 f                    | 2           |
| 04 | Spanish                |                                       | m f                       |             |
| 05 | Esperanto              |                                       |                           | n           |
| 06 | Ido                    |                                       |                           |             |
| 07 | Russian                | m f n p nom gen dat acc abl pre       | m f n p                   | 6           |
| 08 | Irish                  |                                       |                           | 4           |
| 09 | Maltese                |                                       |                           | 12          |
| 0A | Tamil                  |                                       |                           |             |
| 0B | Chuvash                |                                       |                           |             |
| 0C | Chinese  (Traditional) |                                       |                           | 1           |
| 0D | Serbian                | nom big gen dat aku vok lok ins       | muški ženski srednji      | 6           |
| 0E | Norwegian (Nynorsk)    | small                                 | masculine feminine neuter |             |
| 0F | Welsh                  |                                       |                           |             |
| 10 | Belarusian             | m f n p nom gen dat acc abl pre       | m f n p                   | 6           |
| 11 | Marathi                |                                       |                           |             |
| 12 | Faroese                |                                       | m f n                     |             |
| 13 | Scottish Gaelic        | dat gen nom voc                       | m f                       | 13          |
| 14 | Arabic   (Egypt)       |                                       |                           | 1           |
| 15 | Czech                  | nom gen dat acc voc loc ins big small | m f n map mnp fp np       | 10          |
| 16 | Slovak                 | g                                     | m z s                     | 10          |
| 17 | Hindi                  |                                       |                           |             |
| 18 | Bulgarian              | m f n p                               | m f n p                   |             |
| 1B | Afrikaans              |                                       | male                      |             |
| 1E | Greek                  | subs date geniki                      | m f n                     | 2           |
| 1F | Dutch                  |                                       |                           |             |
| 21 | Basque                 |                                       |                           |             |
| 22 | Catalan                |                                       | Masculin Femenin          |             |
| 23 | Luxembourgish          |                                       |                           |             |
| 24 | Hungarian              | t ba                                  |                           | 2           |
| 26 | Macedonian             |                                       |                           |             |
| 27 | Italian                | ms mp fs fp                           | m ma f                    |             |
| 28 | Romanian               |                                       |                           |             |
| 29 | Icelandic              |                                       | karlkyn kvenkyn hvorugkyn |             |
| 2A | Latvian                | kas                                   | m f                       | 3           |
| 2B | Lithuanian             | kas ko kam ka kuo kur kreip           | vyr mot                   | 5           |
| 2C | Slovenian              | r d t                                 |                           | 8           |
| 2D | Danish                 |                                       |                           |             |
| 2E | Swedish                |                                       |                           |             |
| 2F | Norwegian (Bokmal)     | small                                 | masculine feminine neuter |             |
| 30 | Polish                 | d c b n m w                           | m f n                     | 7           |
| 31 | Galician               |                                       | m f n                     |             |
| 32 | Frisian                |                                       |                           |             |
| 33 | Ukrainian              | r d z                                 | m f s mn                  | 6           |
| 34 | Estonian               | g in sü                               |                           |             |
| 35 | Finnish                |                                       |                           |             |
| 36 | Portuguese             |                                       | n m f mp fp               |             |
| 37 | Brazilian Portuguese   |                                       | m f                       | 2           |
| 38 | Croatian               | nom gen dat aku vok lok ins           | male female middle        | 6           |
| 39 | Japanese               |                                       |                           | 1           |
| 3A | Korean                 |                                       | m f                       | 11          |
| 3C | Malay                  |                                       |                           |             |
| 3D | English (AU)           |                                       |                           |             |
| 3E | Turkish                | tamlanan                              |                           | 1           |
| 42 | Thai                   |                                       |                           | 1           |
| 54 | Vietnamese             |                                       |                           | 1           |
| 55 | Mexican Spanish        |                                       | m f                       | 0           |
| 56 | Chinese (Simplified)   |                                       |                           | 1           |
| 5A | Indonesian             |                                       |                           | 1           |
| 5C | Urdu                   |                                       | m f                       |             |
| 61 | Hebrew                 | singular plural gen                   | m f                       |             |
| 62 | Persian                |                                       |                           |             |
| 66 | Latin                  | gen acc abl dat                       | m f n mp fp np            |             |
