# AI新闻日报 - GitHub部署指南

## 🚀 快速部署步骤

### 1. 在GitHub创建仓库
访问：https://github.com/new
- **Repository name**: `ai-news-daily`
- 勾选 ✅ **Add a README file**
- 点击 **Create repository**

### 2. 克隆并复制代码

```bash
# 克隆你的新仓库
git clone https://github.com/royelau76/ai-news-daily.git
cd ai-news-daily

# 复制本地代码到这里
cp -r /root/.openclaw/workspace/ai-news-daily/* .
```

### 3. 提交并推送

```bash
# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: AI News Daily System"

# 推送
git push origin main
```

### 4. 启用GitHub Pages

1. 访问：`https://github.com/royelau76/ai-news-daily/settings/pages`
2. **Build and deployment** → **Source**
3. 选择 **GitHub Actions**
4. 点击 **Save**

### 5. 验证部署

- 等待Actions运行完成（约2-3分钟）
- 访问：`https://royelau76.github.io/ai-news-daily/`

---

## ⚡ 一键部署脚本

复制以下命令在本地终端运行：

```bash
# 创建并进入目录
mkdir -p ~/ai-news-daily && cd ~/ai-news-daily

# 克隆仓库
git clone https://github.com/royelau76/ai-news-daily.git .

# 从服务器复制最新代码
rsync -avz root@你的服务器IP:/root/.openclaw/workspace/ai-news-daily/ .

# 提交并推送
git add .
git commit -m "Update: AI News Daily System"
git push origin main

echo "✅ 部署完成！"
echo "访问地址: https://royelau76.github.io/ai-news-daily/"
```

---

## 📁 本地代码位置

服务器上的代码已准备就绪：
```
/root/.openclaw/workspace/ai-news-daily/
├── news/2026-02-11.md       # 今日日报
├── generate_daily.py         # 日报生成脚本
├── .github/workflows/        # GitHub Actions
└── ...
```

---

## 🔧 配置完成后的效果

- ✅ 每天早上9点自动生成日报
- ✅ 飞书推送提醒
- ✅ GitHub Pages在线访问
- ✅ 历史日报归档

---

🦞 **Powered by OpenClaw**
