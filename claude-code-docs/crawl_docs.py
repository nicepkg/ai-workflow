#!/usr/bin/env python3
"""
Claude Code 文档爬虫脚本
将 https://code.claude.com/docs 的文档爬取并转换为 Markdown 文件
"""

import os
import re
import time
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# 配置
BASE_URL = "https://code.claude.com/docs"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "docs")
LANGUAGE = "en"  # 爬取英文文档

# 文档页面列表
DOC_PAGES = [
    # Getting started
    "overview",
    "quickstart",
    "common-workflows",
    "changelog",
    # Outside of the terminal
    "claude-code-on-the-web",
    "desktop",
    "chrome",
    "vs-code",
    "jetbrains",
    "github-actions",
    "gitlab-ci-cd",
    "slack",
    # Build with Claude Code
    "sub-agents",
    "plugins",
    "discover-plugins",
    "skills",
    "output-styles",
    "hooks-guide",
    "headless",
    "mcp",
    "troubleshooting",
    # Deployment
    "third-party-integrations",
    "amazon-bedrock",
    "google-vertex-ai",
    "microsoft-foundry",
    "network-config",
    "llm-gateway",
    "devcontainer",
    "sandboxing",
    # Administration
    "setup",
    "iam",
    "security",
    "data-usage",
    "monitoring-usage",
    "costs",
    "analytics",
    "plugin-marketplaces",
    # Configuration
    "settings",
    "terminal-config",
    "model-config",
    "memory",
    "statusline",
    # Reference
    "cli-reference",
    "interactive-mode",
    "slash-commands",
    "checkpointing",
    "hooks",
    "plugins-reference",
    # Resources
    "legal-and-compliance",
]

# HTTP 请求头
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}


def fetch_page(url: str) -> str | None:
    """获取页面 HTML 内容"""
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"  ❌ 获取失败: {e}")
        return None


def extract_main_content(html: str) -> tuple[str, str]:
    """从 HTML 中提取主要内容区域，返回 (title, content_html)"""
    soup = BeautifulSoup(html, "html.parser")

    # 提取标题
    title = ""
    title_tag = soup.find("h1")
    if title_tag:
        title = title_tag.get_text(strip=True)

    # 尝试找到主内容区域 - 通常在 article 或 main 标签中
    main_content = None

    # 尝试不同的选择器
    selectors = [
        "article",
        "main",
        "[role='main']",
        ".docs-content",
        ".content",
        "#content",
        ".markdown-body",
    ]

    for selector in selectors:
        main_content = soup.select_one(selector)
        if main_content:
            break

    # 如果没找到，使用 body
    if not main_content:
        main_content = soup.find("body")

    if main_content:
        # 移除不需要的元素
        for element in main_content.select("nav, header, footer, script, style, .sidebar, .toc, .navigation"):
            element.decompose()

        return title, str(main_content)

    return title, ""


def html_to_markdown(html: str, base_url: str) -> str:
    """将 HTML 转换为 Markdown"""
    # 先用 BeautifulSoup 清理 HTML
    soup = BeautifulSoup(html, "html.parser")

    # 移除按钮和交互元素
    for btn in soup.select("button, .copy-button, [data-copy], .ask-ai"):
        btn.decompose()

    # 移除 "Copy" 和 "Ask AI" 文本节点
    for text_node in soup.find_all(string=re.compile(r"^(Copy|Ask AI)$")):
        if text_node.parent and text_node.parent.name not in ["code", "pre"]:
            text_node.extract()

    # 修复代码块语言
    for code in soup.select("code"):
        classes = code.get("class", [])
        for cls in classes:
            if "language-shiki" in cls or cls == "shiki":
                # 尝试从父元素或 data 属性获取真实语言
                code["class"] = [c.replace("shiki", "bash") for c in classes]

    html = str(soup)

    # 使用 markdownify 转换
    markdown = md(
        html,
        heading_style="ATX",
        bullets="-",
        code_language_callback=lambda el: el.get("class", [""])[0].replace("language-", "") if el.get("class") else "",
    )

    # 清理 shiki 语言标记
    markdown = re.sub(r"```shiki\b", "```bash", markdown)
    markdown = re.sub(r"```language-shiki\b", "```bash", markdown)

    # 移除残留的 "Copy" 和 "Ask AI"
    markdown = re.sub(r"\nCopy\n", "\n", markdown)
    markdown = re.sub(r"\nAsk AI\n", "\n", markdown)
    markdown = re.sub(r"^Copy$", "", markdown, flags=re.MULTILINE)
    markdown = re.sub(r"^Ask AI$", "", markdown, flags=re.MULTILINE)

    # 清理多余的空行
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)

    # 清理行首行尾空白
    lines = [line.rstrip() for line in markdown.split("\n")]
    markdown = "\n".join(lines)

    return markdown.strip()


def save_markdown(content: str, filename: str):
    """保存 Markdown 文件"""
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✅ 已保存: {filename}")


def crawl_page(page_slug: str) -> bool:
    """爬取单个页面"""
    url = f"{BASE_URL}/{LANGUAGE}/{page_slug}"
    print(f"\n📄 正在爬取: {page_slug}")
    print(f"   URL: {url}")

    html = fetch_page(url)
    if not html:
        return False

    title, content_html = extract_main_content(html)
    if not content_html:
        print("  ⚠️ 未找到内容")
        return False

    markdown = html_to_markdown(content_html, url)

    # 添加文档头信息
    header = f"""---
source: {url}
title: {title}
---

"""

    full_content = header + markdown

    # 保存文件
    filename = f"{page_slug}.md"
    save_markdown(full_content, filename)

    return True


def create_index(successful_pages: list[str]):
    """创建索引文件"""
    index_content = """---
title: Claude Code Documentation Index
---

# Claude Code 文档索引

此文件夹包含从 https://code.claude.com/docs 爬取的文档。

## 文档列表

"""

    categories = {
        "Getting Started": ["overview", "quickstart", "common-workflows", "changelog"],
        "Outside of the Terminal": ["claude-code-on-the-web", "desktop", "chrome", "vs-code", "jetbrains", "github-actions", "gitlab-ci-cd", "slack"],
        "Build with Claude Code": ["sub-agents", "plugins", "discover-plugins", "skills", "output-styles", "hooks-guide", "headless", "mcp", "troubleshooting"],
        "Deployment": ["third-party-integrations", "amazon-bedrock", "google-vertex-ai", "microsoft-foundry", "network-config", "llm-gateway", "devcontainer", "sandboxing"],
        "Administration": ["setup", "iam", "security", "data-usage", "monitoring-usage", "costs", "analytics", "plugin-marketplaces"],
        "Configuration": ["settings", "terminal-config", "model-config", "memory", "statusline"],
        "Reference": ["cli-reference", "interactive-mode", "slash-commands", "checkpointing", "hooks", "plugins-reference"],
        "Resources": ["legal-and-compliance"],
    }

    for category, pages in categories.items():
        index_content += f"### {category}\n\n"
        for page in pages:
            if page in successful_pages:
                index_content += f"- [{page}](./{page}.md)\n"
        index_content += "\n"

    save_markdown(index_content, "INDEX.md")


def main():
    """主函数"""
    # 确保输出目录存在
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("=" * 60)
    print("Claude Code 文档爬虫")
    print("=" * 60)
    print(f"输出目录: {OUTPUT_DIR}")
    print(f"文档数量: {len(DOC_PAGES)}")

    successful = []
    failed = []

    for page_slug in DOC_PAGES:
        if crawl_page(page_slug):
            successful.append(page_slug)
        else:
            failed.append(page_slug)

        # 礼貌性延迟，避免请求过快
        time.sleep(0.5)

    # 创建索引
    print("\n📑 创建索引文件...")
    create_index(successful)

    # 打印统计
    print("\n" + "=" * 60)
    print("爬取完成!")
    print(f"成功: {len(successful)}/{len(DOC_PAGES)}")

    if failed:
        print(f"失败: {failed}")

    print("=" * 60)


if __name__ == "__main__":
    main()
