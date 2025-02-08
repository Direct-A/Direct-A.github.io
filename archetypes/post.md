---
draft: true
title: "{{ replace .Name "-" " " | title }}"
description: "{{ .Name }}"
keywords: "{{replace .Name "-" ","}}"

date: {{ .Date }}
lastmod: {{ .Date }}

categories:
  - blog
tags:
  - test

author:          Direct-A
math: mathjax
toc: true
password:
abstract: 有东西被加密了，请输入密码查看
message: 请输入密码
---

{% asset_path filenameWithExpand %}
{% asset_link filenameWithExpand  title%}
{% asset_img filenameWithExpand title %}

<!-- more -->

<!-- 网页预览 -->
{% linkPreview url target rel %}

<!-- pdf预览 -->
{% pdf url [height] %}

<!-- 黑幕 -->
<span class='heimu' title='你知道的太多了'>黑幕测试</span>

<!-- 按钮 -->
{% btn url, text, icon [class], [title] %}

<!-- 图片组 -->
{% gp [number]-[layout] %}
{% endgp %}

<!-- 高亮标签 -->
{% label [class]@text %}

<!-- 链接组 -->
{% lg [image] [delimiter] [comment] %}
{% endlg %}

<!-- 笔记 -->
{% note [class] [no-icon] [summary] %}
Any content (support inline tags too).
{% endnote %}
