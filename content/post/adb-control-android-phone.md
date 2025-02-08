---
layout: post
title: 使用 adb 操作安卓系统
subtitle: adb 完成 android 备份恢复
author: Direct-A
date: 2022-03-01
toc: true
top: false
cover: false
mathjax: true
categories:
  - 折腾
tags:
  - 安卓
  - adb
  - 数据备份
summary: adb 操作安卓手机来备份还是优点多此一举，但是考虑到只有一台手机还是可以这么搞搞。
password:
description:
---

## 使用 adb 操作安卓系统

adb 全称 Android Debug Bridge，看名字就知道，它设计之初的目的就是用于安卓设备的调试，既然是参与调试，那么它对安卓系统的操作能力也就不一般了，像常用的文件操作，包管理都是基本操作。
所以在电脑上操作安卓手机也就首选 adb 了。

之所以突然想要在电脑上用这种方式来操作手机，也是因为我手机用了大概有四年左右了，最近开始出现各种卡顿，程序无响应，很多时候直接就开始干扰使用了。
所以决心今天进行一次大清扫，同时备份一下数据，方便以后使用。
<!-- more -->

那么我大概的想法就是：
1. adb 把所有重要的程序安装包备份出来
2. 用 adb 把数据复制出来
3. 手机出厂设置
4. adb 把整理好的数据复制回去

那么第一步就是获取 adb

### 获取 adb

archlinux 就很方便，一行命令（感谢 pacman 感谢 AUR）

```shell
sudo pacman -S android-tools
```

windows 就请参考[使用adb免root迁移应用数据 | BDの小窝](https://www.bluesdawn.top/419/#%E8%BF%98%E5%8E%9F%E5%A4%87%E4%BB%BD) [【转载】使用adb免root迁移应用数据 - 凌维三度](https://www.fwder.cn/index.php/archives/74/)

### 使用

既然是调试工具，那首要前提就是手机得开启开发者模式，怎么开启我就不详述了毕竟不同品牌不同操作。
最后开启USB调试，把手机连接到电脑，并且完成手机上USB调试的确认。

完成上面的操作，并安装完adb，在终端就可以使用`adb`命令了。
不知道怎么用就先看看`adb help`。
但既然是备份，也就没必要知道太多别的了。

```shell
# 目前版本已准备弃用buckup了，而且安卓9也不知道为什么不是很好用这条命令
# 同样restore也是
adb backup [-system-nosystem] -all [-apk-noapk] [-shared-noshared] -f <ab包储存位置> <应用包名>
# [-system-nosystem] 是否包含系统应用，默认为-system，一般备份全部应用时才用到
# -all 带有此参数会备份所有应用
# [-apk-noapk] 备份数据的同时是否备份apk，默认为-noapk
# [-shared-noshared] 是否备份设备内置存储或SD卡的内容，比如音乐、图片和视频，默认为-noshared
# -f <ab包储存位置> 选择备份的文件存放在哪里，可根据喜好自行替换
# <应用包名> 备份单个应用需要知道包名

adb restore <ab包储存位置>

# 一句命令全部备份，还原步骤同上
adb backup -apk -shared -all -f <ab包储存位置>

# 不备份系统应用，换新机时可以用
adb backup -apk -nosystem -shared -all -f <ab包储存位置>

# 不备份系统应用和内置存储媒体等内容
adb backup -apk -nosystem -noshared -all -f <ab包储存位置>

# 备份全部用户应用数据，但不备份apk
adb backup -noapk -nosystem -noshared -all -f <ab包储存位置>
```

不知道为什么，adb 提供的备份和还原在我这台魅族上就没法用，虽然可以导出`.ab`的备份文件，但是只有区区30多MB，怎样也没法让人相信这是完整的应用备份文件，所以我选择自己手动进行备份。

```shell
# 获取所有软件包名称
# pm 就是 package manager
# 这里返回的是 package:<包名> 格式，每个一行的标准输出
adb shell pm list package

# 获取包地址
# 返回的是 package:<地址> 格式的每行一个的标准输出
adb shell pm path <包名>

# 复制文件
adb pull <手机内地址> <本机存放地址>
```

结合这些命令的使用我写了个shell脚本：

```bash
touch pkgs_android
adb shell pm list package >pkgs_android

touch pkgs_android_path
for i in $(cat pkgs_android); do
  adb shell pm path $i >>pkgs_android_path
done

for i in $(cat pkgs_android_path); do
  j=${i#*app/}
  echo ${j%%-*==/base*}
  adb pull ${i#*:} ./${j%%-*==/base*}.apk
done
```

通过上面的一系列操作，算是完成了安装包备份，但是自己的文件和图片、音乐那些还是需要自己动手去迁移。
所以还需要使用其他命令。

```shell
ARRAY=("DCIM" "Pictures" "Movies" "Tencent/QQ_images" "Documents" "Download" "Snapseed" "Bluetooth" "Music")
for i in $(seq ${#ARRAY[@]}); do
  adb pull /storage/emulated/0/${ARRAY[$i]}
done
```

这样一来基本就该备份的都备份了。

手机上恢复出厂设置，然后再把数据恢复回去就行了。

```shell
# 向手机复制数据
adb push <电脑> <手机>
```

其实还可以通过adb安装软件包，但是这次恢复出厂本身就在于清理系统软件，也就没这个必要了。

-----

一整套整完，手机焕然一新，再起第二春😋。


## 参考资料

[Android Debug Bridge - ArchWiki](https://wiki.archlinux.org/title/Android_Debug_Bridge) [使用adb免root迁移应用数据 | BDの小窝](https://www.bluesdawn.top/419/#%E8%BF%98%E5%8E%9F%E5%A4%87%E4%BB%BD) [【转载】使用adb免root迁移应用数据 - 凌维三度](https://www.fwder.cn/index.php/archives/74/) 
