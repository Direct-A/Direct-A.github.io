---
layout: post
title: 进一步配置Zotero
subtitle: Zotero advance settings
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

# Zotero + Sci-Hub

说到将 Zotero 和 Sci-Hub 结合就首先得从Zotero PDF retrieval谈起。从Zotero 5.0.56版本开始，Zotero迎来了PDF retrieval功能。
该功能会在你用Zotero Connector保存文献时，自动检查Unpaywall上是否有可供下载的免费文献。
> Unpaywall能免费下载文献，但你不要以为它和Sci-Hub一样是非法的。其实Unpaywall是个非盈利性合法组织，它整合了数千个Open Access期刊或数据库，将免费文献集中之后开放API，从而供其他平台使用。

假如你在网页端保存的文献是Open Access的，Zotero Connector就会将PDF同文献条目一起抓取。对于已经在Zotero中却还没有PDF附件的文献条目，点击右键菜单中的Find Available PDF，即可下载文献。
<!-- more -->

但是，毕竟Unpaywall只支持OA文献，而OA文献又只是少数。也就是说，通过Unpaywall无法解决付费文献的下载问题。作为一款开源软件，Zotero的开发者为很多功能带来了可定制的能力，方便用户根据自己的喜好自定义。
PDF retrieval功能也不例外，Zotero允许用户自定义PDF解析器（custom PDF resolvers），也就是说你可以将其他网站作为PDF解析器，来替代Unpaywall。

Zotero 官网对于[自定义 PDF 解析器](https://www.zotero.org/support/kb/custom_pdf_resolvers)也有相关的文档

## 设置Sci-Hub作为PDF解析器

打开 **编辑 -> 首选项 -> 高级 -> 设置编辑器**。 
刚打开会有风险提示
{% asset_img "Snipaste_2020-06-16_18-45-58.png" "risk alarm" %}

点击 accept 后，在搜索框，搜索 `extensions.zotero.findPDFs.resolvers` 。
{% asset_img "Snipaste_2020-06-16_18-48-30.png" "after search" %}

双击 `extensions.zotero.findPDFs.resolvers`，默认情况下是只有一对`[]`。
删除`[]`，并将以下代码粘贴进去。

```json
{
    "name":"Sci-Hub",
    "method":"GET",
    "url":"https://sci-hub.tw/{doi}",
    "mode":"html",
    "selector":"#pdf",
    "attribute":"src",
    "automatic":true
}
```

然后点击OK。
到此就成功将Sci-Hub配置为PDF解析器了，也就是说替代了默认的Unpaywall。

现在，无需重启Zotero，即可调用Sci-Hub免费下载文献了。
{% asset_img "Snipaste_2020-06-16_18-55-53.png" "find pdf" %}

## 注意：

  1. 在`"url":"https://sci-hub.ren/{doi}"`中，目前可用的域名有`.tw、.ren、.si、.shop`，挑选其中一个就可以，哪个用起来体验更好就用哪个。
  2. 从`"url":"https://sci-hub.ren/{doi}"`还能看到一点。由于Sci-Hub是通过doi下载文献的，因此该PDF解析器也需要doi。也就说你的文献必须要有doi，如果doi是空缺的，便无法通过PDF解析器免费下载文献。幸运的是，对于缺失doi的文献，我们可以通过插件[zotero-shortdoi](https://github.com/bwiernik/zotero-shortdoi)插件一键抓取doi。
  3. `"automatic":true`，如果设置为true，Zotero会自动下载保存到Zotero中的文献的PDF。比如你用Zotero Connector保存了一些文献到Zotero，它便会自动帮你从Sci-Hub下载文献，并附在相应文献条目下。如果你不需要自动下载，可以设置为`"automatic":false`。

# Zotero + 百度学术、中国知网的文章检索引擎

**相较于之前在软件界面里进行操作，要实现这个功能，会显得有些难度，所以如果并非真的很迫切需要使用，没有能力的还是不要修改了。**

关于添加文章检索引擎的方法，[官方文档](https://www.zotero.org/support/locate#managing_lookup_engines)还是有讲的😁。里面提到有一个官方随时更新的`engines.json`文件，下载下来，保存到相应的文件夹就可以了。
另外官方文档里还提供了一张[检索引擎列表](http://egh.github.io/zotero-lookup-engines/)，可以结合之后的操作进行修改添加。

现将百度学术的搜索引擎添加方法记录于下：
依次点选 **首选项 -> 高级 -> 文件和文件夹 -> 打开数据文件夹**，然后在`locate文件夹`中找到文件`engines.json`，用文本编辑器打开。插入代码：

``` json
{
  "name": "百度学术搜索",
  "alias": "BaiDu",
  "icon": "http://xueshu.baidu.com/favicon.ico",
  "_urlTemplate": "https://xueshu.baidu.com/s?wd={z:title}&rsv_bp=0&tn=SE_baiduxueshu_c1gjeupa&rsv_spt=3&ie=utf-8&f=8&rsv_sug2=0&sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D",
  "description": "百度学术搜索",
  "hidden": false,
  "_urlParams": [],
  "_urlNamespaces": {
      "z": "http://www.zotero.org/namespaces/openSearch#",
      "": "http://a9.com/-/spec/opensearch/1.1/"
  },
  "_iconSourceURI": "http://xueshu.baidu.com/favicon.ico"
}
```

## 注意：

  * 搜索引擎代码之间用“,”隔开，可参考原文件的格式。
  * `_urlTemplate`的获取办法，先在百度搜索中搜索TEST，然后复制网址，将其中TEST替换为`{z:title}`。
  * icon的获取方法，一般在网站url后面加上 `/favicon.ico` 就可以了，但有些不是。如果不是的话，或者用Chrome 按 `F12` 查找，这种方法很麻烦。有一种较简易的方法，填写`https://www.google.com/s2/favicons?domain=http://xueshu.baidu.com` ，也能获取。格式就是`https://www.google.com/s2/favicons?domain=` 后面加上网址 `http://xueshu.baidu.com` ，以此类推。

cnki的定位网址有点特别
参考[Zotero 如何添加文章检索引擎？](https://www.zhihu.com/question/46484469/answer/651913741)，得到的网址如下：

```json
{
    "name": "CNKI搜索",
    "alias": "CNKI",
    "icon": "http://cnki.net/favicon.ico",
    "_urlTemplate": "http://kns.cnki.net/kns/brief/default_result.aspx?txt_1_sel=SU%24%=%7C&txt_1_value1={z:title}&txt_1_special1=%&txt_extension=&currentid=txt_1_value1&dbJson=coreJson&dbPrefix=SCDB&db_opt=CJFQ,CDFD,CMFD,CPFD,IPFD,CCND,CCJD&singleDB=SCDB&db_codes=CJFQ,CDFD,CMFD,CPFD,IPFD,CCND,CCJD&singleDBName=againConfigJson=false&action=scdbsearch&ua=1.11",
    "description": "CNKI搜索",
    "hidden": false,
    "_urlParams": [],
    "_urlNamespaces": {
        "z": "http://www.zotero.org/namespaces/openSearch#",
        "": "http://a9.com/-/spec/opensearch/1.1/"
    },
    "_iconSourceURI": "http://cnki.net/favicon.ico"
}
```
