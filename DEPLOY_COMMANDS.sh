#!/bin/bash
# AI新闻日报 - 精确部署命令
# GitHub: royelau76 / 邮箱: royelau@hotmail.com

echo "======================================"
echo "🚀 AI新闻日报 GitHub 精确部署命令"
echo "======================================"
echo ""

# 方案1: 使用GitHub Token直接推送（服务器上执行）
echo "【方案一】服务器直接推送（需要GitHub Token）"
echo "--------------------------------------"
echo ""
echo "步骤1: 在GitHub生成Token"
echo "  访问: https://github.com/settings/tokens"
echo "  点击: Generate new token (classic)"
echo "  勾选: repo (完整仓库权限)"
echo "  复制生成的token"
echo ""
echo "步骤2: 在服务器上运行以下命令:"
echo ""
echo "  cd /root/.openclaw/workspace/ai-news-daily"
echo "  git remote set-url origin https://royelau76:你的TOKEN@github.com/royelau76/ai-news-daily.git"
echo "  git push -u origin main"
echo ""
echo "  # 推送完成后，移除token（安全）"
echo "  git remote set-url origin https://github.com/royelau76/ai-news-daily.git"
echo ""

# 方案2: 本地推送（推荐）
echo "【方案二】本地电脑推送（更安全）"
echo "--------------------------------------"
echo ""
echo "步骤1: 在GitHub创建仓库"
echo "  访问: https://github.com/new"
echo "  仓库名: ai-news-daily"
echo "  勾选: Add a README file"
echo "  点击: Create repository"
echo ""
echo "步骤2: 在本地电脑上运行:"
echo ""
cat << 'LOCAL_COMMANDS'
# 创建目录
mkdir -p ~/ai-news-daily
cd ~/ai-news-daily

# 克隆仓库
git clone https://github.com/royelau76/ai-news-daily.git .

# 从服务器复制代码（将下面IP替换为你的服务器IP）
scp -r root@43.134.162.137:/root/.openclaw/workspace/ai-news-daily/* .

# 或者手动复制服务器上的这些文件:
# - generate_daily.py
# - index.md
# - README.md
# - _config.yml
# - .github/workflows/generate.yml
# - news/2026-02-11.md

# 配置Git
git config user.name "royelau76"
git config user.email "royelau@hotmail.com"

# 添加并提交
git add .
git commit -m "Initial commit: AI News Daily System"

# 推送
git push origin main

# 完成后访问:
# https://github.com/royelau76/ai-news-daily/settings/pages
# 启用 GitHub Actions
LOCAL_COMMANDS

echo ""
echo "步骤3: 启用GitHub Pages"
echo "  访问: https://github.com/royelau76/ai-news-daily/settings/pages"
echo "  Source → GitHub Actions → Save"
echo ""
echo "步骤4: 访问你的日报"
echo "  https://royelau76.github.io/ai-news-daily/"
echo ""
echo "======================================"
