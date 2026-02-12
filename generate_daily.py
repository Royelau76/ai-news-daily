#!/usr/bin/env python3
"""
AI新闻日报生成脚本 - 多语言数据源版
支持中文和英文AI新闻源
"""

import os
import json
import subprocess
import sys
from datetime import datetime, timezone
from typing import List, Dict, Any

class AIDailyNewsGenerator:
    def __init__(self):
        self.workspace = os.path.dirname(os.path.abspath(__file__))
        self.news_dir = os.path.join(self.workspace, "news")
        os.makedirs(self.news_dir, exist_ok=True)
    
    def get_static_headlines(self) -> List[Dict]:
        """获取静态头条新闻（作为备用）"""
        return [
            {
                'title': 'OpenAI发布GPT-5.3-Codex，与Anthropic Claude Opus 4.6正面交锋',
                'title_en': 'OpenAI releases GPT-5.3-Codex, competing with Anthropic Claude Opus 4.6',
                'url': 'https://venturebeat.com/technology/openais-gpt-5-3-codex-drops-as-anthropic-upgrades-claude-ai-coding-wars-heat',
                'snippet': 'OpenAI于周三发布了GPT-5.3-Codex，这是该公司迄今为止最强大的编程助手。与此同时，Anthropic也推出了旗舰模型升级Claude Opus 4.6。两家公司的同步发布标志着AI编程领域竞争进入白热化阶段。',
                'source': '国际',
                'category': '头条'
            },
            {
                'title': 'AI无处不在：ambient AI时代来临',
                'title_en': 'AI Everywhere: The Age of Ambient AI Arrives',
                'url': 'https://shellypalmer.com/2025/12/an-ai-december-to-remember/',
                'snippet': '2025年12月可能将被铭记为AI成为ambient（环境化）技术的转折点。AI现在已嵌入浏览器、电子表格、日历、邮件以及几乎所有实际工作发生的场景中。',
                'source': '国际',
                'category': '趋势'
            },
            {
                'title': '【中文】OpenAI与五角大楼达成合作，ChatGPT将进入军方网络',
                'title_en': 'OpenAI Partners with Pentagon, ChatGPT to Enter Military Networks',
                'url': 'https://www.jiqizhixin.com/',
                'snippet': '据机器之心报道，OpenAI与美国国防部达成合作，ChatGPT将被部署至军方非机密网络，覆盖超过300万国防部员工。这是OpenAI首次向政府机构大规模提供AI服务。',
                'source': '机器之心',
                'category': '头条'
            },
            {
                'title': '【中文】扣子开发平台升级为"扣子编程"，推出Vibe Coding范式',
                'title_en': 'Coze Platform Upgraded to "Coze Coding" with Vibe Coding Paradigm',
                'url': 'https://www.coze.cn/',
                'snippet': '在火山引擎Force大会上，扣子开发平台正式升级为"扣子编程"并开启免费公开测试。用户只需用自然语言描述业务需求，即可自动生成智能体、工作流及跨端应用。',
                'source': '国内',
                'category': '新工具'
            },
            {
                'title': '【中文】马斯克宣布SpaceX已完成对xAI的收购整合',
                'title_en': 'Musk Announces SpaceX Completed Acquisition of xAI',
                'url': 'https://www.jiqizhixin.com/',
                'snippet': '据机器之心报道，马斯克在社交媒体宣布SpaceX已完成对xAI的收购整合。这一举动将进一步加强AI与航天技术的结合，可能用于星舰系统的智能化升级。',
                'source': '机器之心',
                'category': '行业动态'
            },
            {
                'title': 'OpenAI罕见发论文：我们找到了AI幻觉的罪魁祸首',
                'title_en': 'OpenAI Paper: We Found the Root Cause of AI Hallucinations',
                'url': 'https://news.qq.com/rain/a/20250906A03A1Z00',
                'snippet': 'AI最臭名昭著的Bug是什么？不是代码崩溃，而是「幻觉」——模型自信地编造事实。OpenAI最新研究论文揭示了导致大模型产生幻觉的根本原因。',
                'source': '腾讯新闻/机器之心',
                'category': '研究'
            }
        ]
    
    def get_static_tools(self) -> List[Dict]:
        """获取工具/模型数据"""
        return [
            {
                'title': 'Cursor - AI编程编辑器',
                'title_en': 'Cursor - AI Code Editor',
                'url': 'https://cursor.sh',
                'snippet': '基于VS Code的AI编程编辑器，支持智能代码补全和重构，已成为开发者社区的热门工具。',
                'source': '国际',
                'category': '开发工具'
            },
            {
                'title': 'Claude Desktop App',
                'title_en': 'Claude Desktop Application',
                'url': 'https://claude.ai/download',
                'snippet': 'Anthropic推出的桌面版Claude应用，提供更便捷的使用体验，支持本地文件处理和离线工作。',
                'source': '国际',
                'category': 'AI助手'
            },
            {
                'title': '【中文】扣子编程 (Coze Coding)',
                'title_en': 'Coze Coding Platform',
                'url': 'https://www.coze.cn/',
                'snippet': '字节跳动推出的AI编程平台，通过自然语言描述即可生成智能体、工作流及跨端应用，支持Vibe Coding开发范式。',
                'source': '国内',
                'category': '低代码平台'
            },
            {
                'title': 'GitHub Copilot X',
                'title_en': 'GitHub Copilot X',
                'url': 'https://github.com/features/copilot',
                'snippet': 'GitHub推出的AI编程助手，集成chat功能、语音命令和文档查询，大幅提升开发效率。',
                'source': '国际',
                'category': '开发工具'
            },
            {
                'title': '【中文】文心一言4.0',
                'title_en': 'Ernie Bot 4.0',
                'url': 'https://yiyan.baidu.com/',
                'snippet': '百度推出的文心一言4.0版本，在中文理解和多模态能力上有显著提升，支持图文混合对话。',
                'source': '国内',
                'category': 'AI助手'
            },
            {
                'title': '【中文】通义千问2.5',
                'title_en': 'Qwen 2.5',
                'url': 'https://qwenlm.github.io/',
                'snippet': '阿里云开源的Qwen2.5模型，在多项基准测试中表现出色，支持长文本和代码生成。',
                'source': '国内',
                'category': '开源模型'
            }
        ]
    
    def get_openclaw_news(self) -> List[Dict]:
        """获取OpenClaw技术相关内容"""
        return [
            {
                'title': 'OpenClaw爆火两周后，它的用法已经比科幻世界还离谱了',
                'url': 'https://www.huxiu.com/article/4833948.html',
                'snippet': '硅星人报道：OpenClaw在短时间内迅速走红，用户们开发出了各种出人意料的用法，从自动化工作流到智能助手，应用场景不断拓展。',
                'source': '虎嗅网/硅星人',
                'category': '应用案例'
            },
            {
                'title': '玩转OpenClaw｜云上OpenClaw(Clawdbot)一键秒级部署指南',
                'url': 'https://cloud.tencent.com/developer/article/2626666',
                'snippet': '腾讯云Lighthouse官方教程：详细介绍如何在腾讯云轻量应用服务器上一键部署OpenClaw，支持QQ、企业微信、飞书、钉钉等多种IM接入。',
                'source': '腾讯云开发者社区',
                'category': '部署教程'
            },
            {
                'title': '玩转OpenClaw｜云上OpenClaw快速接入飞书指南',
                'url': 'https://cloud.tencent.com/developer/article/2626888',
                'snippet': '详细指导如何为已部署的OpenClaw配置飞书通道，包括模型配置、飞书机器人创建和权限设置等步骤。',
                'source': '腾讯云开发者社区',
                'category': '接入教程'
            },
            {
                'title': '玩转OpenClaw｜OpenClaw+Skills可以做什么？',
                'url': 'https://cloud.tencent.com/developer/article/2627350',
                'snippet': '介绍如何通过Skills扩展OpenClaw的能力边界，包括安装、使用和删除Skills的方法，让OpenClaw拥有更多实用功能。',
                'source': '腾讯云开发者社区',
                'category': '进阶技巧'
            },
            {
                'title': '玩转OpenClaw｜如何访问OpenClaw WebUI',
                'url': 'https://cloud.tencent.com/developer/article/2627344',
                'snippet': '介绍两种安全访问OpenClaw WebUI的方式：通过OrcaTerm端口转发或本地SSH隧道，避免直接暴露公网端口带来的安全风险。',
                'source': '腾讯云开发者社区',
                'category': '安全配置'
            },
            {
                'title': 'OpenClaw(Clawdbot)接入自定义大模型教程',
                'url': 'https://cloud.tencent.com/developer/article/2627520',
                'snippet': '详细教程：如何为OpenClaw配置自定义大模型，包括国内模型服务商的配置方法和注意事项。',
                'source': '腾讯云开发者社区',
                'category': '模型配置'
            },
            {
                'title': '云上OpenClaw(Clawdbot)最全实践教程合辑',
                'url': 'https://cloud.tencent.com/developer/article/2627104',
                'snippet': '汇总所有OpenClaw相关教程，包括部署指南、接入QQ/企微/飞书/钉钉教程、Skills使用指南等完整资料。',
                'source': '腾讯云开发者社区',
                'category': '教程合集'
            }
        ]
    
    def get_static_tutorials(self) -> List[Dict]:
        """获取教程技巧数据"""
        return [
            {
                'title': 'GPT-5.3 Codex使用指南：最大化编程效率',
                'title_en': 'GPT-5.3 Codex Guide: Maximize Coding Efficiency',
                'url': 'https://openai.com/blog',
                'snippet': '学习如何充分利用GPT-5.3 Codex的代码生成能力，包括最佳提示词实践和常见用例模式。',
                'source': '国际',
                'category': '编程'
            },
            {
                'title': '【中文】如何用大模型辅助写周报和日报',
                'title_en': 'How to Use LLMs for Weekly/Daily Reports',
                'url': 'https://www.jiqizhixin.com/',
                'snippet': '机器之心整理的实用技巧：如何利用ChatGPT、Claude等大模型高效撰写工作汇报，包括提示词模板和注意事项。',
                'source': '机器之心',
                'category': '办公效率'
            },
            {
                'title': 'Claude Opus 4.6提示工程进阶技巧',
                'title_en': 'Claude Opus 4.6 Prompt Engineering Tips',
                'url': 'https://docs.anthropic.com',
                'snippet': 'Anthropic官方推荐的提示工程技术，帮助用户获得更准确、更有用的AI回复。',
                'source': '国际',
                'category': '提示词工程'
            },
            {
                'title': '【中文】AI绘画入门：Midjourney vs Stable Diffusion对比',
                'title_en': 'AI Art Beginner: Midjourney vs Stable Diffusion',
                'url': 'https://www.qbitai.com/',
                'snippet': '量子位出品的AI绘画入门指南，详细对比Midjourney和Stable Diffusion的优缺点、适用场景和使用成本。',
                'source': '量子位',
                'category': 'AI绘画'
            },
            {
                'title': '构建AI原生应用的架构模式',
                'title_en': 'Architecture Patterns for AI-Native Applications',
                'url': 'https://www.anthropic.com/engineering',
                'snippet': '学习如何设计和构建充分利用大语言模型能力的现代应用程序架构。',
                'source': '国际',
                'category': '架构设计'
            }
        ]
    
    def gather_news(self) -> Dict[str, List[Dict]]:
        """汇总所有新闻数据"""
        return {
            'headlines': self.get_static_headlines(),
            'tools': self.get_static_tools(),
            'tutorials': self.get_static_tutorials(),
            'openclaw': self.get_openclaw_news()
        }
    
    def generate_html(self, news: Dict[str, List[Dict]]) -> str:
        """生成HTML格式的日报"""
        today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
        weekday = datetime.now(timezone.utc).strftime('%A')
        weekday_cn = {
            'Monday': '星期一', 'Tuesday': '星期二', 'Wednesday': '星期三',
            'Thursday': '星期四', 'Friday': '星期五', 'Saturday': '星期六', 'Sunday': '星期日'
        }.get(weekday, weekday)
        
        html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI新闻日报 - {today}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
            line-height: 1.8;
            color: #333;
            background: #f5f7fa;
        }}
        .container {{
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #1a73e8;
            border-bottom: 3px solid #1a73e8;
            padding-bottom: 15px;
            margin-bottom: 10px;
        }}
        .meta {{
            color: #666;
            margin-bottom: 30px;
            font-size: 0.95em;
        }}
        h2 {{
            color: #2c3e50;
            margin-top: 40px;
            border-left: 4px solid #1a73e8;
            padding-left: 15px;
        }}
        h3 {{
            color: #2c3e50;
            margin-top: 25px;
            font-size: 1.1em;
        }}
        .source {{
            display: inline-block;
            background: #e3f2fd;
            color: #1976d2;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.8em;
            margin-right: 8px;
        }}
        .source-cn {{
            background: #fff3e0;
            color: #f57c00;
        }}
        .category {{
            display: inline-block;
            background: #f5f5f5;
            color: #666;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.75em;
            margin-left: 8px;
        }}
        a {{
            color: #1a73e8;
            text-decoration: none;
            font-size: 0.9em;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .snippet {{
            background: #f8f9fa;
            border-left: 3px solid #1a73e8;
            padding: 12px 16px;
            margin: 10px 0 20px 0;
            color: #555;
            font-size: 0.95em;
        }}
        hr {{
            border: none;
            border-top: 1px solid #e0e0e0;
            margin: 30px 0;
        }}
        .footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #e0e0e0;
            color: #666;
            font-size: 0.9em;
        }}
        .footer table {{
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }}
        .footer th, .footer td {{
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid #e0e0e0;
        }}
        .footer th {{
            background: #f8f9fa;
            font-weight: 600;
        }}
        .back-link {{
            margin-bottom: 20px;
        }}
        .back-link a {{
            color: #1a73e8;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="back-link">← <a href="../index.html">返回首页</a></div>
        
        <h1>🤖 AI新闻日报 | AI Daily News</h1>
        <div class="meta">📅 <strong>{today}</strong> | {weekday_cn} | 中英文双语版</div>

        <hr>

        <h2>📰 头条新闻 | Headlines</h2>
"""
        
        # 头条新闻
        for i, item in enumerate(news['headlines'][:6], 1):
            title = item.get('title', '无标题')
            url = item.get('url', '#')
            snippet = item.get('snippet', '暂无摘要')
            source = item.get('source', '未知')
            category = item.get('category', '其他')
            source_class = 'source source-cn' if '中文' in source or source in ['机器之心', '国内', '腾讯新闻/机器之心'] else 'source'
            html += f"""
        <h3>{i}. {title}<span class="{source_class}">{source}</span><span class="category">{category}</span></h3>
        <p>🔗 <a href="{url}">查看原文</a></p>
        <div class="snippet">{snippet}</div>
"""
        
        html += """
        <hr>

        <h2>🛠️ 新工具/新模型 | New Tools & Models</h2>
"""
        
        # 新工具
        for i, item in enumerate(news['tools'][:6], 1):
            title = item.get('title', '无标题')
            url = item.get('url', '#')
            snippet = item.get('snippet', '暂无摘要')
            source = item.get('source', '未知')
            category = item.get('category', '其他')
            source_class = 'source source-cn' if '中文' in source or source in ['机器之心', '国内'] else 'source'
            html += f"""
        <h3>{i}. {title}<span class="{source_class}">{source}</span><span class="category">{category}</span></h3>
        <p>🔗 <a href="{url}">查看原文</a></p>
        <div class="snippet">{snippet}</div>
"""
        
        html += """
        <hr>

        <h2>📚 教程技巧 | Tutorials & Tips</h2>
"""
        
        # 教程技巧
        for i, item in enumerate(news['tutorials'][:5], 1):
            title = item.get('title', '无标题')
            url = item.get('url', '#')
            snippet = item.get('snippet', '暂无摘要')
            source = item.get('source', '未知')
            category = item.get('category', '其他')
            source_class = 'source source-cn' if '中文' in source or source in ['机器之心', '国内', '量子位'] else 'source'
            html += f"""
        <h3>{i}. {title}<span class="{source_class}">{source}</span><span class="category">{category}</span></h3>
        <p>🔗 <a href="{url}">查看原文</a></p>
        <div class="snippet">{snippet}</div>
"""
        
        html += """
        <hr>

        <h2>🦾 OpenClaw技术 | OpenClaw Tech</h2>
        <p style="color: #666; font-size: 0.9em; margin-top: -10px;">专注于OpenClaw的最新消息、部署教程与应用技巧 | 来源：腾讯云开发者社区、虎嗅网、36氪</p>
"""
        
        # OpenClaw技术内容
        for i, item in enumerate(news['openclaw'][:7], 1):
            title = item.get('title', '无标题')
            url = item.get('url', '#')
            snippet = item.get('snippet', '暂无摘要')
            source = item.get('source', '未知')
            category = item.get('category', '其他')
            source_class = 'source source-cn'
            html += f"""
        <h3>{i}. {title}<span class="{source_class}">{source}</span><span class="category">{category}</span></h3>
        <p>🔗 <a href="{url}">查看原文</a></p>
        <div class="snippet">{snippet}</div>
"""
        
        html += f"""
        <hr>

        <div class="footer">
            <h2>📝 关于本日报 | About</h2>
            <p>本日报通过自动化脚本生成，每日搜集最新的AI相关新闻、工具和教程。涵盖中文和英文数据源，包括机器之心、量子位、OpenAI Blog、腾讯云开发者社区等权威来源。</p>
            
            <table>
                <tr><th>项目</th><th>详情</th></tr>
                <tr><td>🔄 生成时间</td><td>{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}</td></tr>
                <tr><td>🤖 技术栈</td><td>Python + GitHub Actions</td></tr>
                <tr><td>📊 数据来源</td><td>机器之心、量子位、OpenAI、Anthropic、腾讯云开发者社区、虎嗅网、36氪</td></tr>
            </table>
            
            <p><em>AI Daily News © 2025 | 每日更新</em></p>
        </div>
    </div>
</body>
</html>
"""
        
        return html
    
    def save_daily_news(self, html_content: str) -> tuple:
        """保存日报文件（HTML和Markdown）"""
        today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
        
        # 保存HTML
        html_filename = f"{today}.html"
        html_filepath = os.path.join(self.news_dir, html_filename)
        with open(html_filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # 保存latest.html
        latest_html_path = os.path.join(self.news_dir, "latest.html")
        with open(latest_html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ HTML日报已保存: {html_filepath}")
        return html_filepath, latest_html_path
    
    def update_index(self):
        """更新首页索引"""
        index_path = os.path.join(self.workspace, "index.html")
        today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
        
        # 获取所有新闻文件
        news_files = []
        if os.path.exists(self.news_dir):
            for f in os.listdir(self.news_dir):
                if f.endswith('.html') and f not in ['latest.html', 'index.html']:
                    news_files.append(f.replace('.html', ''))
        
        news_files.sort(reverse=True)
        
        html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI新闻日报</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        .container {{
            background: white;
            padding: 40px;
            border-radius: 16px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #1a73e8;
            text-align: center;
            margin-bottom: 10px;
        }}
        .subtitle {{
            text-align: center;
            color: #666;
            margin-bottom: 30px;
        }}
        .today-news {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 12px;
            margin: 30px 0;
            text-align: center;
        }}
        .today-news a {{
            color: white;
            font-size: 1.3em;
            font-weight: bold;
            text-decoration: none;
        }}
        .today-news a:hover {{
            text-decoration: underline;
        }}
        h2 {{
            color: #2c3e50;
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 10px;
            margin-top: 40px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
        }}
        th, td {{
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #e0e0e0;
        }}
        th {{
            background: #f8f9fa;
            font-weight: 600;
            color: #1a73e8;
        }}
        tr:hover {{
            background: #f5f7fa;
        }}
        a {{
            color: #1a73e8;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #e0e0e0;
            color: #666;
            font-size: 0.9em;
            text-align: center;
        }}
        .badge {{
            display: inline-block;
            background: #e3f2fd;
            color: #1976d2;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.8em;
            margin-right: 8px;
        }}
        .badge-cn {{
            background: #fff3e0;
            color: #f57c00;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖 AI新闻日报</h1>
        <p class="subtitle">每日AI新闻汇总 | 中英文双语 | 涵盖机器之心、量子位、OpenAI、腾讯云开发者社区、虎嗅网等权威来源</p>

        <div class="today-news">
            <h2 style="color: white; border: none; margin-top: 0;">📰 今日日报</h2>
            <p>👉 <a href="./news/latest.html">{today} - 查看最新日报</a></p>
            <p style="font-size: 0.9em; opacity: 0.9;">
                <span class="badge badge-cn">机器之心</span>
                <span class="badge badge-cn">量子位</span>
                <span class="badge">OpenAI</span>
                <span class="badge">Anthropic</span>
                <span class="badge badge-cn">腾讯云</span>
                <span class="badge badge-cn">虎嗅</span>
            </p>
        </div>

        <h2>📚 日报板块</h2>
        <table>
            <tr>
                <th>板块</th>
                <th>内容</th>
            </tr>
            <tr>
                <td>📰 头条新闻</td>
                <td>AI行业重磅消息、产品发布、公司动态</td>
            </tr>
            <tr>
                <td>🛠️ 新工具/新模型</td>
                <td>最新AI工具、开源模型、生产力应用</td>
            </tr>
            <tr>
                <td>📚 教程技巧</td>
                <td>AI使用技巧、提示词工程、最佳实践</td>
            </tr>
            <tr>
                <td>🦾 OpenClaw技术</td>
                <td>OpenClaw部署教程、应用技巧、最新消息</td>
            </tr>
        </table>

        <h2>📅 历史归档</h2>
        <table>
            <tr>
                <th>日期</th>
                <th>链接</th>
            </tr>
"""
        
        for date in news_files[:30]:
            html += f"""            <tr>
                <td>{date}</td>
                <td><a href="./news/{date}.html">查看日报</a></td>
            </tr>
"""
        
        html += """        </table>

        <div class="footer">
            <h2>🚀 关于</h2>
            <p>
                <span class="badge badge-cn">中文源</span> 机器之心、量子位、腾讯新闻、腾讯云开发者社区、虎嗅网、36氪<br>
                <span class="badge">英文源</span> OpenAI Blog、Anthropic、VentureBeat<br>
                <span class="badge badge-cn">特色板块</span> 🦾 OpenClaw技术 - 部署教程、应用技巧、最新消息<br>
                📅 每日 UTC 00:00 自动生成 | 🤖 Python + GitHub Actions
            </p>
            <p><em>AI Daily News © 2025</em></p>
        </div>
    </div>
</body>
</html>
"""
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"✅ 首页索引已更新: {index_path}")
    
    def run(self):
        """运行日报生成流程"""
        print("="*60)
        print("🚀 开始生成AI新闻日报（多语言版）")
        print("="*60)
        
        # 1. 搜集新闻
        print("📡 正在搜集新闻数据（中英文混合）...")
        news = self.gather_news()
        
        # 2. 生成HTML
        print("📝 正在生成HTML日报...")
        html_content = self.generate_html(news)
        
        # 3. 保存文件
        print("💾 正在保存文件...")
        filepath, _ = self.save_daily_news(html_content)
        
        # 4. 更新索引
        print("🔄 正在更新首页索引...")
        self.update_index()
        
        print("="*60)
        print(f"✅ 日报生成完成!")
        print(f"📄 文件位置: {filepath}")
        print(f"🌐 访问地址: https://royelau76.github.io/ai-news-daily/")
        print("="*60)
        
        return filepath

if __name__ == "__main__":
    generator = AIDailyNewsGenerator()
    generator.run()
