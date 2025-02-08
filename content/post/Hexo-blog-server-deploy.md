---
layout: post
title: Hexo个人博客私有云服务器部署
subtitle: Hexo个人博客迁移至私有云服务器，并部署
author: Direct-A
date: 2022-03-08
toc: true
top: false
cover: false
mathjax: true
categories:
  - blog
tags:
  - hexo
  - node.js
  - 博客建设
summary:
password:
description:
---

自打有自己的个人博客之后，就一直在用gitpage，感觉够用，也没有想着更换到个人服务器。
直到前一段时间，我更新了一篇博文，推上仓库，等 git action 自动部署成功后刷新博客地址，发现没有出现更新的那篇博文。
好好查了一下仓库部署用的分支，还有自己的配置，都没有问题，为什么没更新呢。
本着解决不了就搜索，谷歌搜了一下的问题，看到很多人都有这种问题，有两种说法：
- 一种是要等几天 gitpage 才会进行部署，github 使用的就是这种策略。
- 还有一种认为没有刷新缓存，`Ctrl + F5` 之后才会刷新。

<!-- more -->
两个都试了试，还是没有更新，好吧，我等等吧😮‍💨。
第二天我再次刷新之后，还是没有更新，这。。第三天刷新才更新。

emmmm，有点不太能接受了。
正好过年从腾讯云买了个三年的轻应用服务器，干脆迁移过去，给自己更大的控制权。

> 2022-04-12 更新
> 现在想想，估计那是 github 给加了 cdn，cdn 没更新，如果能够操控 cdn 手动刷新估计就能直接见到了。


## 准备工作

- 一台部署lnmp架构的服务器， [LNMP一键安装包 - CentOS/RadHat/Debian/Ubuntu下自动编译安装Nginx,PHP,MySQL,PHPMyAdmin](https://lnmp.org/)
- 一个域名
- 一个备案号（如果你服务器在国内，那么你还需要）
- node.js 环境
- hexo 环境

有了以上的内容就可以按照下面的步骤进行部署了

## 部署步骤

我使用的腾讯云的 Ubuntu 20.04，下面的步骤仅限于这个环境，其他的发行版请自行调整。

### 搭建 git 仓库

添加用户，并更改权限

```shell
sudo adduser git
sudo EDITOR=nvim visudo /etc/sudoers
```

给 git 用户以下权限

```text
git    ALL=(ALL)    ALL
```

保存并退出

切换到 git 用户并上传自己的公钥，让 git 你能够使用 git 访问服务器

```shell
sudo su -ls /bin/bash git
mkdir .ssh && chmod 700 .ssh
touch .ssh/authorized_keys && chmod 600 .ssh/authorized_keys
cat git.pub >> .ssh/authorized_keys
```

创建 git 仓库

```shell
mkdir myrepo && cd myrepo
git init --bare blog.git
```

至于为什么使用 `--bare` 参数，可以看 [git init 和 git init --bare 的区别？ - SegmentFault 思否](https://segmentfault.com/q/1010000004683286)

配置 git hooks 让你向服务提交代码后可以自动同步目录更新

```shell
cat > myrepo/blog.git/hooks/post-receive <<EOF
#!/bin/sh
git --work-tree=/home/wwwroot/<BLOG_DIRECTORY>/ --git-dir=/home/git/myrepo/blog.git checkout -f
EOF
chmod +x /var/repo/blog.git/hooks/post-receive
```

由于权限问题这里还会有一些细小的微调，但是不做展示，根据自己服务器的情况自行调整即可。

添加 `git-shell` 并更改 git 用户的shell

```shell
exit
sudo echo /usr/bin/git-shell >> /etc/shells
sudo chsh git
```

回到你自己的电脑，现在尝试 ssh 连接以下服务器，看一下咱们辛苦的成果

```shell
ssh git@<SERVER_IP>
#fatal: Interactive git shell is not enabled.
#hint: ~/git-shell-commands should exist and have read and execute access.
#Connection to gitserver closed.
```

返回内容类似上面的注释部分，那你就成功了，如果不是，那你可得好生排查排查，大概的几个方向：
- 权限问题，`.ssh` 目录以及 `.ssh/authorized_keys` 的权限
- `.ssh/authorized_keys` 内容是不是和你公钥一致
- 其他，根据自己的系统和其他周边设置找找吧

### lnmp 构架部署

这个我就不详述了，参考 [LNMP一键安装包 - CentOS/RadHat/Debian/Ubuntu下自动编译安装Nginx,PHP,MySQL,PHPMyAdmin](https://lnmp.org/) 。

### Nginx 配置

添加一个博客主页目录以及相关配置

```shell
lnmp vhost add
```

根据提示进行输入吧，这里每个人都不一样，根据自己的域名和需求调整吧。

接着修改 Nginx 的配置文件

```shell
sudo nvim /usr/local/nginx/conf/nginx.conf
```

修改 server 下 root 和 server_name 部分的参数

```conf
server
    {
        listen 80 default_server reuseport;
        #listen [::]:80 default_server ipv6only=on;
        server_name <YOUR_DOMAIN>;
        index index.html index.htm index.php;
        root  <YOUR_BLOG_PATH>;

        error_page   404   /404.html;

        # Deny access to PHP files in specific directory
        #location ~ /(wp-content|uploads|wp-includes|images)/.*\.php$ { deny all; }

        include enable-php.conf;
```


## 参考资料

[Hexo 博客部署到私有云服务器 - 1024搜-程序员专属的搜索引擎](https://www.1024sou.com/article/7405.html)  [Hexo 博客部署到私有云服务器 - SegmentFault 思否](https://segmentfault.com/a/1190000040283888) [利用云服务器搭建HEXO个人博客 - 知乎](https://zhuanlan.zhihu.com/p/387061562) [在阿里云上搭建Hexo博客详细流程 - 简书](https://www.jianshu.com/p/8b503f4fa378)
