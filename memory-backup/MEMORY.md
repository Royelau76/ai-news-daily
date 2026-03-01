# 🧠 长期记忆总库

> 采用 3-file pattern 管理记忆
> 本文档作为总索引，详细内容分散在专用文件中

---

## 📁 记忆文件结构（2026-02-24 更新）

| 文件 | 用途 | 更新频率 |
|------|------|----------|
| [CONFIG.md](./CONFIG.md) | 配置、操作指南、决策记录 | 有变更时 |
| [learnings.md](./learnings.md) | 学习总结、踩坑记录、决策 | 有新发现时 |
| [memory/YYYY-MM-DD.md](./memory/) | 每日进展（保留7天） | 每天 |
| [memory/专题.md](./memory/) | 专题记忆（高考、项目等） | 专题相关时 |

**归档机制**: 每周日将7天记忆合并为周总结，删除原始日文件

**核心原则**: Read Before Decide | 2-Action Rule | Log ALL Errors

---

## 👤 关于我

详见 [IDENTITY.md](./IDENTITY.md) 和 [SOUL.md](./SOUL.md)

- **名字**: 小莫
- **身份**: AI 助手
- **特点**: 靠谱但会开玩笑的搭档

---

## 👤 关于瑞哥

详见 [USER.md](./USER.md)

- **称呼**: 瑞哥
- **所在地**: 昆明
- **子女**: 儿子2026年参加高考（目标：南方科技大学）
- **宠物**: 十一（贵宾犬，2017年7月23日生）

---

## 🛠️ 工具配置

详见 [CONFIG.md](./CONFIG.md)

---

## 🔄 自动备份

所有记忆文件每天 10:00 自动备份到 GitHub:
https://github.com/Royelau76/ai-news-daily/tree/main/memory-backup/

---

## 📝 快速参考

### 当前活跃任务
1. AI新闻日报系统 - 每日20:00自动推送 ✅
2. 记忆文件自动备份 - 每天10:00执行 ⏳
3. 十一挑食纠正 - 已解决 🐶

### RSS日报系统配置（2026-02-28更新）
- **定时任务**: 每天20:00自动生成并推送
- **模型**: Kimi K2.5 + Gemini 2.5 Flash fallback
- **信息源**: 12个中文AI媒体
- **分类**: 6大分类体系
- **格式**: 详细版（Top3摘要+分类统计）

### 最近重要发现
- 3-file pattern 记忆管理法（MyloreAgent）
- GitHub Pages 部署需禁用 Jekyll
- OpenClaw 定时任务配置要点
- Gemini 2.5 Flash 已更新

### 最近踩的坑
- GitHub Token 需要 workflow 权限
- Python 脚本要用相对路径
- 飞书推送要用 isolated session
- 上下文76%时需要考虑reset

---

*采用 3-file pattern 重构于 2026-02-12*
