# 黑幕 / 模糊遮罩效果实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 为 direct-a.cn（Hugo + hugo-theme-next）文章添加防剧透「黑幕」与「模糊」遮罩效果，悬停显示、移动端可点击切换。

**Architecture:** 全部走主题官方扩展点，不修改 `themes/` 内任何文件：自定义 CSS 经 `customFilePath.style` 注入 `<head>`；点击切换 JS 经 `customFilePath.footer` 以 partial 形式注入页脚；`layouts/_shortcodes/` 提供 `heimu`/`blur` 两个短代码（`{{< >}}` 行内输出 `<span>`，`{{% %}}` 块级输出 `<div>`）。

**Tech Stack:** Hugo v0.167.0+extended（新模板系统，`layouts/_shortcodes/`）、Goldmark（`renderer.unsafe = true`）、原生 CSS/JS（无依赖）。

## Global Constraints

- 工作目录：`/Users/yishai/Documents/kimi/Workspaces/zola主题生成/direct-a.cn`，当前分支 `hugo`
- 绝不修改 `themes/hugo-theme-next/` 内任何文件
- 测试构建一律输出到 `/tmp/heimu-build`（`hugo -D --destination /tmp/heimu-build --cleanDestinationDir`），绝不用默认 `public/` 目录
- 站点配置 `[minify] minifyOutput = true`，生产构建的 HTML 会被压缩：grep 校验时只匹配特征子串，不要假设属性顺序和空白
- 多语言站点（zh-cn 默认 + en-us），测试文章放在默认语言，`/post/test-heimu/` 路径位于构建输出根下
- 提交信息遵循仓库 gitmoji 惯例（参照 `git log --oneline`：`:bug:`、`:memo:` 等）
- 规格文档：`docs/superpowers/specs/2026-10-06-heimu-blur-design.md`

---

### Task 1: 黑幕/模糊 CSS 样式 + 启用自定义样式入口

**Files:**
- Create: `static/css/custom_style.css`
- Modify: `config/_default/params.toml`（第 62-65 行附近的 `[customFilePath]` 注释块）

**Interfaces:**
- Consumes: 主题机制 `customFilePath.style`（`themes/hugo-theme-next/layouts/_partials/head/styles.html:42-46` 会输出 `<link>` 指向该 CSS）
- Produces: CSS 类 `.heimu`、`.blur`、`.revealed`（Task 2 的短代码和 Task 3 的 JS 依赖这三个类名）

- [ ] **Step 1: 创建 `static/css/custom_style.css`**

完整内容如下：

```css
/* ============================================================
 * 防剧透遮罩：黑幕 (.heimu) 与模糊 (.blur)
 * 悬停显示；.revealed 为 JS 点击切换的展开态
 * 参考: https://dev.fandom.com/wiki/Heimu / SpoilerBlur
 * ============================================================ */

/* ---------- 黑幕 ---------- */
.heimu {
  background-color: #252525;
  border-radius: 2px;
  cursor: help;
  transition: color 0.3s ease;
}
/* 遮盖所有内链子元素（链接色、代码底色等） */
.heimu, .heimu * {
  color: #252525 !important;
  text-shadow: none !important;
}
.heimu code, .heimu pre {
  background-color: #252525 !important;
}
.heimu img {
  visibility: hidden;
}
/* 悬停 / 点击展开：黑条保留，文字翻白 */
.heimu:hover, .heimu.revealed {
  color: #ffffff !important;
}
.heimu:hover *, .heimu.revealed * {
  color: #ffffff !important;
}
.heimu:hover img, .heimu.revealed img {
  visibility: visible;
}

/* ---------- 模糊 ---------- */
.blur {
  filter: blur(5px);
  cursor: help;
  transition: filter 0.5s ease;
}
.blur:hover, .blur.revealed {
  filter: none;
}

/* ---------- 打印时强制显示 ---------- */
@media print {
  .heimu, .heimu * {
    background-color: transparent !important;
    color: inherit !important;
  }
  .heimu img {
    visibility: visible;
  }
  .blur {
    filter: none !important;
  }
}
```

- [ ] **Step 2: 启用 `customFilePath.style`**

修改 `config/_default/params.toml`，把这段（约 62-65 行）：

```toml
# [customFilePath]
#sidebar = custom_sidebar.html
#footer = custom_footer.html
#style = /css/custom_style.css
```

改为（`footer` 一行在 Task 3 才会启用，本任务只加 `style`）：

```toml
[customFilePath]
#sidebar = custom_sidebar.html
#footer = custom_footer.html
style = "/css/custom_style.css"
```

- [ ] **Step 3: 构建并验证 CSS 被注入**

Run:
```bash
cd /Users/yishai/Documents/kimi/Workspaces/zola主题生成/direct-a.cn
hugo -D --destination /tmp/heimu-build --cleanDestinationDir
grep -o 'custom_style\.css[^"]*' /tmp/heimu-build/index.html | head -1
```

Expected: 构建无报错；grep 输出一行类似 `custom_style.css?v=1759...`（证明 `<link>` 已注入首页 `<head>`）。再抽查一个文章页：

```bash
grep -c 'custom_style\.css' /tmp/heimu-build/post/adb-control-android-phone/index.html
```

Expected: 输出 `1`（或更多）。

- [ ] **Step 4: Commit**

```bash
cd /Users/yishai/Documents/kimi/Workspaces/zola主题生成/direct-a.cn
git add static/css/custom_style.css config/_default/params.toml
git commit -m ":sparkles: Add heimu/blur spoiler styles and enable custom style entry"
```

---

### Task 2: heimu / blur 短代码 + 测试文章

**Files:**
- Create: `layouts/_shortcodes/heimu.html`
- Create: `layouts/_shortcodes/blur.html`
- Create: `content/post/test-heimu.md`（草稿，仅测试用，Task 4 结束时删除）

**Interfaces:**
- Consumes: Task 1 产出的 CSS 类 `.heimu`、`.blur`
- Produces: 短代码 `{{< heimu >}}` / `{{< blur >}}`（行内）与 `{{% heimu %}}` / `{{% blur %}}`（块级）；提示参数：位置参数 0 优先，其次命名参数 `tip`，默认「你知道的太多了」（Task 3 的 JS 只依赖类名，不依赖本任务的参数）

- [ ] **Step 1: 创建 `layouts/_shortcodes/heimu.html`**

完整内容如下（`{{% %}}` 变体的 `.Inner` 经 Markdown 渲染后含 `<p>`，据此判断输出 `<div>` 还是 `<span>`）：

```html
{{- $tip := .Get 0 | default (.Get "tip") | default "你知道的太多了" -}}
{{- if strings.Contains .Inner "<p>" -}}
<div class="heimu" title="{{ $tip }}">{{ .Inner }}</div>
{{- else -}}
<span class="heimu" title="{{ $tip }}">{{ .Inner }}</span>
{{- end -}}
```

- [ ] **Step 2: 创建 `layouts/_shortcodes/blur.html`**

完整内容如下（与 heimu 相同，仅类名不同）：

```html
{{- $tip := .Get 0 | default (.Get "tip") | default "你知道的太多了" -}}
{{- if strings.Contains .Inner "<p>" -}}
<div class="blur" title="{{ $tip }}">{{ .Inner }}</div>
{{- else -}}
<span class="blur" title="{{ $tip }}">{{ .Inner }}</span>
{{- end -}}
```

- [ ] **Step 3: 创建测试文章 `content/post/test-heimu.md`**

完整内容如下（front matter 格式参照 `content/post/adb-control-android-phone.md`）：

```markdown
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
```

- [ ] **Step 4: 构建并验证渲染结果**

Run:
```bash
cd /Users/yishai/Documents/kimi/Workspaces/zola主题生成/direct-a.cn
hugo -D --destination /tmp/heimu-build --cleanDestinationDir
```

Expected: 构建无报错（若报短代码相关错误，检查文件路径是否为 `layouts/_shortcodes/`）。

然后逐项 grep 验证（HTML 已压缩，只匹配特征子串）：

```bash
P=/tmp/heimu-build/post/test-heimu/index.html
grep -c 'class="heimu"' "$P"        # 期望 >= 4（行内3 + 块级1 + 原生HTML 1，实际应为 5）
grep -c 'class="blur"' "$P"         # 期望 >= 3
grep -c '你知道的太多了' "$P"        # 期望 4（未传提示参数的 4 个短代码：行内/块级各 2）
grep -c '别看了' "$P"               # 期望 2（“别看了”与“真的别看了”各 1）
grep -o '<span class="heimu"[^>]*>防剧透的黑幕内容' "$P"
grep -o '<div class="heimu"' "$P"
grep -o '<span class="blur"[^>]*>防剧透的模糊内容' "$P"
grep -o '<div class="blur"' "$P"
```

Expected: 各 `grep -c` 计数达标；四个 `grep -o` 均有输出（证明行内输出 `<span>`、块级输出 `<div>`）。

- [ ] **Step 5: Commit**

```bash
cd /Users/yishai/Documents/kimi/Workspaces/zola主题生成/direct-a.cn
git add layouts/_shortcodes/heimu.html layouts/_shortcodes/blur.html content/post/test-heimu.md
git commit -m ":sparkles: Add heimu/blur shortcodes with draft test post"
```

---

### Task 3: 点击切换 JS（移动端支持）

**Files:**
- Create: `layouts/_partials/custom_footer.html`
- Modify: `config/_default/params.toml`（Task 1 建立的 `[customFilePath]` 表内）

**Interfaces:**
- Consumes: Task 1 的类名 `.heimu` / `.blur` / `.revealed`；主题机制 `customFilePath.footer`（`themes/hugo-theme-next/layouts/_partials/footer.html:61-63` 以 `partialCached` 加载站点 `layouts/_partials/custom_footer.html`）
- Produces: 无（末端功能）

- [ ] **Step 1: 创建 `layouts/_partials/custom_footer.html`**

完整内容如下（事件委托，点击命中 `.heimu`/`.blur` 时切换 `.revealed`）：

```html
<script>
  document.addEventListener('click', function (e) {
    var t = e.target.closest('.heimu, .blur');
    if (t) {
      t.classList.toggle('revealed');
    }
  });
</script>
```

- [ ] **Step 2: 启用 `customFilePath.footer`**

修改 `config/_default/params.toml` 中 Task 1 建立的表，把：

```toml
[customFilePath]
#sidebar = custom_sidebar.html
#footer = custom_footer.html
style = "/css/custom_style.css"
```

改为：

```toml
[customFilePath]
#sidebar = custom_sidebar.html
footer = "custom_footer.html"
style = "/css/custom_style.css"
```

- [ ] **Step 3: 构建并验证脚本注入**

Run:
```bash
cd /Users/yishai/Documents/kimi/Workspaces/zola主题生成/direct-a.cn
hugo -D --destination /tmp/heimu-build --cleanDestinationDir
grep -c "closest('.heimu, .blur')" /tmp/heimu-build/index.html
grep -c "closest('.heimu, .blur')" /tmp/heimu-build/post/test-heimu/index.html
```

Expected: 两处均输出 `1`（JS 压缩不会改变单引号字符串内容；若为 `0`，先检查 `grep -c 'classList.toggle'`，仍无则说明 partial 未被加载，检查文件名与配置拼写）。

- [ ] **Step 4: Commit**

```bash
cd /Users/yishai/Documents/kimi/Workspaces/zola主题生成/direct-a.cn
git add layouts/_partials/custom_footer.html config/_default/params.toml
git commit -m ":sparkles: Add click-to-reveal toggle for heimu/blur via custom footer"
```

---

### Task 4: 端到端浏览器验证 + 清理测试文章

**Files:**
- Delete: `content/post/test-heimu.md`（验证通过后删除）

**Interfaces:**
- Consumes: Task 1-3 的全部产出
- Produces: 无

- [ ] **Step 1: 启动本地服务**

Run（后台运行）:
```bash
cd /Users/yishai/Documents/kimi/Workspaces/zola主题生成/direct-a.cn
hugo server -D --port 1313
```

Expected: 输出 `Web Server is available at http://localhost:1313/`，无构建错误。

- [ ] **Step 2: HTTP 层验证**

Run:
```bash
curl -s -o /dev/null -w '%{http_code}' http://localhost:1313/css/custom_style.css
curl -s http://localhost:1313/post/test-heimu/ | grep -c 'class="heimu"'
curl -s http://localhost:1313/post/test-heimu/ | grep -c "closest('.heimu, .blur')"
```

Expected: `200`；计数 >= 4；计数 `1`。（`hugo server` 是开发模式不压缩 HTML，计数与 Task 2 的压缩构建可能略有差异，达标线不变。）

- [ ] **Step 3: 浏览器视觉验证**

在浏览器打开 `http://localhost:1313/post/test-heimu/`，逐项确认：

1. 初始状态：黑幕处显示为纯黑条（文字不可读），模糊处内容不可读
2. 鼠标悬停黑幕：黑条内文字变白可读；悬停模糊：内容变清晰
3. 点击黑幕：松开后保持显示（`.revealed` 生效），再次点击恢复遮盖
4. 块级黑幕内的 **Markdown 加粗**正常渲染
5. 切换站点暗色模式（主题 `darkmode = true`），黑幕/模糊仍可用

如发现视觉问题，回到对应 Task 修 CSS/JS 后重新验证。

- [ ] **Step 4: 删除测试文章并做最终构建**

```bash
cd /Users/yishai/Documents/kimi/Workspaces/zola主题生成/direct-a.cn
rm content/post/test-heimu.md
hugo -D --destination /tmp/heimu-build --cleanDestinationDir
```

Expected: 构建无报错（确认删除草稿后短代码不再被任何内容引用也不影响构建）。

- [ ] **Step 5: 停止服务并 Commit**

停掉后台的 `hugo server`，然后：

```bash
cd /Users/yishai/Documents/kimi/Workspaces/zola主题生成/direct-a.cn
git add -A
git commit -m ":white_check_mark: Verify heimu/blur E2E and remove draft test post"
```

（若 Step 4 后工作区无变化——例如测试文章本就未纳入版本控制之外的其他改动——则跳过空提交。）
