# 三义漫剧 AI 编程助手插件（Claude Code / Codex / Kimi Code 通用）

> ⚠️ 本仓库公开发布写作规则。不要把真实剧本、客户资料或密钥提交到本仓库。

| 插件 | 版本 | 用途 |
|---|---|---|
| `sanyi-manhua-writing` | 2.2.1 | 剧本**写作线**：写/续写/改稿、分集大纲、人设、钩子与集尾卡点、项目初始化。**不含评分**。 |

评审线（评分 SOP）尚未拆分发布，暂不在本仓库。

三个工具共用**同一份** `SKILL.md` 和参考文件，只是各自有自己的插件清单。改规则只需改一处。

---

## 安装

以下命令已填写本仓库地址。

### Claude Code

```
/plugin marketplace add ronalluotoufang-gif/-V2.2
/plugin install sanyi-manhua-writing@sanyi-manhua
```

建议在 `/plugin` → Marketplaces 中开启自动更新。

### Codex

```
codex plugin marketplace add ronalluotoufang-gif/-V2.2
codex plugin add sanyi-manhua-writing@sanyi-manhua
```

之后更新：`codex plugin marketplace upgrade sanyi-manhua`。安装或更新后重启 Codex。

### Kimi Code

在 Kimi Code 的对话里运行：

```
/plugins install https://github.com/ronalluotoufang-gif/-V2.2
/reload
```

⚠️ Kimi Code 从 GitHub 安装时不经过 GitHub 登录，**私有仓库大概率无法用这种方式安装**，请改用下面的"手动安装"。

### 手动安装（任何工具都适用，私有仓库推荐）

先运行 `git clone https://github.com/ronalluotoufang-gif/-V2.2.git`，进入克隆目录，然后：

- macOS / Linux：`bash install.sh`
- Windows：`powershell -ExecutionPolicy Bypass -File install.ps1`

脚本会把 skill 复制到 `~/.claude/skills/`（Claude Code）和 `~/.agents/skills/`（Codex 与 Kimi Code 共用）。更新时 `git pull` 后再运行一次即可。

### Claude.ai 网页版 / Claude Desktop

把 `plugins/sanyi-manhua-writing/skills/sanyi-manhua-writing/` 打包成 zip，在 设置 → Capabilities → Skills 上传。

---

## 使用

| 工具 | 手动调用 | 自动触发 |
|---|---|---|
| Claude Code | `/sanyi-manhua-writing` | 说"写第 3 集""改这场戏"等 |
| Codex | `$sanyi-manhua-writing` | 同上 |
| Kimi Code | `/skill:sanyi-manhua-writing` | 同上 |

1. **新项目**：说"用 sanyi-manhua-writing 初始化一个新漫剧项目"，它会把项目模板复制到你指定的目录。
2. 先填好项目根目录的 `AGENTS.md`、`01-设定/`、`03-大纲/分集大纲.md`。
3. 每集一个新会话："用 sanyi-manhua-writing，读本目录 AGENTS.md，按开工流程写 EPxx"。

**关于项目说明文件**：项目模板里 `AGENTS.md` 是正本，Codex 和 Kimi Code 直接读取；`CLAUDE.md` 只有一行 `@AGENTS.md`，让 Claude Code 也读到同一份内容。只改 `AGENTS.md`。

---

## 目录结构

```
.claude-plugin/marketplace.json            ← Claude Code 市场清单
.agents/plugins/marketplace.json           ← Codex 市场清单
kimi.plugin.json                           ← Kimi Code 插件清单
plugins/sanyi-manhua-writing/
  .claude-plugin/plugin.json               ← Claude Code 插件清单
  .codex-plugin/plugin.json                ← Codex 插件清单
  skills/sanyi-manhua-writing/             ← 三个工具共用的 skill 本体
    SKILL.md
    references/
    assets/项目模板/
install.sh / install.ps1                   ← 手动安装脚本
scripts/check_versions.py                  ← 发布前检查三套清单版本是否一致
CHANGELOG.md
```

---

## 更新规则的流程

1. 修改 `SKILL.md` 或 `references/` 下的文件。
2. 实质变化时在 `CHANGELOG.md` 登记。
3. **把三个清单里的 `version` 改成同一个新版本号**：
   - `plugins/sanyi-manhua-writing/.claude-plugin/plugin.json`
   - `plugins/sanyi-manhua-writing/.codex-plugin/plugin.json`
   - `kimi.plugin.json`
4. 运行 `python3 scripts/check_versions.py`，确认显示"三套清单一致"。
5. 提交并推送。

不改版本号的话，Claude Code 和 Codex 那边不会推送更新。
