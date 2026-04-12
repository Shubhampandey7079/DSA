import requests
import datetime

USERNAME = "8AdxLDYG0y"
GITHUB = "Shubhampandey7079"

# -------------------------------
# FETCH STATS
# -------------------------------
stats_url = f"https://leetcode-api-faisalshohag.vercel.app/{USERNAME}"

try:
    res = requests.get(stats_url, timeout=10)
    stats = res.json() if res.status_code == 200 else {}
except:
    stats = {}

total = stats.get("totalSolved", 0)
easy = stats.get("easySolved", 0)
medium = stats.get("mediumSolved", 0)
hard = stats.get("hardSolved", 0)
ranking = stats.get("ranking", "N/A")

# -------------------------------
# FETCH RECENT SUBMISSIONS
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
        }
    }
    """,
    "variables": {"username": USERNAME, "limit": 5}
}

headers = {
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com/",
    "User-Agent": "Mozilla/5.0"
}

recent_problems = []

try:
    res = requests.post(recent_url, json=query, headers=headers, timeout=10)
    data = res.json()
    recent = data.get("data", {}).get("recentAcSubmissionList", [])

    for p in recent:
        recent_problems.append({
            "title": p["title"],
            "link": f"https://leetcode.com/problems/{p['titleSlug']}/",
            "difficulty": p["difficulty"],
            "lang": p["lang"]
        })
except:
    recent_problems = []

# -------------------------------
# PROGRESS BAR (CLEAN)
# -------------------------------
def progress_bar(value, total):
    percent = int((value / total) * 100) if total > 0 else 0
    filled = int(percent / 10)
    bar = "█" * filled + "░" * (10 - filled)
    return f"{percent}% {bar}"

# -------------------------------
# WRITE README
# -------------------------------
with open("README.md", "w", encoding="utf-8") as f:

    # HERO HEADER (ANIMATED)
    f.write('<div align="center">\n')
    f.write(f'<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=30&duration=2500&pause=1000&color=00F7FF&center=true&vCenter=true&width=700&lines=🚀+LeetCode+Dashboard;{total}+Problems+Solved;Keep+Grinding+🔥;Ranking:+{ranking}" />\n')
    f.write('</div>\n\n')

    # BADGES
    f.write('<div align="center">\n')
    f.write(f'<img src="https://img.shields.io/badge/Total_Solved-{total}-blue?style=for-the-badge&logo=leetcode"/>\n')
    f.write(f'<img src="https://img.shields.io/badge/Easy-{easy}-success?style=for-the-badge"/>\n')
    f.write(f'<img src="https://img.shields.io/badge/Medium-{medium}-yellow?style=for-the-badge"/>\n')
    f.write(f'<img src="https://img.shields.io/badge/Hard-{hard}-red?style=for-the-badge"/>\n')
    f.write('</div>\n\n')

    # PROGRESS SECTION
    f.write("## 🎯 Progress Tracker\n\n")
    f.write(f"**Easy**   → {progress_bar(easy, 200)} ({easy}/200)\n\n")
    f.write(f"**Medium** → {progress_bar(medium, 500)} ({medium}/500)\n\n")
    f.write(f"**Hard**   → {progress_bar(hard, 150)} ({hard}/150)\n\n")

    # LEETCODE CARD
    f.write("## 📊 LeetCode Stats\n\n")
    f.write(f'<div align="center">\n')
    f.write(f'<img src="https://leetcard.jacoblin.cool/{USERNAME}?theme=dark&ext=heatmap" width="80%"/>\n')
    f.write(f'</div>\n\n')

    # GITHUB STATS
    f.write("## 🔥 GitHub Insights\n\n")
    f.write('<div align="center">\n')
    f.write(f'<img src="https://github-readme-stats.vercel.app/api?username={GITHUB}&show_icons=true&theme=tokyonight" height="180"/>\n')
    f.write(f'<img src="https://github-readme-stats.vercel.app/api/top-langs/?username={GITHUB}&layout=compact&theme=tokyonight" height="180"/>\n')
    f.write('</div>\n\n')

    f.write('<div align="center">\n')
    f.write(f'<img src="https://streak-stats.demolab.com?user={GITHUB}&theme=tokyonight"/>\n')
    f.write('</div>\n\n')

    # ACTIVITY GRAPH
    f.write("## 📈 Contribution Graph\n\n")
    f.write(f'<img src="https://github-readme-activity-graph.vercel.app/graph?username={GITHUB}&theme=tokyo-night" width="100%"/>\n\n')

    # RECENT SUBMISSIONS
    f.write("## 🕒 Recent Submissions\n\n")
    f.write("| # | Problem | Difficulty | Language |\n")
    f.write("|---|---------|------------|----------|\n")

    if recent_problems:
        for i, p in enumerate(recent_problems, 1):
            emoji = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}.get(p["difficulty"], "⚪")
            f.write(f"| {i} | [{p['title']}]({p['link']}) | {emoji} {p['difficulty']} | {p['lang']} |\n")
    else:
        f.write("| 1 | No recent submissions | - | - |\n")

    # FOOTER
    now = datetime.datetime.utcnow().strftime("%b %d, %Y %H:%M UTC")
    f.write(f"\n---\n⏱ Updated: {now}\n")

print("🔥 PRO README generated!")
