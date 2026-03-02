---
tags: [learnings, config]
updated: 2026-02-24
---

# 🧠 学习与决策记录

> 知识积累 + 重大决策
> 原则：Log ALL Errors | Read Before Decide

---

## 🎯 重要决策

### [D-001] 采用 3-File Pattern 记忆管理
**时间**: 2026-02-12 | **状态**: ✅ 已实施

重构记忆系统：
- `memory/YYYY-MM-DD.md` - 每日进展
- `MEMORY.md` - 长期记忆筛选
- 专题文件（如 `高考记忆_2026.md`）

### [D-002] AI新闻日报用静态HTML
**时间**: 2026-02-12 | **状态**: ✅ 已实施

GitHub Pages 部署，禁用 Jekyll，直接服务 HTML

### [D-003] 记忆文件每日自动备份
**时间**: 2026-02-12 | **状态**: ⏸️ 待修复API Key

### [D-004] 十一挑食纠正方案
**时间**: 2026-02-12 | **状态**: 🐶 进行中

小份量多餐 + 手喂 + 漏食玩具

---

## 💡 关键发现

### GitHub Actions 部署
- 加 `.nojekyll` 禁用 Jekyll
- Source 选 "Deploy from a branch"
- 根目录必须有 `index.html`

### OpenClaw 定时任务
- 飞书推送用 `sessionTarget: "isolated"`
- `delivery.to` 格式: `user:open_id`

### 3-File Pattern 核心
| 原则 | 说明 |
|------|------|
| Read Before Decide | 决策前重读记录 |
| 2-Action Rule | 每2个操作保存一次 |
| Log ALL Errors | 所有错误都记录 |

---

## ⚠️ 错误记录

| 编号 | 问题 | 解决 |
|------|------|------|
| E-001 | GitHub Token 缺 workflow 权限 | 重新生成 Token |
| E-002 | Git push 冲突 | `git pull --no-rebase` |
| E-003 | Python 绝对路径问题 | 改用相对路径 |
| M-001 | 备份脚本漏新文件 | 同步更新备份范围 |

---

## 🎓 最佳实践

### 宠物挑食 (十一)
✅ 小份量多餐、手喂、漏食玩具  
❌ 频繁换粮、人食剩饭、心软给零食

---

## 🔗 常用链接

- AI日报: https://royelau76.github.io/ai-news-daily/
- GitHub: https://github.com/Royelau76/ai-news-daily
- OpenClaw文档: https://docs.openclaw.ai
