---
layout:          post
title:           "批处理set命令的使用--变量及变量延迟"
subtitle:        how to use 'set' command
header-img:      img/post-bg-cmd.jpg
author:          Direct-A
date:            2019-06-21
catalog:         true
categories:
  - programming
tags:
  - 批处理文件
  - batch
---

在批处理文件中，`set`命令用于设置变量，为变量赋值，

``` bat
set [variable=["string"]]
set /p [variable=["string"]]
set /a expression
```

# `set /p [variable=["string"]]`

使用`/p`开关在命令行中创建交互，使输入的字符段对变量赋值

``` bat
set /p a="请输入变量a"
```

# `set /a expression`

使用`/a`开关允许`set`在赋值的同时进行简单的运算

在其中可使用的运算符包括

<!-- more -->

| 运算符             |     运算符     | 优先级依次降低 |
| :----------------- | :------------: | :------------: |
| `( ) `             |      分组      |       0        |
| `! ~ -`            |   一元运算符   |       1        |
| `* / %`            |   算数运算符   |       2        |
| `-`                |   算术运算符   |       3        |
| `<< >>`            | 二进制逻辑移位 |       4        |
| `&`                |       与       |       5        |
| `^`                |       非       |       6        |
| `|`                |       或       |       7        |
| `= *= /= %= += -=` |    算数赋值    |       8        |
| `&= ^= |= <<= >>=` | 二进制运算赋值 |       9        |
| `,`                |     分隔符     |       10       |

``` bat
set a=1
set b=2
set /a c=%a%+%b%
```

# set字符串处理

## 字符串替换

``` bat
%srting:str1=str2%
rem 字符替换
%srting:str1=%
rem 字符删除
```

## 字符串截取

``` bat
%string:~[m,[n]]%
%string:~[-9, 4]%
rem 从倒数第九位开始截取四位
```

| 参数 | 作用     | 默认值     |
| ---- | -------- | ---------- |
| `m`  | 偏移量   | 默认为0    |
| `n`  | 截取长度 | 默认为全部 |

# 扩展变量

## 与`%i`相关的变量

| 示例    | `c:\programfile\test.bat`   |
| ------- | --------------------------- |
| `%0`    | `"c:\programfile\test.bat"` |
| `%cd%`  | `c:\programfile`            |
| `%~0`   | `test.bat`                  |
| `%~f0`  | `c:\programfile\test.bat`   |
| `%~d0`  | `c:\`                       |
| `%~p0`  | `.\programfile\test.bat`    |
| `%~dp0` | `c:\programfile\`           |
| `%~n0`  | `test`                      |
| `%~x0`  | `.bat`                      |
| `%~nx0` | `test.bat`                  |
| `%~s0`  | 路径缩写                    |
| `%~a0`  | 文件属性                    |
| `%~t0`  | 创建时间                    |
| `%~z0`  | 文件大小                    |

## 命令行参数

`%0`表示执行文件`.bat`本身

`%1 %2 %3 ...`表示传入参数1，2，3，...

## 系统变量

| 变量                     |      | 解释                                                         | 示例                                                         |
| ------------------------ | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| %CD%                     | 本地 | 返回当前目录字符串                                           | `C:Documents and SettingsAdministrator桌面`                  |
| %OS%                     | 系统 | 返回操作系统名称                                             | Windows 2000 显示其操作系统为 Windows_NT                     |
| %DATE%                   | 系统 | 返回当前日期                                                 | `YYYY/MM/DD WWW`                                             |
| %TIME%                   | 系统 | 返回当前时间                                                 | `HH:MM:SS.SS`                                                |
| %PATH%                   | 系统 | 指定可执行文件的搜索路径                                     |                                                              |
| %PATHEXT%                | 系统 | 返回操作系统                                                 | 认为可执行的文件扩展名的列表                                 |
| %HOMEPATH%               | 系统 | 返回用户主目录的完整路径基于主目录值而设置用户主目录是在“本地用户和组”中指定的 | `Documents and SettingsAdministrator`                        |
| %USERPROFILE%            | 本地 | 返回当前用户的配置文件的位置                                 | `C:Documents and SettingsAdministrator`                      |
| %WINDIR%                 | 系统 | 返回操作系统目录的位置                                       | `C:WINDOWS`                                                  |
| %RANDOM%                 | 系统 | 返回 0 到 32767 之间的任意十进制数字                         | `30580`                                                      |
| %ERRORLEVEL%             | 系统 | 返回上一条命令的错误代码通常用非零值表示错误                 |                                                              |
| %COMPUTERNAME%           | 系统 | 返回计算机的名称                                             | `xxxx`                                                       |
| %USERNAME%               | 本地 | 返回当前登录的用户的名称                                     | `Administrator`                                              |
| %SYSTEMDRIVE%            | 系统 | 返回包含 Windows server operating system 根目录(即系统根目录`$P$G`的驱动器 | `C:`                                                         |
| %SYSTEMROOT%             | 系统 | 返回 Windows server operating system 根目录的位置            | `C:WINDOWS`                                                  |
| %HOMEDRIVE%              | 系统 | 返回连接到用户主目录的本地工作站驱动器号基于主目录值而设置用户主目录是在“本地用户和组”中指定的 | `C:`                                                         |
| %HOMESHARE%              | 系统 | 返回用户的共享主目录的网络路径基于主目录值而设置用户主目录是在“本地用户和组”中指定的 |                                                              |
| %NUMBER_OF_PROCESSORS%   | 系统 | 指定安装在计算机上的处理器的数目                             |                                                              |
| %PROCESSOR_LEVEL%        | 系统 | 返回计算机上安装的处理器的型号                               | `15`                                                         |
| %APPDATA%                | 本地 | 返回默认情况下应用程序存储数据的位置                         | `C:Documents and SettingsAdministratorApplication Data`      |
| %ALLUSERSPROFILE%        | 本地 | 返回“所有用户”配置文件的位置                                 | `C:Documents and SettingsAll Users`                          |
| %CMDCMDLINE%             | 本地 | 返回用来启动当前的 Cmd.exe 的准确命令行                      | `cmd /c ""C:Documents and SettingsAdministrator桌面a.bat" "` |
| %CMDEXTVERSION%          | 系统 | 返回当前的“命令处理程序扩展”的版本号                         | `2`                                                          |
| %COMSPEC%                | 系统 | 返回命令行解释器可执行程序的准确路径                         | `C:WINDOWSsystem32cmd.exe`                                   |
| %LOGONSERVER%            | 本地 | 返回验证当前登录会话的域控制器的名称                         | `\ xxxx`                                                     |
| %PROCESSOR_ARCHITECTURE% | 系统 | 返回处理器的芯片体系结构                                     | 值： x86 或 IA64 基于Itanium x86                             |
| %PROCESSOR_IDENTFIER%    | 系统 | 返回处理器说明                                               |                                                              |
| %PROCESSOR_REVISION%     | 系统 | 返回处理器的版本号                                           | `4f02`                                                       |
| %PROMPT%                 | 本地 | 返回当前解释程序的命令提示符设置                             | `$P$G`                                                       |
| %TEMP% %TMP%             |      | (temp)`C:DOCUME~1ADMINI~1LOCALS~1Temp`和(tmp)`C:DOCUME~1ADMINI~1LOCALS~1Temp`系统和用户返回对当前登录用户可用的应用程序所使用的默认临时目录 | 有些应用程序需要 TEMP，而其他应用程序则需要 TMP              |
| %USERDOMAIN%             | 本地 | 返回包含用户帐户的域的名称                                   | `xxxx`                                                       |

# 变量延迟

在平时使用`for`的时候，会有需要产生能够自加的变量，然后根据变量的值进行相应的操作。在这种时候就需要用到变量延迟。

``` bat
for /f "delims= tokens=1,2,3,*" %%i in ('dir /a-d /o-d /tc') do (
  set /a n+=1
  if %n%==2 echo %%i
)
```

上述的代码就如我们所臆想的写了出来，**但是**不能实现我们所想的效果

``` bat
setlocal enabledelayedexpansion
for /f "delims= tokens=1,2,3,*" %%i in ('dir /a-d /o-d /tc') do (
  set /a n+=1
  if !n!==2 echo %%i
)
endlocal
```

当开启变量延迟后，预期效果得以实现。

在这里`!!`内部的变量，在执行下一步命令前才会执行赋值命令，进而可以动态的感知变量的变化。而`%%`内部的变量，直接在赋值语句执行时就进行赋值，**但是**只有在下一条命令执行时才得以显现（可以理解为利用 之前的数据 作为 目前行 执行的前提，目前行 执行的结果在储存进之前的数据中去）。

``` bat
set var1=2
set var1=5 & echo %var1%
rem 2
```

上面的代码可以理解成这样

{% asset_img "delayed-expansion.png" 未开启变量延迟 %}

运用这个规律可以在不使用临时变量的情况下，进行变量间的数值交换

``` bat
set var1=a
set var2=b
set var1=%var2% & set var2=%var1%
```

### 注意

1. 批处理文件是一行一行的一次执行的
2. `()`内的命令将被视作在同一行内
