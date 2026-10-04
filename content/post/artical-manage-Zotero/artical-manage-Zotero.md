---
layout: post
title: 全能又开源的文献管理软件——Zotero
subtitle: Zotero, the best RIS manager
author: Direct-A
date: 2020-06-16
toc: true
top: false
cover: false
mathjax: true
categories:
  - lab
tags:
  - zotero
  - RIS manager
  - how to
summary:
password:
description:
---

# 为什么迁移到 Zotero

其实最开始我是使用 Endnote 的，在刚开始使用 Endnote 的时候我就因为它古怪的逻辑，而使用困难。它的使用逻辑与以往使用软件不同，用起来就很别扭。
不过好在有重庆大学万震老师的[《手把手教你使用EndNote X9》](https://github.com/wanzhenchn/EndNote_Tutorial_Hand_by_Hand)，以及网络上中多的相关教程，学起来并不难。但是就算是学会了 Endnote 的使用，它在使用的过程中，很多操作仍然让人感觉受限制，用的并不自由。
最大的缺陷就是，Endnote 真的就只是收纳文献，并把文献分类归档，方便查看和引用。多个库的管理思维，使得查阅文献有时还需要少量的翻找。窗口套窗口的软件界面，在多个库同时打开时一不小心就给整的一两个窗口挪不动了，虽然可以用重新自动排列窗口来解决。不直接显示笔记区域，在真正对文献进行阅读和归纳时显得异常的麻烦，并不能快捷的把对文献的想法自由的记录下来，当然你可以用其他的软件配合使用，但是两个软件之间如何做到交互就成了问题。作为一个文献管理软件，在文献管理时不能够很好的在多平台多终端之间款快速便捷的切换，也是一大痛点。
<!-- more -->
因此我也尝试着去寻找一些其他的文献管理软件，但是并不理想，很多功能都不及 Endnote。当然国内的 NoteExpress 也并不差，但是它插入文献的功能不够完善。
另外，最近的美国封锁软件的事情（哈工大Matlab），也让我决定把工具链换成更加开源的会更可靠。
碰巧又一次看到 bilibili 上 Straggle with me 制作的关于 Zotero 的视频，还是一整套教程。仔细查看之后发现，完全击中了 Endnote 的许多使用痛点，并且团队协作这点简直棒。干脆迁移至 Zotero。

{% asset_img "Snipaste_2020-06-16_10-37-20.png" Zotero %}

## Zotero 的优点：
* 更加高效，文献管理很多操作都是程序化的，几个脚本就可以自动解决的问题，Endnot 里却仍然需要手动操作
* 信息展示较 Endnote 更加合理，不是窗口套窗口，更不是多个库的管理思想。
* 文献信息云端同步，多终端，多平台支持
* 软件开源，不需要授权，github可以提issue，软件功能更加亲近使用
* Endnote的功能它一个不缺
* 有 tag 管理系统，自动生成 tag
* 插件扩展，GitHub 方便找
* 文档更加友好，官网就有，多语言支持（含中文！）[官方文档](https://www.zotero.org/support/zh/start)

## 相较 Endnote 的不足：
* 不能直接展示pdf，打开需要软件跳转，但并不是很繁琐，但有时候挺需要的，可以通过添加笔记弥补
不能添加星级，区分文献重要度，不过不是很必要

# 安装和使用
## 安装

Zotero 是一个全平台的软件，可以在 Windows，Linux 和 Mac 上使用。

Windows上可以通过 chocolatey 进行安装，在[安装chocolatey](https://chocolatey.org/install) 后，打 powershell 并输入
``` shell
choco install zotero
```
即可安装

在 Linux 和 Mac 上也有相应的安装方式，可以见[官方文档](https://www.zotero.org/support/installation)

## 使用

安装完成后，开箱即用，但是为了达到更好的使用体验，仍需要根据自身的需要进行相关的设置。

首先可以进行语言设置，在 **Edit -> Preferences -> Advanced -> Language**，中可以更改软件语言，更改后会提示重启软件。
在 **编辑 -> 首选项 -> 同步**，可以登录在官网注册的 Zotero 账户，方便对导入的文件进行云同步。默认情况下 Zotero 官方提供 300M 的免费空间以供使用。

在 工具 -> 插件 中可以打开以添加的浏览器插件和写作引用插件。方便导入文献以及文献引用。

### Zotero + ZotFile + OneDrive

由于 Zotero 是开源软件，更具包容性，他也支持你使用第三方的云盘来对自己的文献附件进行云同步（不过没有特殊需求的话，更推荐使用 Zotero 官方的云盘，毕竟官方的更加稳定，而且官方运行也是要恰饭的嘛）。

* 在 PC 端
  * 安装 Zotero + [ZotFile](https://github.com/jlegewie/zotfile) 插件
  * ZotFile 把文件自动重命名并且放到文件夹里，然后同步到 OneDrive
* 在移动端
  * Android 可以使用 Zoo for Zotero，但是它只能访问 Zotero 官方网盘中的内容，因此只能通过 OneDrive 来查看文献。
  * IOS 有 papership 可以使用

#### Zotero 具体设置

打开 **编辑 -> 首选项 -> 高级 -> 文件和文件夹 -> 链接附件的根目录** 中选择 OneDrive 里的 Zotero 文件夹，这样当 Zotero 同步的时候，会同步一个相对地址，可以避免不同 PC 上 OneDrive 文件夹位置不同导致打不开 PDF

{% asset_img "Snipaste_2020-06-16_10-37-30.png" "settings in zotero" %}

#### 下载安装zotfile

  zotfile 应该是安装率最高的插件了，利用同步盘同步附件的方法也必须使用这个插件。
  [下载zotfile](http://zotfile.com/)
  打开zotero，打开 **工具 -> 插件**，  将刚刚下载的zotfile-x.x.x-fx.xpi文件拖到这个界面里进行安装

{% asset_img Snipaste_2020-06-16_11-28-04.png "install add-ins" %}

#### ZotFile 具体设置

在 工具 -> ZotFile Preferences - Location of Files - Custom Location 选择 OneDrive 的 Zotero 文件夹

{% asset_img Snipaste_2020-06-16_11-30-34.png "settings in zotfile" %}

第一次设置好之后，选中所有条目，**右键 - Manage Attachments - Rename Attachments** 然后应该就会在自己的 Zotero 文件夹里看到所有的 paper 啦。

{% asset_img Snipaste_2020-06-16_11-33-19.png "icon changes" %}
{% asset_img Snipaste_2020-06-16_11-34-26.png "files in onedrive" %}

### Endnote 库导入 Zotero

关于这个有[官方文档](https://www.zotero.org/support/zh/kb/importing_records_from_endnote)我就不写了😁
