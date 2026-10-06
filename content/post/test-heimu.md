---
layout: post
title: 黑幕效果测试
author: Direct-A
date: 2026-10-06
draft: true
toc: false
---

这段字是{{< heimu >}}防剧透的黑幕内容{{< /heimu >}}测试。

这段字是{{< blur >}}防剧透的模糊内容{{< /blur >}}测试。

{{< heimu "别看了" >}}位置参数自定义提示{{< /heimu >}}

{{< heimu tip="真的别看了" >}}命名参数自定义提示{{< /heimu >}}

{{% heimu %}}
整段黑幕，支持 **Markdown** 语法。
{{% /heimu %}}

{{% blur %}}
整段模糊，支持 **Markdown** 语法。
{{% /blur %}}

<p class="heimu">原生 HTML 整段黑幕</p>

<p class="blur">原生 HTML 整段模糊</p>
