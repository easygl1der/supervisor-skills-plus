<div align="center">

<img src="assets/icon.png" alt="sv-skills" height="240" />

</div>

# sv-skills：Yihua Yue 的学术科研技能库

[English](README.en.md) · 中文

面向 Claude Code、Cursor、Codex 的 **Agent Skills**：十二个 `sv-*` 组，外加共享的 `research-core`（规则、领域与会议 profile、带出处的 checklist）。每组一个可被自动选中的总入口，加若干只能点名的子命令，例如 `/sv-write-polish`。

维护者：[Yihua Yue](https://github.com/easygl1der)（`easygl1der`）。仓库：[`easygl1der/supervisor-skills-plus`](https://github.com/easygl1der/supervisor-skills-plus)。

这是一份独立维护的技能包，不是 HKUSTDial/Supervisor-Skills（港科广 DIAL / SuperY）的产品页或官方 fork 展示。技能所引用的手册与部分早期流程仍保留出处，见 [THIRD_PARTY.md](THIRD_PARTY.md) 与 [`handbook/README.md`](handbook/README.md)。

从本地 clone 安装见 [INSTALL.md](INSTALL.md)，使用指南见 [skills/README.md](skills/README.md)，分组决定见 [docs/adr/0021-sv-skill-groups.md](docs/adr/0021-sv-skill-groups.md)。

<p align="center">
  <a href="https://github.com/easygl1der/supervisor-skills-plus/stargazers"><img src="https://img.shields.io/github/stars/easygl1der/supervisor-skills-plus?style=flat-square&logo=github" alt="GitHub stars"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey?style=flat-square" alt="License"></a>
</p>

## 仓库结构

```
supervisor-skills-plus/
├── skills/              # 可安装的 Agent Skills（核心）
│   ├── sv-supervisor/ … sv-slides/
│   └── research-core/
├── handbook/            # 中文课程（技能引用的来源材料，见该目录 README）
├── handbook-en/         # 英文镜像
├── notes/               # 被 research-core 引用的证据笔记
├── docs/adr/            # 本库自己的决策记录
└── scripts/             # 安装与 lint
```

## Skills

| 组 | 覆盖什么 | 链接 |
|---|---|---|
| **sv-supervisor** | 会话简报与路由、项目初始化、STATUS / TODO / ADR / 日志、经验沉淀进 research-core | [打开](skills/sv-supervisor/SKILL.md) |
| **sv-quickread** | 一篇论文的九段式五分钟速读卡；可选风格卡 | [打开](skills/sv-quickread/SKILL.md) |
| **sv-study** | 理解优先地学一个概念、一篇论文或一章教材：复述、诊断、纠正；接回项目 | [打开](skills/sv-study/SKILL.md) |
| **sv-idea** | 完整的 idea 评估（五维、生命周期、范式探针），或只做致命缺陷早筛 | [打开](skills/sv-idea/SKILL.md) |
| **sv-litreview** | 综述级文献调研、逐条核验引用；或已读文献地图 | [打开](skills/sv-litreview/SKILL.md) |
| **sv-proposal** | 开题报告、基金申请（NSFC、NSF、ERC、NIH）、研究陈述 | [打开](skills/sv-proposal/SKILL.md) |
| **sv-experiment** | 冻结输入、运行日志、数字可追溯进论文、复现包 | [打开](skills/sv-experiment/SKILL.md) |
| **sv-write** | 骨架、Introduction、各节正文、润色、中译英、只挑毛病、按论文/报告/幻灯片/信件去 AI 味、期刊风格 | [打开](skills/sv-write/SKILL.md) |
| **sv-figure** | 作图设计、draw.io 重建、代码画图、TikZ、HTML、海报、讲解图 | [打开](skills/sv-figure/SKILL.md) |
| **sv-review** | 只读的投稿前终审，或有轮数上限的多轮检查 | [打开](skills/sv-review/SKILL.md) |
| **sv-feedback** | 意见逐条修改并核实、专家指导记录、rebuttal 规划 | [打开](skills/sv-feedback/SKILL.md) |
| **sv-slides** | 组会 Beamer：周报或论文讲解 | [打开](skills/sv-slides/SKILL.md) |
| **research-core** | 共享规则、领域与会议 profile、checklist、AI 协作守则、模板（不是命令） | [打开](skills/research-core/SKILL.md) |

## 快速开始

```
git clone https://github.com/easygl1der/supervisor-skills-plus.git
```

然后按 [INSTALL.md](INSTALL.md) 把 `skills/` 链到 Claude Code / Cursor / Codex。也可以把这段发给助手：

```
Help me install the skills from https://github.com/easygl1der/supervisor-skills-plus (see INSTALL.md).
```

## 手册

`handbook/` 与 `handbook-en/` 是技能 checklist 与领域规则仍在引用的课程材料（CC BY-NC-SA 4.0）。它们**不是**本仓库的对外品牌；如何引用见 [`handbook/README.md`](handbook/README.md)。

## 贡献

欢迎 Issue 与 PR。约定见 [CONTRIBUTING.md](CONTRIBUTING.md)。改动走 PR 合入 `main`，不 force-push。

## License

本仓库采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)。第三方代码与手册出处见 [THIRD_PARTY.md](THIRD_PARTY.md) 与 [LICENSE](LICENSE)。

## Plugin

`/plugin install sv-skills --marketplace easygl1der/supervisor-skills-plus` (Claude Code); Cursor and Codex: see [INSTALL.md](INSTALL.md).
