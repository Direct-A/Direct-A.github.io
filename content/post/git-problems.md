---
layout: post
title: 【持续更新】git 使用中的问题
subtitle: Troubleshooting of git
author: Direct-A
date: 2020-06-16
toc: true
top: false
cover: false
mathjax: true
categories:
  - programming
tags:
  - git
  - troubleshooting
summary:
password:
description:
---

## Problem

{% asset_img "image-20200525105854145.png" "problem1" %}

## Solution

我以为是我用的代理软件`clash`规则文件有问题（以前出过这事），但是连接`github`正常。

几番查找，最终还是使用最为暴力的方法解决了。干脆就把验证关了，
<!-- more -->


``` shell
git config --global http.sslVerify false
git config --global https.sslVerify false
```

OK, problem solved!

## Problem

{% asset_img "image-20200531103451068.png" "problem2" %}

## Solution

最初以为自己乱改代理端口整坏了，后来发现是`~/.ssh`下没有`known_hosts`文件。

为确认，通过命令`ssh -T git@github.com`，进行验证。

通过添加`config`文件

``` config
Host github.com
  Hostname ssh.github.com
  Port 443
```

问题解决。

## Problem

``` shell
ssh: connect to host github.com port 22: Connection timed out
fatal: Could not read from remote repository.
```
`https`开头的链接克隆不报错，一旦换成`ssh`就出问题

## Solution

给`ssh`加代理

``` config
# windows
ProxyCommand connect -S 127.0.0.1:1080 -a none %h %p
# linux
Host *
  ProxyCommand nc -X 5 -x 127.0.0.1:1080 %h %p
```

## Problem

``` shell
git submodule add https://github.com/repo.git
## fatal: unable to access 'https://github.com/repo.git/': gnutls_handshake() failed: Error in the pull function.
```

正常克隆仓库都可以使用，但是就在这没法用。

## Solution

自己粗心大意，把`.gitconfig`的代理设置出错了，`http/https`都走`socks5`了。

``` config
git config --global http.proxy http://127.0.0.1:1080
git config --global https.proxy http://127.0.0.1:1080
```

problem solved
