#!/bin/bash
# AI新闻日报 - 一键部署脚本
# 运行前请确保已安装 git

set -e

GITHUB_USER="royelau76"
REPO_NAME="ai-news-daily"
EMAIL="royelau@hotmail.com"

echo "🚀 AI新闻日报 GitHub 一键部署"
echo "================================"
echo ""

# 检查git
if ! command -v git &> /dev/null; then
    echo "❌ 请先安装 Git: https://git-scm.com/downloads"
    exit 1
fi

# 创建临时目录
TEMP_DIR=$(mktemp -d)
cd "$TEMP_DIR"

echo "📦 步骤1: 克隆GitHub仓库..."
git clone "https://github.com/$GITHUB_USER/$REPO_NAME.git" 2>/dev/null || {
    echo "⚠️  仓库不存在，请先创建:"
    echo "   访问: https://github.com/new"
    echo "   仓库名: $REPO_NAME"
    echo "   勾选 'Add a README file'"
    exit 1
}

cd "$REPO_NAME"

echo "📥 步骤2: 下载最新代码..."
# 从服务器下载代码
curl -sL "https://raw.githubusercontent.com/$GITHUB_USER/$REPO_NAME/main/deploy-files.sh" -o /tmp/deploy-files.sh 2>/dev/null || true

# 如果curl失败，提示手动复制
echo ""
echo "⚠️  请手动复制服务器上的代码文件到当前目录:"
echo "   服务器路径: /root/.openclaw/workspace/ai-news-daily/"
echo "   本地路径: $(pwd)"
echo ""
echo "   复制命令示例:"
echo "   scp -r root@你的服务器IP:/root/.openclaw/workspace/ai-news-daily/* ."
echo ""
read -p "按回车键继续 (确保文件已复制)..."

echo "📄 步骤3: 配置Git..."
git config user.name "$GITHUB_USER"
git config user.email "$EMAIL"

echo "💾 步骤4: 提交代码..."
git add .
git commit -m "Initial commit: AI News Daily System - $(date +%Y-%m-%d)" || echo "已是最新"

echo "⬆️  步骤5: 推送到GitHub..."
git push origin main

echo ""
echo "✅ 代码推送成功!"
echo ""
echo "🔧 步骤6: 启用GitHub Pages..."
echo "   访问: https://github.com/$GITHUB_USER/$REPO_NAME/settings/pages"
echo "   Source → GitHub Actions → Save"
echo ""
echo "🌐 部署完成后访问:"
echo "   https://$GITHUB_USER.github.io/$REPO_NAME/"
echo ""

# 清理
cd /
rm -rf "$TEMP_DIR"

echo "🎉 部署完成！"
