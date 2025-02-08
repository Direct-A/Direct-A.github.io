---
layout:           post
title:            hexo博客搭建
author:           Direct-A
date:             2020-03-26
toc:              true
top:              false
cover:            false
mathjax:          false
categories:
  - programming
tags:
  - hexo
  - node.js
  - 博客建设
summary: hexo 个人博客建设
password:
description: 换电脑了，之前 jekyll 搭博客那一套太麻烦，懒得再安了，看 hexo 轻巧，就决定改使用 hexo。这里就记录一下安装过程中的一些磕磕绊绊
---

之前的博客是基于 jekyll 搭建的，但是 jekyll 再本地的软件安装实在有些恼人，~~我换电脑了，懒得再安了~~，了解到 hexo 只需要安装 node.js ，并且之后的都是在 node.js 里添加 module ，我决定改使用 hexo。

# Install hexo

在开始着手自己搭建 hexo 博客前，首先还是先看看官方的教程。这是搭建的第一步，同时也可以增加对 hexo 的了解。

[官方教程](https://hexo.io/docs/)

# `_config.yml` 配置文件

对于 hexo 来说，配置文件主要存在于两个地方，
  1. 主目录下的 `_config.yml`，后称**站点配置文件**
  2. 主目录/theme/主题名目录下的 `_config.yml`，后称**主题配置文件**

<!-- more -->

由于存在两个配置文件，刚开始配置时会搞不清动手哪一个。在 NexT 的 [Github](https://github.com/theme-next/hexo-theme-next/blob/master/docs/zh-CN/DATA-FILES.md) 文档里，由关于这方面的推荐方案。
我是用的是 **选择1** 来配置 `_config.yml`，也就是把主题配置文件中需要的配置复制进站点配置文件中进行修改。这样做对于后续的主题升级来说是一件轻松的事，但是对于最初修改配置并企图实时渲染查看是，就没法实现了。每次对站点配置文件进行修改后（post文件是可以实时的），需要在命令行 `ctrl+c` 结束进程，然后 `hexo clean & hexo s -o` 来启动服务，实在折腾。
对于这个目前还不知道有什么好的解决方案。

# 首页内容显示控制

对于刚搭建好，而且也已经把以往的 post 已经放进 hexo 的 `source/_post` 中了。此时的 hexo 网站，会直接显示所有文章的全文。
这时候有两种选择：
  1. 使用 `<!-- more -->` 在 markdown 中自己进行控制（官方推荐）
  2. 使用插件 [chekun/hexo-excerpt](https://github.com/chekun/hexo-excerpt) 来解决问题
以上来自 [hexo Github issue page](https://github.com/theme-next/hexo-theme-next/issues/1217)

# 页面添加

添加新页面，使用的是 hexo 的命令 `hexo new page name` ，但是对于部分页面内容特殊，需要根据后来的更改自动生成，这里对我设置时的查找进行收集整理

## 添加 tags 页面

1. 新建页面

``` bash
hexo new page tags
```

2. 编辑刚新建的页面，将页面的类型设置为 tags ，主题将自动为这个页面显示标签云。页面内容如下：（主目录/source/tags/index.md）

``` markdown
---
title: tags
date: 2020-03-26 12:39:04
type: "tags"
---
```

这里 `type: "tags"` **是必须的**不能遗漏，但是引号不一定要有

3. 在菜单中添加链接。编辑主题配置文件（主目录/themes/next/_config.yml），添加 tags 到 menu 中，如下：

``` yaml
menu:
  home: /
  archives: /archives
  tags: /tags
```
以上内容参考自[知乎页面](https://www.zhihu.com/question/29017171)

# hexo 网站的部署

> ## 使用 `hexo deploy` 进行部署
> 
> 部署的整个流程，以及其他平台上部署和其他部署方法，均参考[hexo官方文档](https://hexo.io/zh-cn/docs/one-command-deployment)
> 
> 对于部署后覆盖 master 分支的问题我通过创建 resource 分支来存储博客源码，在 master 分支发布网站部署内容来解决。
> 由于我是用公开 repo 创建的 gitpage ，使用 hexo deploy 如果用的是同一个项目，那就会出现覆盖 master 分支下的文件这种问题，有些头疼，所以最后我决定使用 Travis CI 。
> 
> ## 使用 Travis CI 进行 hexo 自动化部署
> 
> 使用 Travis CI 进行部署前的检测，以及进行自动部署
> 
> ### 创建 Travis CI 账户
> 
> 可以直接使用 github 账户登录，方便快捷。登陆后可以选择给指定 repo 安装，还是给全部 repo 安装。
> 
> ### 了解 Travis CI
> 
> 阅读[官方文档](https://docs.travis-ci.com/user/for-beginners/)，快速了解 Travis CI。
> 其实 Travis CI ,就相当于一个机器人，在提交之后根据你提前已经进行设置的流程，对提交的代码进行检测并部署。
> 减少工作量，只需要 git push 然后就可以先休息，等测试结果出来了再查看并解决，通过每次提交检测，来提升代码质量。
> 
> ### Travis CI 的几个专有名词的理解
> 
> ![专有名词](/images/word_in_specific_meaning.png)
> 
> ### Travis CI 的配置
> 
> 1. 首先主目录下建立文件 `.travis.yml`
> 2. 按照[]()

以前的配置多少有些问题，不过现在不一样了，现在我们有 Github Action ，我们可以通过第三方或者官方的 actions 省去繁杂的代码书写，快速进行博客提交后部署。

## github action 使用

在 repo 根目录下建立 `.github/workflows` 目录

在目录中创建一个 yaml 文件，命名可以随意，但是最好能明白文件用途。

文件内容如下

```yaml
name: check & deploy

on:
  push:
    branches:
      - resource
  pull_request:
    branches:
      - resource

env:
  TZ: Asia/Shanghai
  GIT_USER: Direct-A
  GIT_EMAIL: songyicheng0@gmail.com
  THEME_REPO: theme-next/hexo-theme-next
  THEME_BRANCH: master
  THEME_PATH: themes/next
  DEPLOY_REPO: Direct-A/Direct-A.github.io
  DEPLOY_BRANCH: master
  DEPLOY_KEY: ${{secrets.DEPLOY_KEY}}
  BUILD_REPO: Direct-A/Direct-A.github.io
  BUILD_BRANCH: resource

jobs:
  build:
    name: Build on node ${{ matrix.node_version }} and ${{ matrix.os }}
    runs-on: ubuntu-latest
    strategy:
      matrix:
        os: [ubuntu-latest]
        node_version: [17.1]

    steps:
      - name: Checkout
        uses: actions/checkout@v2
        with:
          ref: ${{env.BUILD_BRANCH}}

      - name: Checkout theme repo
        uses: actions/checkout@v2
        with:
          repository: ${{env.THEME_REPO}}
          ref: ${{env.THEME_BRANCH}}
          path: ${{env.THEME_PATH}}

      - name: Use Node.js ${{matrix.node_version}}
        uses: actions/setup-node@v1
        with:
          node-version: ${{matrix.node_version}}

      - name: Install dependencies
        run: |
          npm install -g hexo-cli
          npm install

      - name: Deploy hexo
        run: |
          sudo timedatectl set-timezone "$TZ"
          hexo clean && hexo generate
          cd public && git init && git add -A
          git config --global user.name $GIT_USER
          git config --global user.email $GIT_EMAIL
          git commit -m "GitHub Actions Auto Builder at $(date +'%Y-%m-%d %H:%M:%S')"
          git push --force --quiet "https://$DEPLOY_KEY@github.com/$DEPLOY_REPO" master:master
```

下面写啥：
- action yaml 的各项内容，及含义，使用
- hexo deply 部署的流程
- 这个 action 的部署流程
- next 主题使用的过程中的坑
- 主题配置过程中的问题
