---
layout: post
title: Hexo Next Theme 踩坑
subtitle: 我碰到的 Next Theme 问题及解决集合
author: Direct-A
date: 2022-03-11
toc: true
top: false
cover: false
mathjax: true
categories:
  - blog
tags:
  - next
  - hexo
  - node.js
  - 博客建设
  - Throubleshooting
summary:
password:
description: Hexo Next Theme 部署及美化过程中遇到的各种奇奇怪怪的问题及解决方案，不定期更新
---

## 报错 Accessing non-existent property

{% asset_img "Pasted image 20220311175317.png"%}

### 环境

```shell
❯ hexo -v
INFO  Validating config
INFO  ==================================
  ███╗   ██╗███████╗██╗  ██╗████████╗
  ████╗  ██║██╔════╝╚██╗██╔╝╚══██╔══╝
  ██╔██╗ ██║█████╗   ╚███╔╝    ██║
  ██║╚██╗██║██╔══╝   ██╔██╗    ██║
  ██║ ╚████║███████╗██╔╝ ██╗   ██║
  ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝   ╚═╝
========================================
NexT version 8.10.1
Documentation: https://theme-next.js.org
========================================
hexo: 5.4.1
hexo-cli: 4.3.0
os: linux 5.16.13-zen1-1-zen Arch Linux
node: 17.3.0
v8: 9.6.180.15-node.12
uv: 1.42.0
zlib: 1.2.11
brotli: 1.0.9
ares: 1.18.1
modules: 102
nghttp2: 1.45.1
napi: 8
llhttp: 6.0.4
openssl: 3.0.1+quic
cldr: 40.0
icu: 70.1
tz: 2021a3
unicode: 14.0
ngtcp2: 0.1.0-DEV
nghttp3: 0.1.0-DEV
```

### 复现

每次 `hexo s` 部署后，访问页面均会有


### 解决方案

> Hexo 这里的 warning是由于[stylus](https://link.juejin.cn/?target=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fstylus%2Fstylus "https://link.zhihu.com/?target=https%3A//github.com/stylus/stylus")导致的，幸运的是stylus 在 0.54.8 版本修复了这个问题，所以对于 Hexo 用户来说，重新装一下hexo-renderer-stylus，就可正常使用。
> 但是我重装之后发现还是会报警告，继续追溯源头，发现是这其实是[ni](https://link.juejin.cn/?target=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fwww.npmjs.com%2Fpackage%2Fnib "https://link.zhihu.com/?target=https%3A//www.npmjs.com/package/nib")b这个包里的 stylus 引起的问题，而这个包已经很久没更新了。
> 2.1 将hexo-renderer-stylus更新到2.0.1
> 2.2 将stylus 从0.54.5更新到0.54.8

添加内容至根目录 `package.json` ：
```json
"resolutions": {
  "stylus": "^0.54.8"
}
```


## 参考资料

[解决 Hexo 使用 Node.js 14 Accessing non-existent property问题 - 掘金](https://juejin.cn/post/7003301549359235086)
