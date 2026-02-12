#!/bin/bash
# 更新 GitHub Token 脚本
# 使用方法: ./update-token.sh ghp_你的新token

NEW_TOKEN="$1"
if [ -z "$NEW_TOKEN" ]; then
    echo "请提供新的 GitHub Token"
    echo "示例: ./update-token.sh ghp_xxxxx"
    exit 1
fi

cd /root/.openclaw/workspace/ai-news-daily
# 更新远程 URL 使用新 token
git remote set-url origin "https://royelau76:${NEW_TOKEN}@github.com/royelau76/ai-news-daily.git"
echo "Token 已更新！"

# 尝试推送
git push -u origin main
