# 黑幕 / 模糊遮罩效果设计

日期：2026-10-06
状态：已获批准
参考：https://blog.yuaner.tw/2025/06/css-heimu/ （Heimu 黑幕 + SpoilerBlur 模糊，源自 Fandom Developers Wiki / 萌娘百科）

## 背景与目标

direct-a.cn 是 Hugo 站点，主题为 hugo-theme-next。需要在文章中支持防剧透遮罩：

- **黑幕（heimu）**：内容盖上黑色遮罩条，悬停时显示内容
- **模糊（blur）**：内容模糊化，悬停时变清晰

已确认的需求决策：

| 问题 | 决策 |
|---|---|
| 效果范围 | 黑幕 + 模糊 两者都要 |
| 标记写法 | Hugo shortcode 为主，CSS 类同时开放给原生 HTML |
| 移动端 | 悬停之外，支持点击切换显示/隐藏（需少量 JS） |

约束：Hugo Goldmark 不支持 markdown-it-attrs 的 `[文字]{.heimu}` 行内属性语法，故用 shortcode 替代。

## 方案

采用主题官方扩展点，零侵入主题文件，主题升级不受影响：

1. `customFilePath.style` → 加载自定义 CSS（`themes/hugo-theme-next/layouts/_partials/head/styles.html:42`）
2. `customFilePath.footer` → 加载自定义页脚 partial，内联 `<script>`（`themes/hugo-theme-next/layouts/_partials/footer.html:61`）
3. 站点级 shortcode 目录 `layouts/_shortcodes/`（Hugo 新模板系统，与主题机制一致）

## 组件

### 1. 样式 `static/css/custom_style.css`

`.heimu`：

- 默认：`background-color: #252525; color: #252525; text-shadow: none;`（文字与底色同色形成黑条）
- 内部链接 `a`、`<code>`、`<img>` 等子元素同样遮盖（链接色、code 背景都压成 #252525；图片用 `visibility` 或黑色覆盖处理）
- 悬停 / `.revealed` 态：背景保持 #252525，文字变白，带 0.3s 过渡
- 鼠标指针：`cursor: help` 提示可交互
- 悬停提示：shortcode 输出 `title` 属性（默认「你知道的太多了」）

`.blur`：

- 默认：`filter: blur(5px);`
- 悬停 / `.revealed` 态：`filter: none;`，过渡 0.5s

共用：

- `.heimu.revealed`、`.blur.revealed` 为 JS 点击切换的展开态，样式与 `:hover` 一致
- 暗色模式（站点 `darkmode = true`）下黑条与模糊效果天然兼容，无需额外适配；若实测暗色下对比度异常，再针对性修正
- `@media print`：打印时强制显示全部内容（黑幕去掉遮盖、模糊去掉 filter）

### 2. 短代码 `layouts/_shortcodes/heimu.html`、`layouts/_shortcodes/blur.html`

两者逻辑相同，仅类名不同：

- 行内用法 `{{< heimu >}}文字{{< /heimu >}}` → `<span class="heimu" title="你知道的太多了">文字</span>`，`.Inner` 不套段落
- 块级用法 `{{% heimu %}}整段 Markdown、图片{{% /heimu %}}` → `<div class="heimu" title="...">` + `.Inner` 经 Markdown 渲染（Hugo 中 `{{% %}}` 变体自动渲染内部 Markdown）
- 可选位置参数 0 或命名参数 `tip` 自定义悬停提示文字

### 3. 点击切换 JS `layouts/_partials/custom_footer.html`

内联 `<script>`（约 10 行，原生 JS，无依赖）：

- 事件委托监听 `document` 点击
- 命中 `.heimu` / `.blur` 元素时切换其 `.revealed` 类
- 脚本放页脚，DOM 已就绪，无需 DOMContentLoaded 包装

### 4. 配置 `config/_default/params.toml`

解开并补全现有的注释块（`params.toml:62-65`）：

```toml
[customFilePath]
style = "/css/custom_style.css"
footer = "custom_footer.html"
```

## 写作用法示例

```markdown
这段字是{{< heimu >}}防止被剧透的黑幕设计{{< /heimu >}}测试。

这段字是{{< blur >}}防止被剧透的模糊设计{{< /blur >}}测试。

{{< heimu "自定义提示" >}}带自定义悬停提示{{< /heimu >}}

{{% heimu %}}
整段遮盖，支持 **Markdown** 与图片：

![图片](/imgs/example.png)
{{% /heimu %}}

<!-- 原生 HTML 同样可用 -->
<p class="blur">整段模糊</p>
```

## 错误处理与边界

- 短代码内容为空：照常输出空标签，不报错
- JS 未加载/被禁用：桌面悬停仍可用（纯 CSS 兜底），仅失去点击切换
- 嵌套遮罩：不特殊处理，内层随外层一起显示即可
- RSS/搜索引擎：遮罩内容仍是正常 HTML 文本，不影响收录（与参考站点行为一致）

## 测试与验证

1. `hugo server` 本地起站
2. 在 `content/post/` 新建一篇测试文章，覆盖：行内黑幕、行内模糊、自定义提示、块级（段落+图片）、原生 HTML 写法
3. 浏览器验证：桌面悬停显示、点击切换、暗色模式、移动端窄屏点击
4. 验证通过后删除测试文章（或转为草稿）

## 明确不做（YAGNI）

- 不做 markdown-it-attrs 风格的 `{.heimu}` 语法（Goldmark 不支持，需替换渲染引擎，成本过高）
- 不做 SpoilerTags 等其它 Fandom 变体
- 不做管理后台/可视化插入按钮
