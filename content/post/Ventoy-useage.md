---
layout: post
title: 全能多系统启动 U 盘制作工具——Ventoy
subtitle: useage of Ventoy
author: Direct-A
date: 2020-07-14
toc: true
top: false
cover: false
mathjax: true
categories:
  - 折腾
tags:
  - ventoy
  - how to
summary:
password:
description:
---

最近重装系统，需要安装双系统，因此需要制作两个启动盘。不巧的是我在装双系统过程中，卡住了，只能成功引导进一个系统，所以我只能重复制作系统盘😖，真是苦了我可怜的 32G U 盘了，来回格式化，做了系统盘还有大半的容量没有用上。

正巧看到[kiteAB](https://www.bilibili.com/video/BV1wz411i7Cg?from=search&seid=4968162955944320486)的视频，讲了这个工具。就找来用用。

<!-- more -->
# 安装

在 Windows 下可以通过 `chocolately` 和 `scoop` 进行安装

``` shell
scoop bucket add extras
scoop install ventoy
choco install ventoy
```
Linux 下可以去[github页面](https://github.com/ventoy/Ventoy/releases)下载。

# 使用

使用起来也是方便，第一次使用的 U 盘，会进行格式化，重新分区，需要注意数据迁移。
建议制作时更改一下分区类型，为了方便使用。（不知道为什么，windows下打开`Ventoy`居然不能正常使用截屏软件🤔）
{% asset_img Snipaste_2020-07-14_18-34-19.png 分区类型 %}

制作完成之后，把系统镜像直接复制进分区，就可以使用了。就是如此方便。
目前[官方网站](https://www.ventoy.net/cn/index.html)称已经测试了 **300\+** 的镜像文件，均可以成功启动。

# 升级

在软件升级之后，可以对 U 盘内的`ventoy`进行升级，此时并**不会**重新格式化并分区，这很就很方便了。

# 总结

`Ventoy`相对于现在各种pe系统盘来说最大的优势就在于：
1. 单盘多启动，并且仅需要复制相应的系统镜像即可。
2. 启动盘升级方便，不需要重新格式化分区，延长 flash 寿命。
3. 开源！！！用的放心。
