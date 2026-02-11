#!/bin/bash
# GitHub部署脚本

echo "🚀 开始部署AI日报到GitHub Pages..."

# 检查是否已初始化
if [ ! -d .git ]; then
    echo "📦 初始化Git仓库..."
    git init
fi

# 配置Git（如果需要）
# git config user.name "你的GitHub用户名"
# git config user.email "你的邮箱"

echo "📄 添加文件..."
git add .

echo "💾 提交代码..."
git commit -m "Initial commit: AI News Daily System - $(date +%Y-%m-%d)"

echo ""
echo "🔗 请执行以下命令完成部署："
echo ""
echo "1. 在GitHub创建仓库: https://github.com/new"
echo "   仓库名: ai-news-daily"
echo ""
echo "2. 然后运行:"
echo "   git remote add origin https://github.com/你的用户名/ai-news-daily.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. 启用GitHub Pages:"
echo "   仓库 → Settings → Pages → Source → GitHub Actions"
echo ""
