---
layout: post
title: 【Rust】基础知识
subtitle: Base knowlage of Rust programming language
author: Direct-A
date: 2021-12-02
toc: true
top: false
cover: false
mathjax: true
categories:
  - programming
tags:
  - rust
  - 基础知识
  - 编程笔记
summary:
password:
description:
---

## 为什么需要 Rust ？

C、C++ 高效快速，但是内存操作存在安全问题。
python 等使用 GC 进行内存管理的语言，虽然没有操作内存的安全问题，但是运行速度始终上不去

rust 的诞生就是为了在保证内存安全的状态下，保证程序的运行效率；并不是百分百的消除内存安全问题，而主要在于非法访问导致的内存安全隐患，主要包含：
- 对空指针和垂悬指针进行解引用
- 读取为初始化的内存
- 缓存溢出
- 非法访问已释放或未分配的指针
<!-- more -->

**内存泄露并不能够通过 Rust 的设计进行防范**


## Rust特性

1. Rust 是一种 **预编译静态类型**(ahead-of-time compiled)语言
2. Rust 是强类型语言，但具有**自动判断变量类型**的能力（相对于静态弱类型的 C 以及动态强类型的 python）
3. Rust 是一种混合范式的面向过程的编程语言
  - 包含面向对象、函数式编程、泛型和面向过程
  - 面向对象和函数式是一种语言特性，并非抽象方式
  - 使用过程中整体感觉和使用C类似，主要按照面向过程的方式进行编程，更加关注问题本身
  - **本质上是一门面向表达式的语言**，即整个计算过程都是通过表达式进行求值，而非通过语句进行状态修改
4. Rust 适用于追求编程语言的速度与稳定性的开发者
5. Rust 的编译器检查确保了增加功能和重构代码时的稳定性
6. Rust 语言为了高并发安全而做的设计：在语言层面尽量少的让变量的值可以改变

相对其他语言的优点：
1. 类型安全：编译器可确保不会将任何操作应用于错误类型的变量。
2. 内存安全：Rust 指针（称为“引用”）始终引用有效的内存。
3. 无数据争用：Rust 的 borrow 检查器通过确保程序的多个部分不能同时更改同一值来保证线程安全。
4. 零成本抽象：Rust 允许使用高级别概念，例如迭代、接口和函数编程，将性能成本控制在最低，甚至不会产生成本。 这些抽象的性能与手工编写的底层代码一样出色。
5. 最小运行时：Rust 具有非常小的可选运行时。 为了有效地管理内存，此语言也不具有垃圾回收器。 在这一点上，Rust 非常类似于 C 和 C++ 之类的语言。
6. 面向裸机：Rust 可以用于嵌入式和“裸机”编程，因此适合用于编写操作系统内核或设备驱动程序。


Rust 在整体上可以分为两部分：
- safe rust
  - 全部代码均需要经过编译器的检查
- unsafe rust，主要面向其他编程语言、系统和底层硬件
  - 仅在下面5种情况下不需要对代码进行检查
    - 解引用裸指针
    - 调用 unsafe 函数或方法
    - 访问或修改可变静态变量
    - 实现 unsafe trait
    - 读写 Unie 联合体中的字段


## Rust 的管理软件

### rustup 工具链管理工具

```bash
# 安装稳定版的Rust
rustup install stable
```

#### rustc

编译工具，由标准输入传入文件并编译

#### rustfmt

代码格式化工具，由标准输入传入文件并格式化

#### rust-analyzer

代码分析工具

### cargo 项目、编译管理

Cargo 是 Rust 的构建系统和包管理器。它可以为你处理很多任务，比如构建代码、下载依赖库并编译这些库。

对于有依赖的项目，使用 cargo 进行管理将带来很多便利。

```bash
# 创建二进制项目，编译后获得一个可执行二进制文件
cargo new <PROJ_NAME>

# 现有的 git 仓库中运行 cargo new，则不会生成 git 文件；你可以通过使用
cargo new --vcs=git <PROJ_NAME>

# 创建库，编译后获得一个lib<LIB_NAME>.rlib文件
cargo new --lib my-library
```

Cargo 的项目文件组织逻辑中：

- 源文件存放在 src 目录中
- 项目根目录只存放 README、license 信息、配置文件和其他跟代码无关的文件

```bash
# 项目构建
# 项目目录下运行
# 仅构建，构建可执行文件 target/debug/hello_cargo 目录下
cargo build
cargo b
# 构建并优化，可执行文件 target/release
cargo build --release

# 构建并运行
cargo run
cargo r

# 快速检查代码确保其可以编译，但并不产生可执行文件
cargo check
cargo c
# 测试项目
cargo test

#  编译项目的文档。
cargo doc

# 将库发布到 crates.io。
cargo publish
```

### Cargo 镜像源更改

1. 在用户目录下 `.cargo` 目录下，创建 `config` 文件
2. 添加如下内容
  ```toml
  [source.crates-io]
  replace-with = 'ustc'
  
  [source.ustc]
  registry = "git://mirrors.ustc.edu.cn/crates.io-index"
  ```

#### `Cargo.toml`

```toml
# 项目信息
[package]
name = "float"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

# 依赖包罗列，引入第三方 crates
[dependencies]
regex = "1.4.2"
```


## Rust 基本编程规范

- `main` 函数是一个特殊的函数在可执行的 Rust 程序中，它总是最先运行的代码
- 所有函数体都要用花括号包裹起来，左花括号与函数声明置于同一行并以空格分隔
- Rust 的缩进风格使用 4 个空格
- 符号 `!` 的时候，就意味着调用的是宏而不是普通函数，并且宏并不总是遵循与函数相同的规则
- 大部分 Rust 代码行以分号结尾
- 代码所需要的库叫做 **依赖**(dependencies)
- 函数和变量名使用 CamalCase 规范风格，小写字母下划线分割


## Rust 的版本标记方式

- 语义化版本，`<MAIN_VER>.<SUB_VER>.<REV_VER>`
  - main_ver: 不兼容的API修改
  - submain_ver: 向下兼容的功能增强
  - revision_ver: 向下兼容的问题修复
- 发行版
  - master -> neight，夜版每晚完成一个版本的编译
  - beta -> 测试版，每6周
  - stable -> 稳定版，每6周
- Edition 版次，自2015开始每3年
  - 对前3年的改变进行总结
  - 制定每3年的主要目标


## 编译过程

{% asset_img "Pasted image 20220119235159.png" 编译过程示意 %}

AST：抽象语法树
HIR：高级中间语言，消除版次差异
MIR：中级中间语言
LLVMIR：LLVM中间语言

正因为这一编译方案，在使用第三方库是并不需要考虑该库是不是你当前使用的Rust兼容的，也就是说**生态不存在版本割裂**。
