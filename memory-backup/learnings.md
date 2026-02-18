# 🧠 学习总结与踩坑记录

> 基于 3-file pattern 的知识积累
> 核心原则：Log ALL Errors | 读取成本 < 重新发现成本

---

## 💡 重要发现 (Findings)

### [F-001] GitHub Actions 部署静态网站的正确姿势
**发现时间**: 2026-02-12
**场景**: AI新闻日报 GitHub Pages 部署

**关键点**:
1. **禁用 Jekyll**: 添加 `.nojekyll` 文件避免构建问题
2. **Source 设置**: 必须选择 "Deploy from a branch" 而不是 GitHub Actions
3. **index.html**: 根目录必须存在，不能只有 index.md

**参考**:
- 仓库: https://github.com/Royelau76/ai-news-daily

---

### [F-002] OpenClaw 定时任务配置要点
**发现时间**: 2026-02-12
**场景**: 配置 AI日报和记忆备份的 cron 任务

**关键点**:
1. **sessionTarget**: 飞书推送必须用 `"isolated"`，`"main"` 不支持完整 message 功能
2. **delivery.to**: 必须指定 `user:open_id` 格式
3. **systemEvent vs agentTurn**: 简单通知用 systemEvent，复杂任务用 agentTurn

---

### [F-003] 3-File Pattern 记忆管理法
**发现时间**: 2026-02-12
**来源**: MyloreAgent @ moltbook.com

**核心原则**:
| 原则 | 说明 |
|------|------|
| Read Before Decide | 重大决策前重读计划文件 |
| 2-Action Rule | 每做2个操作保存一次发现 |
| Log ALL Errors | 所有错误都记录，防止重复踩坑 |

**文件分工**:
- `task_plan.md` → 记"要做什么"
- `findings.md` → 记"发现了什么"
- `progress.md` → 记"做了什么" (对应我们的 memory/YYYY-MM-DD.md)

---

## ⚠️ 错误记录 (Errors)

### [E-001] GitHub Token 缺少 workflow 权限
**错误时间**: 2026-02-12
**错误信息**: `refusing to allow a Personal Access Token to create or update workflow`

**原因**: Token 没有 `workflow` scope，无法推送 `.github/workflows/` 文件

**解决**: 重新生成 Token，勾选 `workflow` 权限

---

### [E-002] Git Push 冲突 (non-fast-forward)
**错误时间**: 2026-02-12
**错误信息**: `! [rejected] main -> main (fetch first)`

**解决步骤**:
```bash
git pull origin main --no-rebase --no-edit
git push
```

---

### [E-003] Python 脚本路径问题
**错误时间**: 2026-02-12
**错误信息**: `PermissionError: [Errno 13] Permission denied: '/root/.openclaw'`

**原因**: GitHub Actions 中使用绝对路径，但 runner 上没有该路径

**解决**: 改用相对路径 `os.path.dirname(os.path.abspath(__file__))`

---

## 🎓 最佳实践 (Best Practices)

### BP-001: 宠物挑食处理
**适用对象**: 十一（贵宾犬，8岁）

**有效方法**:
1. 小份量多餐（分成3-4份）
2. 手喂建立信任
3. 漏食玩具增加进食乐趣
4. 严格执行"不吃完不补"

**避免**:
- ❌ 频繁换粮/加料（会惯坏）
- ❌ 人食剩饭（太咸）
- ❌ 心软给零食（破坏规律）

---

## 🔗 有用的资源

| 资源 | 链接 | 用途 |
|------|------|------|
| AI日报网站 | https://royelau76.github.io/ai-news-daily/ | 每日AI新闻 |
| GitHub 仓库 | https://github.com/Royelau76/ai-news-daily | 代码和备份 |
| OpenClaw 文档 | https://docs.openclaw.ai | 官方文档 |
| moltbook | https://moltbook.com | AI Agent 社区 |

---

## ⚠️ 踩坑记录 (Mistakes)

### [M-001] 备份脚本漏掉 3-file pattern 文件
**发现时间**: 2026-02-13
**场景**: 记忆文件自动备份

**问题**:
- 重构 MEMORY.md 为 3-file pattern (tasks.md, learnings.md, decisions.md)
- 但 backup-memory.sh 脚本只备份了旧的 6 个文件
- 导致新结构下的重要记忆文件没有备份

**解决**:
```bash
# 在备份脚本中新增
# 2. 3-file pattern 记忆文件
cp -v "$SOURCE_DIR/tasks.md" "$BACKUP_DIR/" 
cp -v "$SOURCE_DIR/learnings.md" "$BACKUP_DIR/" 
cp -v "$SOURCE_DIR/decisions.md" "$BACKUP_DIR/"
```

**教训**: 重构文件结构后，记得同步更新备份脚本！

---

*最后更新: 2026-02-13 10:20*
