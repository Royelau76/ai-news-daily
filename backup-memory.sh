#!/bin/bash
# 记忆文件备份脚本
# 每天自动备份记忆文件到 GitHub

set -e

# 配置
SOURCE_DIR="/root/.openclaw/workspace"
BACKUP_DIR="/root/.openclaw/workspace/ai-news-daily/memory-backup"
DATE=$(date +'%Y-%m-%d')
TIME=$(date +'%H:%M:%S')

echo "🚀 开始备份记忆文件..."
echo "📅 时间: $DATE $TIME"

# 创建备份目录
mkdir -p "$BACKUP_DIR"

# 备份文件列表
echo "📁 备份以下文件:"

# 1. 核心记忆文件
cp -v "$SOURCE_DIR/MEMORY.md" "$BACKUP_DIR/" 2>/dev/null || echo "⚠️ MEMORY.md 不存在"
cp -v "$SOURCE_DIR/IDENTITY.md" "$BACKUP_DIR/" 2>/dev/null || echo "⚠️ IDENTITY.md 不存在"
cp -v "$SOURCE_DIR/USER.md" "$BACKUP_DIR/" 2>/dev/null || echo "⚠️ USER.md 不存在"
cp -v "$SOURCE_DIR/SOUL.md" "$BACKUP_DIR/" 2>/dev/null || echo "⚠️ SOUL.md 不存在"
cp -v "$SOURCE_DIR/AGENTS.md" "$BACKUP_DIR/" 2>/dev/null || echo "⚠️ AGENTS.md 不存在"
cp -v "$SOURCE_DIR/TOOLS.md" "$BACKUP_DIR/" 2>/dev/null || echo "⚠️ TOOLS.md 不存在"

# 2. 记忆目录下的每日文件
if [ -d "$SOURCE_DIR/memory" ]; then
    echo "📂 备份 memory/ 目录..."
    cp -r "$SOURCE_DIR/memory/"* "$BACKUP_DIR/" 2>/dev/null || true
fi

# 3. 创建备份记录
cat > "$BACKUP_DIR/README.md" << EOF
# 🧠 记忆文件备份

## 📅 最新备份

- **日期**: $DATE
- **时间**: $TIME
- **来源**: /root/.openclaw/workspace

## 📁 备份内容

| 文件 | 说明 |
|------|------|
| MEMORY.md | 长期记忆、重要事件 |
| IDENTITY.md | AI身份配置 |
| USER.md | 用户信息 |
| SOUL.md | 核心人格 |
| AGENTS.md | 代理配置 |
| TOOLS.md | 工具配置 |

## 🔄 自动备份

- **频率**: 每天
- **时间**: 自动执行
- **方式**: GitHub Actions / Cron

---
*自动生成的备份记录*
EOF

echo ""
echo "✅ 备份完成!"
echo "📂 备份位置: $BACKUP_DIR"
echo ""

# GitHub 推送部分（如果配置了git）
cd /root/.openclaw/workspace/ai-news-daily

if [ -d ".git" ]; then
    echo "🔄 推送到 GitHub..."
    git add memory-backup/
    git commit -m "🧠 Memory backup: $DATE $TIME" || echo "⚠️ 没有新变更需要提交"
    git push origin main || echo "⚠️ 推送失败，请检查git配置"
    echo "✅ 推送完成!"
else
    echo "⚠️ 不是git仓库，跳过推送"
fi

echo ""
echo "🎉 备份流程结束!"
