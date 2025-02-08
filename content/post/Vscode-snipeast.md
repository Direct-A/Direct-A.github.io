---
layout: post
title: Vscode 用户代码片段创建的规则
subtitle: vscode sniooest
author: Direct-A
date: 2021-08-22
toc: true
top: false
cover: false
mathjax: true
categories:
  - programming
tags:
  - vscode
  - ide
  - snippets
  - 推荐
summary:
password:
description:
---

在写代码的时候，很多片段都是重复的，有些部分是固定不变的，也有些部分是仅需要修改一部分的。像这样的片段也没必要记住。这时候代码片段（snippest）就是一个很好的工具。
<!-- more -->

## 基本结构

```json
"display in hin list": {
  "scope": "use <C> + K M to search file type, empty is global",
  "prefix": "code-to-trigger-hint, can-be-multiple",
  "body": [
    "snippets to output, can be multi line",
    "character needs to convert \n \t \" $$ \\$ \\{",
    "curser placeholder, defaule is empty $1",
    "	can displayed in multiplace $1",
    "curser predefinded placeholder ${2:one}",
    "curser selecatable placeholder ${3|one,tow,three|}",
    "	can be nested ${3|one,two,three| ${4:four}}",
    "predefinded variable $CURRENT_MONTH $CURRENT_DATE $CURRENT_YEAR",
    "predefinded variable $CURRENT_MONTH $CURRENT_DATE $CURRENT_YEAR",
    "predefinded variable $CURRENT_MONTH $CURRENT_DATE $CURRENT_YEAR",
    "curser end placeholder, unnecessary $0"
  ],
  "description": "display in IntelliSense"
}
```

**注意：**现在版本的 vscode（`1.65.2`）改变了 snippest 的管理方案，每一种编程语言分别使用该语言名称作为文件名的 json 文件，作为该语言使用的snippets。
所以不用加 `scoop` 这一部分了。但是以前的 `code-snippets` 后缀的文件仍然可以使用。

## 变量

- `TM_SELECTED_TEXT` 当前选择的文本或空字符串
- `TM_CURRENT_LINE` 当前行的内容
- `TM_CURRENT_WORD` 光标下的单词内容或空字符串
- `TM_LINE_INDEX` 基于零索引的行号
- `TM_LINE_NUMBER` 基于一索引的行号
- `TM_FILENAME` 当前文档的文件名
- `TM_FILENAME_BASE` 当前文档的文件名，不带扩展名
- `TM_DIRECTORY` 当前文件的目录
- `TM_FILEPATH` 当前文档的完整文件路径
- `CLIPBOARD` 剪贴板中的内容
- `WORKSPACE_NAME` 打开的工作空间或文件夹的名称

以上用于替换，当前行指插入脚本。

当前日期和时间：

- `CURRENT_YEAR` 本年度
- `CURRENT_YEAR_SHORT` 本年度的最后两位数字
- `CURRENT_MONTH` 以两位数表示的月份（例如“ 02”）
- `CURRENT_MONTH_NAME` 月的全名（例如“july”）
- `CURRENT_MONTH_NAME_SHORT` 该月的简称（例如“ Jul”）
- `CURRENT_DATE` 一个月中的某天
- `CURRENT_DAY_NAME` 一天的名称（例如“周一”）
- `CURRENT_DAY_NAME_SHORT` 一天的简称（例如“ Mon”）
- `CURRENT_HOUR` 当前小时（24小时制）
- `CURRENT_MINUTE` 当前分钟
- `CURRENT_SECOND` 当前秒
- `CURRENT_SECONDS_UNIX` 自Unix时代以来的秒数

行或块注释，按照对应语言进行匹配：

- `BLOCK_COMMENT_START` 块注释
- `BLOCK_COMMENT_END` 块注释
- `LINE_COMMENT` 行注释

## 替换

大致的格式就是

`"${<STRING>/<MATCH_CASE>/<REPLACEMENT>/i}"`

## 如何添加

在 vscode 左下的设置中，点击 `User snippets`，然后按照界面UI提示就可以创建相应的 snippets 文件，并添加 snippets 了。

但是有一点需要注意，snippets 有 project、global、language 3 种生效范围，设置的时候注意范围别整了不生效。

## 参考资料

[Vs code添加自定义snippet - 博客园](https://www.cnblogs.com/silencehuan/p/11877655.html)
[escaping - VS代码段-转义$ {file} - IT工具网](https://www.coder.work/article/6679386)
