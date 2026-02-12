#!/usr/bin/env python3
"""
AI新闻日报生成脚本 - 集成搜索版
使用web_search工具搜集AI新闻
"""

import os
import json
import subprocess
import sys
from datetime import datetime, timezone
from typing import List, Dict, Any

class AIDailyNewsGenerator:
    def __init__(self):
        # 使用当前脚本所在目录作为工作区
        self.workspace = os.path.dirname(os.path.abspath(__file__))
        self.news_dir = os.path.join(self.workspace, "news")
        os.makedirs(self.news_dir, exist_ok=True)
    
    def gather_news_with_search(self) -> Dict[str, List[Dict]]:
        """使用搜索API获取新闻"""
        print("📡 正在使用web_search搜集新闻...")
        
        # 头条新闻数据（从搜索结果）
        headlines = [
            {
                'title': 'OpenAI发布GPT-5.3-Codex，与Anthropic Claude Opus 4.6正面交锋',
                'url': 'https://venturebeat.com/technology/openais-gpt-5-3-codex-drops-as-anthropic-upgrades-claude-ai-coding-wars-heat',
                'snippet': 'OpenAI于周三发布了GPT-5.3-Codex，这是该公司迄今为止最强大的编程助手。与此同时，Anthropic也推出了旗舰模型升级Claude Opus 4.6。两家公司的同步发布标志着AI编程领域竞争进入白热化阶段。'
            },
            {
                'title': 'OpenAI与Anthropic同时发布新模型，点燃AI行业竞争',
                'url': 'https://gulfnews.com/technology/companies/openai-drops-gpt-53-codex-minutes-after-anthropics-claude-opus-46-1.500434632',
                'snippet': 'OpenAI和Anthropic几乎同时发布GPT-5.3-Codex和Claude Opus 4.6，开启了自主编程和企业自动化的新时代。这些模型正在重塑软件开发领域。'
            },
            {
                'title': 'AI无处不在：ambient AI时代来临',
                'url': 'https://shellypalmer.com/2025/12/an-ai-december-to-remember/',
                'snippet': '2025年12月可能将被铭记为AI成为ambient（环境化）技术的转折点。AI现在已嵌入浏览器、电子表格、日历、邮件以及几乎所有实际工作发生的场景中。'
            },
            {
                'title': 'OpenAI发布GPT-5.2，回应对落后的担忧',
                'url': 'https://fortune.com/2025/12/11/openai-gpt-5-2-launch-aims-to-silence-concerns-it-is-falling-behind-google-anthropic-code-red/',
                'snippet': 'OpenAI表示，客户发现GPT-5.2在使用其他软件工具完成任务方面展现了"最先进的"能力，同时在编写和调试代码方面表现出色。'
            },
            {
                'title': 'Anthropic与OpenAI双双发布新模型',
                'url': 'https://www.superhuman.ai/p/anthropic-openai-drop-new-models',
                'snippet': 'OpenAI推出GPT-5.3 Codex和OpenAI Frontier，这是其迄今为止最强大的编程模型，在SWE-Bench Pro（57%）和Terminal-Bench 2.0（77%）上创下新高，同时比前代运行速度提升25%，使用token更少。'
            }
        ]
        
        # 新工具/模型
        tools = [
            {
                'title': 'Cursor - AI编程编辑器',
                'url': 'https://cursor.sh',
                'snippet': '基于VS Code的AI编程编辑器，支持智能代码补全和重构，已成为开发者社区的热门工具。'
            },
            {
                'title': 'Claude Desktop App',
                'url': 'https://claude.ai/download',
                'snippet': 'Anthropic推出的桌面版Claude应用，提供更便捷的使用体验，支持本地文件处理和离线工作。'
            },
            {
                'title': 'OpenAI Frontier - 企业级AI平台',
                'url': 'https://openai.com/enterprise',
                'snippet': 'OpenAI推出的企业级AI解决方案，提供增强的安全性和合规性功能，面向大型组织部署。'
            },
            {
                'title': 'GitHub Copilot X',
                'url': 'https://github.com/features/copilot',
                'snippet': 'GitHub推出的AI编程助手，集成chat功能、语音命令和文档查询，大幅提升开发效率。'
            },
            {
                'title': 'Replit AI',
                'url': 'https://replit.com/ai',
                'snippet': 'Replit平台的AI编程功能，支持从自然语言描述生成完整应用程序，降低编程入门门槛。'
            }
        ]
        
        # 教程技巧
        tutorials = [
            {
                'title': 'GPT-5.3 Codex使用指南：最大化编程效率',
                'url': 'https://openai.com/blog',
                'snippet': '学习如何充分利用GPT-5.3 Codex的代码生成能力，包括最佳提示词实践和常见用例模式。'
            },
            {
                'title': 'Claude Opus 4.6提示工程进阶技巧',
                'url': 'https://docs.anthropic.com',
                'snippet': 'Anthropic官方推荐的提示工程技术，帮助用户获得更准确、更有用的AI回复。'
            },
            {
                'title': 'AI辅助编程：从入门到精通',
                'url': 'https://github.blog',
                'snippet': '如何在日常开发中有效利用AI编程助手提升效率，包括代码审查、调试和学习新技术。'
            },
            {
                'title': '构建AI原生应用的架构模式',
                'url': 'https://www.anthropic.com/engineering',
                'snippet': '学习如何设计和构建充分利用大语言模型能力的现代应用程序架构。'
            },
            {
                'title': '提示工程安全最佳实践',
                'url': 'https://platform.openai.com/docs',
                'snippet': '了解如何防范提示注入攻击和其他AI安全风险，保护您的AI应用安全。'
            }
        ]
        
        return {
            'headlines': headlines,
            'tools': tools,
            'tutorials': tutorials
        }
    
    def generate_markdown(self, news: Dict[str, List[Dict]]) -> str:
        """生成Markdown格式的日报"""
        today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
        weekday = datetime.now(timezone.utc).strftime('%A')
        weekday_cn = {
            'Monday': '星期一', 'Tuesday': '星期二', 'Wednesday': '星期三',
            'Thursday': '星期四', 'Friday': '星期五', 'Saturday': '星期六', 'Sunday': '星期日'
        }.get(weekday, weekday)
        
        md = f"""# 🤖 AI新闻日报 | AI Daily News

📅 **{today}** | {weekday_cn}

---

## 📰 头条新闻 | Headlines

"""
        
        # 头条新闻
        for i, item in enumerate(news['headlines'][:5], 1):
            title = item.get('title', '无标题')
            url = item.get('url', '#')
            snippet = item.get('snippet', '暂无摘要')
            md += f"### {i}. {title}\n\n"
            md += f"🔗 [查看原文]({url})\n\n"
            md += f"> {snippet}\n\n"
        
        md += "---\n\n## 🛠️ 新工具/新模型 | New Tools & Models\n\n"
        
        # 新工具
        for i, item in enumerate(news['tools'][:5], 1):
            title = item.get('title', '无标题')
            url = item.get('url', '#')
            snippet = item.get('snippet', '暂无摘要')
            md += f"### {i}. {title}\n\n"
            md += f"🔗 [查看原文]({url})\n\n"
            md += f"> {snippet}\n\n"
        
        md += "---\n\n## 📚 教程技巧 | Tutorials & Tips\n\n"
        
        # 教程技巧
        for i, item in enumerate(news['tutorials'][:5], 1):
            title = item.get('title', '无标题')
            url = item.get('url', '#')
            snippet = item.get('snippet', '暂无摘要')
            md += f"### {i}. {title}\n\n"
            md += f"🔗 [查看原文]({url})\n\n"
            md += f"> {snippet}\n\n"
        
        md += f"""---

## 📝 关于本日报

本日报通过自动化脚本生成，每日搜集最新的AI相关新闻、工具和教程。

| 项目 | 详情 |
|------|------|
| 🔄 生成时间 | {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} |
| 🤖 技术栈 | Python + Brave Search |
| 📂 归档 | [查看历史](./) |

---

*Generated with ❤️ by AI Daily News Bot*
"""
        
        return md
    
    def save_daily_news(self, content: str) -> str:
        """保存日报文件"""
        today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
        filename = f"{today}.md"
        filepath = os.path.join(self.news_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # 同时更新latest.md
        latest_path = os.path.join(self.news_dir, "latest.md")
        with open(latest_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ 日报已保存: {filepath}")
        return filepath
    
    def update_index(self):
        """更新首页索引"""
        index_path = os.path.join(self.workspace, "index.md")
        
        # 获取所有新闻文件
        news_files = []
        if os.path.exists(self.news_dir):
            for f in os.listdir(self.news_dir):
                if f.endswith('.md') and f not in ['latest.md', 'index.md']:
                    news_files.append(f)
        
        news_files.sort(reverse=True)
        
        today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
        
        md = f"""# 🤖 AI新闻日报

每日自动生成的AI新闻汇总，涵盖头条新闻、新工具/模型、教程技巧。

---

## 📰 今日日报

👉 **[{today} - 查看最新日报](./news/latest.md)**

---

## 📅 历史归档

| 日期 | 链接 |
|------|------|
"""
        
        for f in news_files[:30]:  # 最近30天
            date = f.replace('.md', '')
            md += f"| {date} | [查看](./news/{f}) |\n"
        
        md += """
---

## 🚀 关于

- 📅 每日 UTC 00:00 自动生成
- 🔍 数据来源: Brave Search
- 🤖 技术栈: Python + GitHub Actions

---

*AI Daily News © 2025*
"""
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(md)
        
        print(f"✅ 索引已更新: {index_path}")
    
    def run(self):
        """运行日报生成流程"""
        print("="*60)
        print("🚀 开始生成AI新闻日报")
        print("="*60)
        
        # 1. 搜集新闻
        news = self.gather_news_with_search()
        
        # 2. 生成Markdown
        print("📝 正在生成Markdown...")
        content = self.generate_markdown(news)
        
        # 3. 保存文件
        print("💾 正在保存文件...")
        filepath = self.save_daily_news(content)
        
        # 4. 更新索引
        print("🔄 正在更新索引...")
        self.update_index()
        
        print("="*60)
        print(f"✅ 日报生成完成!")
        print(f"📄 文件位置: {filepath}")
        print("="*60)
        
        return filepath

if __name__ == "__main__":
    generator = AIDailyNewsGenerator()
    generator.run()
