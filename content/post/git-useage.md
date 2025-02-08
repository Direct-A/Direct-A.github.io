---
layout: post
title: 【未完待续】git使用汇总
subtitle: how to git
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
  - how to
summary:
password:
description:
---


# 什么是 Git

git 是一个用于版本控制的软件，或者说

> 是一个开源的分布式版本控制系统。

它是 Linus Torvalds 为了管理 Linux 的内核代码开发而开发的软件。

# Git 的原理

我认为，只有知道原理，才能更好的使用一个工具。所以我又了解了一下 git 的原理。

在使用 git 进行版本控制时，可以将需要进行版本控制的文件分类为三个阶段，如下图。
<!-- more -->

<!-- ![git 命令流程图](http://upload-images.jianshu.io/upload_images/3884693-b327d97357a30f8c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240) -->

{% asset_img "1719120-a3db1c8caa1324e2.webp" "img" %}

- 未进行版本控制
- 暂存
- 存入仓库

# Git 的安装

## Windows

[官网](https://git-scm.com/)下载

{% asset_img "image-20200412232715087.png" "image-20200412232715087" %}

双击安装程序，一路下一步，直至安装结束。

## Linux

在 ubuntu 下，直接使用命令行进行安装更为方便：

``` shell
sudo apt install -y git
```

# 基础配置

使用 git 的第一步，首先设置一下全局邮箱和用户名

winsows 在桌面右键，可以看到 `Git Bash Here`，点击后打开这样一个界面

{% asset_img "image-20200413104956115.png" "image-20200413104956115" %}

在界面内输入

``` shell
git config --global user.name "yourName"
git config --global user.email "yourEmail"
```

Linux 直接在终端输入上述命令，名字和邮箱按自己的内容填写在`yourName`和`yourEmail`的位置。

完成后使用`git config --global --list`查看设置情况。


# 使用 Git 进行版本控制

进入计划使用 Git 进行版本控制的文件目录

``` shell
git init
git add *
```

创建 git 仓库，并将当前目录下所有文件添加入当前库。

git 是通过`.git`文件夹来存储目录下文件的变动历史，以及分支和提交信息。所以创建版本库后，在当前目录下会出现一个`.git`文件夹。如果想重新建立库，可以直接删除`.git`文件夹，重新开始上述步骤。

## git 基本操作

| 命令                            | 作用                                                         | 示例                                                                    |
| :------------------------------ | :----------------------------------------------------------- | :---------------------------------------------------------------------- |
| `^`                             | 相对引用，向过去移动一次提交                                 |                                                                         |
| `~num`                          | 相对引用，向过去移动`num`次提交                              |                                                                         |
| `git init`                      |                                                              | {% asset_img "image-20200419101438349.png" "image-20200419101438349" %} |
| `git config`                    |                                                              |                                                                         |
| `git add`                       | 添加文件进入版本控制中                                       | `git add *`                                                             |
| `git stage`                     | 暂存某文件                                                   |                                                                         |
| `git rm`                        |                                                              |                                                                         |
| `git remote`                    | 管理远程仓库                                                 |                                                                         |
| `git remote -v`                 | 查看已添加的远程仓库                                         | {% asset_img "image-20200419110204418.png" "image-20200419110204418" %} |
| `git remote add`                | 添加一个远程仓库连接                                         | `git remote add github git@github.com:Direct-A/readed_articles.git`     |
| `git clone`                     | 克隆远程仓库                                                 | {% asset_img "image-20200419102608234.png" "image-20200419102608234" %} |
| `git commit`                    | 提交暂存文件修改                                             |                                                                         |
| `git commit -m`                 | 提交暂存文件修改并添加注释                                   | {% asset_img "image-20200419101826781.png" "image-20200419101826781" %} |
| `git push`                      | 向远程仓库提交修改                                           |                                                                         |
| `git pull`                      | 拉取远程仓库的修改                                           |                                                                         |
| `git fetch`                     |                                                              |                                                                         |
| `git branch`                    | 创建分支                                                     |                                                                         |
| `git branch -a`                 | 查看当前所有分支                                             | {% asset_img "image-20200419113528526.png" "image-20200419113528526" %} |
| `git branch -f master hashCode` | 移动分支头至指定提交                                         |                                                                         |
| `git merge`                     | 将指定分支合并入当前分支                                     |                                                                         |
| `git merge --no-ff`             | 合并同时提交一次，针对被合并分支后续无提交                   |                                                                         |
| `git rebase`                    | 变基，减少分支                                               |                                                                         |
| `git rebase -i`                 | 交互式变基，需要指定变基起点                                 |                                                                         |
| `git reset`                     | 撤回提交，撤回的提交处于未加入暂存区状态，对远程仓库**无效** |                                                                         |
| `git revert`                    | 撤销提交更改，创建一次提交，用以保存更改，对远程仓库**有效** |                                                                         |
| `git checkout`                  | 切换分支                                                     | {% asset_img "image-20200419102323690.png" "image-20200419102323690" %} |
| `git checkout -b`               | 切换分支并自动创建分支                                       |                                                                         |
| `git status`                    | 查看仓库状态，所在分支，文件变动，待提交和暂存情况           | {% asset_img "image-20200419101553362.png" "image-20200419101553362" %} |
| `git diff`                      | 查看尚未缓存的改动                                           |                                                                         |
| `git diff  --cash`              | 查看已缓存改动                                               |                                                                         |
| `git diff HEAD`                 | 查看所有改动                                                 |                                                                         |
| `git diff --stat`               | 显示当前改变的摘要                                           |                                                                         |
| `git cherry-pick hashCode `     | 复制指定提交至当前分支                                       |                                                                         |

# 远程仓库（Repository）的使用

由于 git 的分布式特点，我们在使用 git 命令时都是在本地执行，如果你想通过 git 分享你的代码，与他人合作或者对代码进行云端存储及备份。 你就需要将代码放在一个相应的代码托管平台上，目前使用最多的基于 git 的代码托管平台是 GitHub，GitLab 和 国内的 Gitee。

# 推荐

[Learn Git breaching](https://learngitbranching.js.org/) 可视化教学

[tig](https://github.com/jonas/tig) 命令行git commit tree
