---
layout:          post
title:           "批处理for命令的使用--创建post"
subtitle:        how to use 'for' command
header-img:      img/post-bg-cmd.jpg
author:          Direct-A
date:            2019-06-16
catalog:         true
categories:
  - programming
tags:
  - 批处理文件
  - batch
---

对于刚创建的博客，使用起来还不是很熟，`_post`里的`MarkDown`文件开头需要有 `tag、title、categroies、layout` 总是记不住格式和内容。今天就构思了个脚本，来解决这个苦恼。

最近刚上手批处理文件，还是有很多不熟悉，最难懂也是最厉害的命令就是`for`命令，这次就记一下笔记。

# `for`命令

`for`命令适用于遍历文件、文本内容，可以截取文件、文本，使用范围很广。

## `for`命令的基本格式

``` bat
for [/d /f /l /r] ["options"] %%i in (file) do (comminds)
for [/d /f /l /r] ["options"] %%i in ("string") do (comminds)
for [/d /f /l /r] ["options"] %%i in ('comminds') do (comminds)
```

<!-- more -->

`for` 命令的作用是，将`file`、`string`或`comminds`中的内容按照`["options"]`中的条件匹配并赋值给`%%i`然后执行`comminds`

### 注意

1. `for` `in`和`do`是基本元素，一个都不能少
2. `in`之后和`do`之前的括号不能缺少
3. `%%i`是形式参数，在后面的`do`中作为参数的起点
4. `in`之后的部分用`""`引用的部分作为字符串遍历其内容
5. `in`之后的部分用`''`引用的部分作为命令遍历其执行结果
6. `in`之后的部分不引用的作为文件遍历其内容

## `FOR /D %%variable IN (set) DO command [command-parameters]`

检索目录，不包括子目录，不包括文件

``` bat
for /d %%i in (c:\w*) do echo %%i
```

检索以`w`开头的目录

## `FOR /R [[drive:]path] %%variable IN (set) DO command [command-parameters]`

递归检索目录，检索目录下所有的子目录

``` bat
for /r c:\ %%i in (*.exe) do echo %%i
```

检索目录下所有`.exe`文件

``` bat
for /r c:\ %%i in (boot.ini) do echo %%i
```

将枚举目录下所有子目录，因此改写为

``` bat
for /r c:\ %%i in (boot.ini) do if exit echo %%i
```

### 注意

1.`/r`**不遍历**隐藏文件

## `FOR /L %%variable IN (start,step,end) DO command [command-parameters]`

创建数列，每个数字占一行

``` bat
for /l %%i in (1,1,5) do start cmd
1
2
3
4
5
```

打开五个命令提示符窗口

## `FOR /F %%variable IN (set) DO command [command-parameters]`

用以提取和截取文本内容，可以处理和切割文本内容

``` bat
FOR /F %%variable ["options"] IN (files) DO command [command-parameters]
FOR /F %%variable ["options"] IN ("string") DO command [command-parameters]
FOR /F %%variable ["options"] IN ('commind') DO command [command-parameters]
```

### options

* delims
* tokens
* eol
* skip
* usebackq

#### delimas

指定分隔符，**默认为空格和tab**，指定后替代

``` bat
type c:\test\test.txt
123#456#789#101112
for /f "delims=#" %%i in (c:\test\test.txt) do echo %%i
123
```

1. `"delims="`可将分隔符指定为空

#### tokens

指定提取字段位置

``` bat
type c:\test\test.txt
123#456#789#101112
123#456#789#101112
for /f "delims=# tokens=3" %%i in (c:\test\test.txt) do echo %%i
789
789
for /f "delims=# tokens=1,3" %%i in (c:\test\test.txt) do echo %%i %%j
123 789
123 789
for /f "delims=# tokens=1,3,*" %%i in (c:\test\test.txt) do echo %%i %%j
123 789
123 789
for /f "delims=# tokens=1,3,*" %%i in (c:\test\test.txt) do echo %%i %%j %%k
123 789 101112
123 789 101112
for /f "delims=# tokens=1,3*" %%i in (c:\test\test.txt) do echo %%i %%j %%k
123 789 101112
123 789 101112
for /f "delims=# tokens=1-4" %%i in (c:\test\test.txt) do echo %%i %%j %%k %%l
123 456 789 101112
123 456 789 101112
```

1. 每行分隔的内容重新以空格分隔并输出
2. `tokens=1,3*`和`tokens=1,3,*`是等效的

#### eol

忽略指定标志起始的行

``` bat
type c:\test\test.txt
#123#456#789#101112
0123#456#789#101112
for /f "eol=# delims=# tokens=3" %%i in (c:\test\test.txt) do echo %%i
789
```

1. 只能指定一个符号，多个就报错
2. 要指定多个需要命令嵌套
3. `"eol="`可将字符集指定为空

#### skip

指定跳过行数

``` bat
type c:\test\test.txt
#123#456#789#101112
0123#456#789#101112
for /f "delims=# tokens=1 skip=1" %%i in (c:\test\test.txt) do echo %%i
0123
```

#### usebackq

改变<code>``''""</code>的作用
<code>`comminds`</code>、`'string'`、`"files"`

``` bat
for /f "usebackq" %%i in ("test 1.txt") do echo %%i
for /f "usebackq" %%i in (`type test.txt`) do echo %%i
for /f "usebackq" %%i in ('hello world!') do echo %%i
```

就是 单引号->反引号，双引号->单引号，没引号->双引号

1. 用以应对文件名内有 空格 或 & 的
2. 应对命令中有 & 的

***

一个例子：

``` bat
For /f "delims=" %%i in (1.txt) do (
  Set /a n+=1
  If !n!==2 Echo %%i
)
```

用以输出文件`1.txt`中的第二行
