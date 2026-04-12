import requests
import datetime

USERNAME = "8AdxLDYG0y"
GITHUB = "Shubhampandey7079"

# -------------------------------
# 1. BASIC STATS API
# -------------------------------
stats_url = f"https://leetcode-api-faisalshohag.vercel.app/{USERNAME}"

try:
    res = requests.get(stats_url, timeout=10)
    stats = res.json() if res.status_code == 200 else {}
except Exception:
    stats = {}

total = stats.get("totalSolved", 0)
easy = stats.get("easySolved", 0)
medium = stats.get("mediumSolved", 0)
hard = stats.get("hardSolved", 0)
ranking = stats.get("ranking", "N/A")
acceptance = stats.get("acceptanceRate", 0.0)

# -------------------------------
# 2. RECENT SUBMISSIONS (GraphQL)
# -------------------------------
recent_url = "https://leetcode.com/graphql"

query = {
    "query": """
    query recentAcSubmissions($username: String!, $limit: Int!) {
        recentAcSubmissionList(username: $username, limit: $limit) {
            title
            titleSlug
            difficulty
            lang
            timestamp
        }
    }
    """,
    "variables": {"username": USERNAME, "limit": 5}
}

recent_problems = []

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://leetcode.com/"
}

try:
    res = requests.post(recent_url, json=query, headers=headers, timeout=10)
    data = res.json()
    recent = data.get("data", {}).get("recentAcSubmissionList", [])

    for p in recent:
        title = p["title"]
        slug = p["titleSlug"]
        link = f"https://leetcode.com/problems/{slug}/"
        recent_problems.append({
            "title": title,
            "link": link,
            "difficulty": p["difficulty"],
            "lang": p["lang"]
        })
except Exception:
    recent_problems = []

# -------------------------------
# 3. ACCURATE RECENT ANALYTICS
# -------------------------------
lang_counts = {}
diff_counts = {"Easy": 0, "Medium": 0, "Hard": 0}

for p in recent_problems:
    lang = p["lang"]
    diff = p["difficulty"]
    lang_counts[lang] = lang_counts.get(lang, 0) + 1
    diff_counts[diff] = diff_counts.get(diff, 0) + 1

# -------------------------------
# 4. HELPER FUNCTIONS (GITHUB SAFE)
# -------------------------------
def get_dynamic_badge(solved, goal, label):
    percent = min((solved / goal) * 100, 100) if goal > 0 else 0
    display_percent = f"{percent:.1f}" if percent > 0 else "0"
    
    if percent < 25: color = "red"
    elif percent < 50: color = "yellow"
    elif percent < 75: color = "green"
    else: color = "brightgreen"
    
    return f'<img src="https://img.shields.io/badge/{label}-{solved}/{goal} ({display_percent}%)-{color}?style=for-the-badge&logo=leetcode" />'

def get_skill_bar(solved, goal, color_hex):
    percent = min((solved / goal) * 100, 100) if goal > 0 else 0
    visual_width = max(percent, 2) if solved > 0 else 0
    display_percent = f"{percent:.1f}" if percent > 0 else "0"
    
    return f'''
    <div align="center">
        <code>██████████</code>&nbsp;{display_percent}%
        <br><br>
        <div style="width: 100%; max-width: 400px; height: 12px; background: #1a1b27; border-radius: 6px; overflow: hidden; border: 1px solid #38bdf8;">
            <div style="width: {visual_width}%; height: 100%; background: linear-gradient(90deg, {color_hex}, #ffffff); border-radius: 6px;"></div>
        </div>
        <br>
    </div>'''

# -------------------------------
# 5. WRITE README
# -------------------------------
with open("README.md", "w") as f:
    
    # Typing SVG Header
    f.write('<div align="center">\n')
    f.write(f'<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=28&duration=3000&pause=1000&color=70A5FD&center=true&vCenter=true&width=600&lines=🚀+LeetCode+Dashboard;Solved+{total}+Problems+and+Counting...;Ranking:+{ranking}" alt="Typing SVG" /></a>\n')
    f.write('</div>\n\n')

    # Glassmorphism Profile Card (FIXED: Removed backdrop-filter)
    f.write('<div align="center">\n')
    f.write('  <div style="background: #1e293b; border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 16px; padding: 20px; max-width: 600px; margin: 0 auto; box-shadow: 0 8px 32px 0 rgba(0,0,0,0.5);">\n')
    f.write(f'    <h2 style="color: #ffffff; margin-bottom: 10px;">🎯 Target Progress</h2>\n')
    f.write(f'    {get_dynamic_badge(easy, 800, "Easy")}\n    <br><br>\n')
    f.write(f'    {get_dynamic_badge(medium, 1500, "Medium")}\n    <br><br>\n')
    f.write(f'    {get_dynamic_badge(hard, 500, "Hard")}\n')
    f.write('  </div>\n')
    f.write('</div>\n\n')
    
    # Animated Skill Bars
    f.write(f'{get_skill_bar(easy, 800, "#00b8a3")} \n')
    f.write(f'{get_skill_bar(medium, 1500, "#ffc01e")} \n')
    f.write(f'{get_skill_bar(hard, 500, "#ff375f")} \n')

    f.write('<br><br>\n')

    # ---------------------------
    # LeetCode Heatmap & Stats Cards
    # ---------------------------
    f.write('<div align="center">\n')
    f.write(f'  <img src="https://leetcard.jacoblin.cool/{USERNAME}?ext=heatmap&theme=dark&font=Lato&radius=10" />\n')
    f.write('</div>\n\n')

    f.write('## 🔥 GitHub Vibe Check\n\n')
    f.write('<p align="center">\n')
    f.write(f'  <img src="https://github-readme-stats.vercel.app/api?username={GITHUB}&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=70a5fd&icon_color=38bdf8" height="180"/>\n')
    f.write(f'  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={GITHUB}&layout=compact&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=70a5fd&text_color=c9d1d9" height="180"/>\n')
    f.write('</p>\n\n')
    
    f.write('<p align="center">\n')
    f.write(f'  <a href="https://github.com/ashutosh00710/github-readme-activity-graph"><img src="https://github-readme-activity-graph.vercel.app/graph?username={GITHUB}&bg_color=0d1117&color=70a5fd&line=38bdf8&point=38bdf8&area=true&hide_border=true&radius=8" width="100%"/></a>\n')
    f.write('</p>\n\n')

    f.write('<p align="center">\n')
    f.write(f'  <img src="https://streak-stats.demolab.com?user={GITHUB}&theme=tokyonight&hide_border=true&background=0d1117&ring=38bdf8&fire=ff375f&currStreakLabel=70a5fd" />\n')
    f.write('</p>\n\n')

    # ---------------------------
    # Recent Submissions (FIXED: Converted from broken Table to pure HTML List)
    # ---------------------------
    f.write('<div align="center">\n')
    f.write('<h2>🕒 Recent Submissions</h2>\n')
    
    f.write('<div style="background: #1e293b; padding: 20px; border-radius: 12px; border: 1px solid #38bdf8; width: 100%; max-width: 700px; margin: 0 auto;">\n')

    if recent_problems:
        for idx, p in enumerate(recent_problems, 1):
            diff_emoji = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}.get(p["difficulty"], "⚪")
            # Using pure HTML list layout to prevent GitHub markdown parser from breaking
            f.write(f'<div style="display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 1px solid #334155;">\n')
            f.write(f'  <span style="color: #8b949e; width: 30px;">{idx}.</span>\n')
            f.write(f'  <a href="{p["link"]}" style="color: #38bdf8; text-decoration: none; flex-grow: 1; text-align: left; margin-left: 10px;">{p["title"]}</a>\n')
            f.write(f'  <span style="margin: 0 15px;">{diff_emoji} {p["difficulty"]}</span>\n')
            f.write(f'  <code style="background: #0d1117; padding: 4px 8px; border-radius: 4px; color: #c9d1d9;">{p["lang"]}</code>\n')
            f.write(f'</div>\n')
    else:
        f.write('<p style="color: #8b949e; text-align: center; margin: 0;"><i>No recent submissions yet. Start solving to see them here!</i></p>\n')

    f.write('</div>\n')
    f.write('</div>\n\n')

    # ---------------------------
    # Recent Analytics (Only shows if data exists)
    # ---------------------------
    if recent_problems:
        f.write('<div align="center">\n')
        f.write('<h2>🧠 Recent Analytics</h2>\n')
        
        lang_badges = " ".join([f'<img src="https://img.shields.io/badge/{lang}-{count}_solve{"s" if count > 1 else ""}-blue?style=flat-square" />' for lang, count in lang_counts.items()])
        diff_badges = " ".join([f'<img src="https://img.shields.io/badge/{diff}-{count}_solve{"s" if count > 1 else ""}-{color}?style=flat-square" />' for diff, count, color in [("Easy", diff_counts.get("Easy",0), "success"), ("Medium", diff_counts.get("Medium",0), "yellow"), ("Hard", diff_counts.get("Hard",0), "critical")] if count > 0])

        f.write(f'{lang_badges}  \n\n')
        f.write(f'{diff_badges}\n')
        f.write('</div>\n\n')

    # ---------------------------
    # Footer
    # ---------------------------
    current_time = datetime.datetime.utcnow().strftime("%b %d, %Y at %H:%M UTC")
    
    f.write('<div align="center">\n')
    f.write('<hr style="border-color: #38bdf8; width: 50%; border-width: 2px;">\n')
    f.write(f'<i style="color: #8b949e;">⏱ Auto-updated: {current_time} | Built with ❤️ by <a href="https://github.com/{GITHUB}" style="color: #70a5fd;">{GITHUB}</a></i>\n')
    f.write('</div>\n')

print("✅ Ultra-attractive README.md generated successfully!")
