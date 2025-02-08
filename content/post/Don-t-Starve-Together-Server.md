---
layout: post
title: Don't Starve Together 私有服务器搭建
subtitle: 搭建自己的饥荒联机私有服务器
author: Direct-A
toc: true
top: false
cover: false
mathjax: true
categories:
  - blog
tags:
  - game
  - 饥荒
  - 饥荒联机板
  - DST
date: 2022-03-24 14:56:20
description:
password:
summary:
---

在 Linux 上玩饥荒联机版是通过 Proton 兼容层运行的，玩起来没什么么问题，但是联机使用自己本机建的公共服务器就会出现延迟过高，别人连进来没法一起开心的游戏。毕竟是兼容层里面的，也难怪。正好手里有服务器，所以就想顺手整个自建的私有饥荒服务器。

下面就是我自己搭建饥荒私有服务器的过程以及踩坑实录。
<!-- more -->

## 必备条件
- 云服务器一台
- Klei用户ID：按下面图片的流程就可以拿到了
	- {% asset_img "Pasted image 20220324135501.png" "用户信息" %}
	- {% asset_img "Pasted image 20220324135649.png" "KeliID" %}
- cluster_token
	- {% asset_img "Pasted image 20220324135758.png" "游戏" %}
	- {% asset_img "Pasted image 20220324135835.png" "服务器" %}
	- {% asset_img "Pasted image 20220324135912.png" "创建服务器" %}
	- 根据上面的连接就可以创建新的 cluster_token 了
- 存档文件
	- 存档可以使用前面的网页里生成的
	- 也可以使用自己本地游戏新建存档
		- `Proton 6.3` 可以适应 Linux 下的目录结构，直接在当前用户的 `$HOME` 目录下就可以见到 `.klei` ，里面就是每个存档的目录
		- `Proton 7` 以上的在 `.steam/steam/steamapps/compatdata/322330/pfx/drive_c/users/steamuser/Documents/Klei/DoNotStarveTogether` 下找到可以找到

## 部署流程

可以使用 [饥荒联机版专用服务器搭建全流程Windows-Linux - 冰牛奶](https://www.icemilk.top/archives/ff1824ec.html#%E6%8B%B7%E8%B4%9D%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E5%88%B0%E6%9C%8D%E5%8A%A1%E7%AB%AF%E5%B9%B6%E5%90%AF%E5%8A%A8) 的流程，包括了 Windows 和 Linux 的，不过我的有我自己的优化。

也可以直接用 [GitHub - cuukenn/dontstarveserver: 饥荒linux服务器安装、启停、定时更新脚本](https://github.com/cuukenn/dontstarveserver) 的脚本，可能更快捷。

### 安装依赖

```shell
# Ubuntu 服务器的话就使用这个吧
sudo add-apt-repository multiverse
sudo dpkg --add-architecture i386
# aliyun 的用户可以直接用这条，tencentyun 的就老实把前面的运行了
# 不知道 tencenyun 的镜像怎么定制的
sudo apt install libstdc++6:i386 libgcc1:i386 libcurl4-gnutls-dev:i386 screen
```

### 创建用户

创建个新用户，分离不同服务，避免相互权限干扰。

```shell
useradd steam
password steam
su steam
```

### 安装 steamcmd

国内的服务器下载安装可能会慢一些。

```shell
mkdir ~/steamcmd
wget -P ~/steamcmd https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz
cd ~/steamcmd
tar -xvzf ~/steamcmd/steamcmd_linux.tar.gz
./steamcmd.sh \
	+login anonymous \
	+app_update 343050 validate \
	+quit
```

### 部署游戏配置

服务器上的游戏存档目录在 `~/.klei/DoNotStarveTogether` 下面，里面有各个档的目录，每个档下面目录结构如下：

```plantext
├── Caves                            # 洞穴世界的目录
│   ├── backup
│   ├── leveldataoverride.lua
│   ├── modoverrides.lua             # 使用的服务器 mod 列表，后面需要用
│   ├── save
│   ├── server_chat_log.txt
│   ├── server.ini
│   └── server_log.txt
├── Master                            # 地上世界的目录
│   ├── backup
│   ├── leveldataoverride.lua
│   ├── modoverrides.lua              # 使用的服务器 mod 列表，后面需要用，但是内用和前面的那个基本一样
│   ├── save
│   ├── server_chat_log.txt
│   ├── server.ini
│   └── server_log.txt
├── adminlist.txt                     # 管理员 ID 存储文件
├── blocklist.txt                     # 黑名单 ID 存储文件
├── cluster_token.txt                 # cluster_token 就放这里面
└── cluster.ini                       # 当前存档的配置文件
```

`cluster.ini` 内容

```plantext
[GAMEPLAY]
game_mode = survival                 # 游戏风格
max_players = 6                      # 服务器支持的最大玩家数量，最大值 12
pvp = false                          # PvP
pause_when_empty = true              # 没人服务器暂停


[NETWORK]
lan_only_cluster = false             # 是不是局域网联机
cluster_intention = cooperative
cluster_password = 01days            # 游戏密码
cluster_description =                # 游戏描述
cluster_name = 01days的世界          # 游戏名
offline_cluster = false              # 可不可以联机
cluster_language = zh


[MISC]
console_enabled = true               # 控制台开启


# 下面的和洞穴世界分服务器有关，但是一般创建在一台服务器里没啥问题
[SHARD]
shard_enabled = true
bind_ip = 127.0.0.1
master_ip = 127.0.0.1
master_port = 10888                 # 端口
cluster_key = defaultPass
```

### 初次运行 & mod 下载

存档和配置文件配置好了，就可以上传服务器，放在相应的位置了。

紧接着配置 mod。
在 `~/Steam/steamapps/common/Don't Starve Together Dedicated Server/mods` 下

```plantext
├── bin                                                 # 32位运行程序
│   ├── dontstarve
│   ├── dontstarve_dedicated_server_nullrenderer
│   ├── dontstarve.xpm
│   ├── lib32
│   ├── scripts
│   └── steam_appid.txt
├── bin64                                               # 64位运行程序
│   ├── dontstarve
│   ├── dontstarve_dedicated_server_nullrenderer_x64    # 主程序
│   ├── dontstarve.xpm
│   ├── lib64
│   ├── scripts
│   └── steam_appid.txt
├── cached_mod_manifests
├── data
│   └── ...
├── dontstarve.xpm
├── linux64
│   └── ...
├── mods                                                # mod 都在里面
│   ├── dedicated_server_mods_setup.lua                 # 指定 mod 加载更新的配置文件
│   ├── INSTALLING_MODS.txt
│   ├── MAKING_MODS.txt
│   ├── modsettings.lua
│   └── ...
├── steamclient.so
├── ugc_mods
│   └── ...
└── version.txt
```

`dedicated_server_mods_setup.lua` 内容结构

```lua
--There are two functions that will install mods, ServerModSetup and ServerModCollectionSetup. Put the calls to the functions in this file and they will be executed on boot.

--ServerModSetup takes a string of a specific mod's Workshop id. It will download and install the mod to your mod directory on boot.
        --The Workshop id can be found at the end of the url to the mod's Workshop page.
        --Example: http://steamcommunity.com/sharedfiles/filedetails/?id=350811795
        --ServerModSetup("350811795")

--ServerModCollectionSetup takes a string of a specific mod's Workshop id. It will download all the mods in the collection and install them to the mod directory on boot.
        --The Workshop id can be found at the end of the url to the collection's Workshop page.
        --Example: http://steamcommunity.com/sharedfiles/filedetails/?id=379114180
        --ServerModCollectionSetup("379114180")
```

这里使用的 ID 不一定就得自己去创意工坊去找，可以在游戏里自己添加，然后寻找 `~/.klei/DoNotStarveTogether/Master/modoverrides.lua` 里面的 `workshop-xxxxxx`，这里 `xxxxxx` 就是 ID，放进里面就可以了。

切换到 `~/Steam/steamapps/common/Don't Starve Together Dedicated Server/bin64/lib64` 下运行 `./dontstarve_dedicated_server_nullrenderer_x64`，等运行完了看看有没有在 `mods` 目录下创建对应的 `workshop-xxxxxx` 目录，缺一个加载 mod 都会失败。

tencenyun 的话可能下载 mod 会有下不下来的，但是如果你只前在自己本地的游戏有创建过游戏存档，那你就可以从本地把 mod 都拿出来上传服务器。
关于本地 mod 的研究可以看 [Steam版饥荒联机版 创意工坊下载mod的机制探索 - 哔哩哔哩](https://www.bilibili.com/read/cv12896150)。
我个人对于的理解就是：
- `~/.steam/steam/steamapps/workshop/content/322330`
	- 所有的创意工坊 mod
	- 解压了的是本地 mod
	- 没解压的是 `.bin` 格式的压缩文件
-  `~/.steam/steam/steamapps/common/Don't Starve Together/mods`
	- 里面是服务器 mod

## 参考资料

[饥荒联机版专用服务器搭建全流程Windows-Linux - 冰牛奶](https://www.icemilk.top/archives/ff1824ec.html#%E6%8B%B7%E8%B4%9D%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E5%88%B0%E6%9C%8D%E5%8A%A1%E7%AB%AF%E5%B9%B6%E5%90%AF%E5%8A%A8) [GitHub - cuukenn/dontstarveserver: 饥荒linux服务器安装、启停、定时更新脚本](https://github.com/cuukenn/dontstarveserver) [Steam版饥荒联机版 创意工坊下载mod的机制探索 - 哔哩哔哩](https://www.bilibili.com/read/cv12896150)
