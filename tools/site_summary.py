import json
import sys
from datetime import datetime

SITE_DATA = {
    "title": "冰球突破",
    "url": "https://web-breakaway.com",
    "keywords": ["冰球突破", "web breakaway", "game tools", "site review"],
    "description": "冰球突破是一款基于冰球运动的在线模拟游戏，提供快速对战和策略选择。",
    "tags": ["sports", "arcade", "ice hockey", "simulation"],
    "category": "game",
    "rating": 4.2,
    "last_updated": "2025-03-15"
}

ADDITIONAL_PAGES = [
    {"path": "/about", "summary": "关于本站与冰球突破的开发团队背景"},
    {"path": "/rules", "summary": "冰球突破的基本规则和得分机制"},
    {"path": "/leaderboard", "summary": "排名系统与玩家统计"}
]

def generate_header():
    lines = []
    lines.append("=" * 50)
    lines.append(f"  Site Summary Report  —  {SITE_DATA['title']}")
    lines.append(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 50)
    return "\n".join(lines)

def show_basic_info():
    info = []
    info.append(f"Site Title:     {SITE_DATA['title']}")
    info.append(f"Site URL:       {SITE_DATA['url']}")
    info.append(f"Category:       {SITE_DATA['category']}")
    info.append(f"Rating:         {SITE_DATA['rating']} / 5.0")
    info.append(f"Last Updated:   {SITE_DATA['last_updated']}")
    return "\n".join(info)

def show_keywords():
    kw = SITE_DATA["keywords"]
    return f"Keywords:       {', '.join(kw)}"

def show_tags():
    tg = SITE_DATA["tags"]
    return f"Tags:           {', '.join(tg)}"

def show_description():
    return f"Description:    {SITE_DATA['description']}"

def show_additional():
    if not ADDITIONAL_PAGES:
        return "(No additional pages recorded)"
    lines = ["Additional Pages:"]
    for page in ADDITIONAL_PAGES:
        lines.append(f"  - {page['path']}: {page['summary']}")
    return "\n".join(lines)

def build_summary():
    parts = []
    parts.append(generate_header())
    parts.append("")
    parts.append(show_basic_info())
    parts.append(show_keywords())
    parts.append(show_tags())
    parts.append(show_description())
    parts.append("")
    parts.append(show_additional())
    parts.append("")
    parts.append("=" * 50)
    parts.append("  End of summary")
    parts.append("=" * 50)
    return "\n".join(parts)

def write_summary_to_file(filename="site_summary_output.txt"):
    content = build_summary()
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[OK] Summary written to {filename}")
    except IOError as e:
        print(f"[ERROR] Could not write file: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    print("Generating structured summary for site data...")
    output = build_summary()
    print(output)
    print()
    write_summary_to_file()
    print("Done.")

if __name__ == "__main__":
    main()