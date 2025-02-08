---
layout:          post
title:           个人博客环境搭建：Ruby + jekyll 本地环境搭建
subtitle:        windows Ruby + jekyll 本地环境搭建
header-img:      img/post-bg-debug.png
header-mask:     0.25
catalog:         true
author:          Direct-A
date:            2019-07-06
categories:
  - blog
tags:
  - jekyll
  - ruby
---

 :sweat_smile: 由于自己不熟悉 gitpage ，就直接配置的 github 上的库来创建的博客，所以在开始的时候调试都是靠提交后上 gitpage 上看，简直不要多麻烦。最近查找了一下可以搭建本地的调试环境，而且这还是创建新博客的开始 :sweat_smile: 。下面正文。

## 配置本地环境

### 配置本地环境，首先需要安装 `Ruby` 以及 `Devkit`

[ruby下载链接](https://rubyinstaller.org/downloads/)

我是安装的是 rubyinstaller-2.6.3-1-x64.exe 和 DevKit-mingw64-64-4.7.2-20130224-1432-sfx.exe

**注意**：这里 rubyinstaller-2.6.3-1-x64.exe 安装完之后不要执行`ridk install`

<!-- more -->

### 安装好 Devkit 和 Ruby 后，命令行`cd`切换至本地`Ruby`的安装目录

执行`ruby dk.rb init`，提示`"Initialization complete!"`表示安装成功。

继续执行`ruby dk.rb review`和`ruby dk.rb install`

### 更换 gem 源

``` powershell
# 查看源
gem sources -l
# 删除原来的源，添加清华源
gem sources --add https://mirrors.tuna.tsinghua.edu.cn/rubygems/ --remove https://rubygems.org/
# 更新源
gem sources -u
```

### 运行 rubyinstaller

``` powershell
ridk install
```

这时会让我们做出选择，选3，过程中会下载很多安装包，耐心等待，一定要耐心，要完整装完才行，装好会让你再做一次123选择，这个时候不需要选了，直接enter退出就行了。

### 安装`jekyll`和`bundle`

``` powershell
gem install jekyll bundle
```

## 运行本地已建立的博客文件

``` powershell
bundle install
```

安装缓慢，可能需要翻墙

安装完成之后就可以运行

``` powershell
bundle exec jekyll serve
```

将本地的博客跑起来

## 报错处理

### 直接执行`jekyll serve`，报错

``` powershell
   You have already activated public_suffix 3.1.1, but your Gemfile requires public_suffix 3.1.0. Prepending `bundle exec` to your command may solve this. (Gem::LoadError)
```
原因很明显，应当执行`bundle exec jekyll serve`

### 执行`bundle exec jekyll serve`后仍报错

``` powershell
Dependency Error: Yikes! It looks like you don't have jekyll-paginate or one of its dependencies installed. In order to use Jekyll as currently configured, you'll need to install this gem. The full error message from Ruby is: 'cannot load such file -- jekyll-paginate' If you run into trouble, you can find helpful resources at https://jekyllrb.com/help/!jekyll 3.8.5 | Error:  jekyll-paginate
```

此时需要在`gemfile`中添加`gem "jekyll-paginate"`

## 参考

[Ruby x Jekyll 本地调试环境搭建](http://szhshp.org/tech/2015/11/14/localjekyllenv.html#2016-10-07-error-undefined-method-size-for-nilnilclass-nomethoderror)
[命令行用法](https://www.jekyll.com.cn/docs/usage/)
[全网最清晰的Jekyll+Github搭建个人博客](https://yq.aliyun.com/articles/640926?spm=a2c4e.11155472.0.0.7ec27bb5iMKDlj)
[本地jekyll突然不能正常工作，遇到的问题全可以在这个文章中找到答案。](https://blog.csdn.net/jearmy/article/details/42752919)
