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
summary:
password:
description:
---

# Problem

{% asset_img image-20200525105854145.png problem1 %}

# Solution

我以为是我用的代理软件`clash`规则文件有问题（以前出过这事），但是连接`github`正常。

几番查找，最终还是使用最为暴力的方法解决了。干脆就把验证关了，
<!-- more -->


``` shell
git config --global http.sslVerify false
git config --global https.sslVerify false
```

OK, problem solved!

# Problem

{% asset_img image-20200531103451068.png problem2 %}

# Solution

最初以为自己乱改代理端口整坏了，后来发现是`~/.ssh`下没有`known_hosts`文件。

为确认，通过命令`ssh -T git@github.com`，进行验证。

通过添加`config`文件

``` config
Host github.com
  Hostname ssh.github.com
  Port 443
```

问题解决。
