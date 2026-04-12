import requests
import datetime

USERNAME = "8AdxLDYG0y"
GITHUB = "Shubhampandey7079"

# -------------------------------
# 1. BASIC STATS
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
# 2. RECENT SUBMISSIONS
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
# 3. ANALYTICS
# -------------------------------
lang_counts = {}
diff_counts = {"Easy": 0, "Medium": 0, "Hard": 0}

for p in recent_problems:
    lang_counts[p["lang"]] = lang_counts.get(p["lang"], 0) + 1
    diff_counts[p["difficulty"]] += 1

# -------------------------------
# 4. UI HELPERS
# -------------------------------
def get_dynamic_badge(solved, goal, label):
    percent = round((solved / goal) * 100, 1) if goal > 0 else 0

    if percent < 25:
        color = "red"
    elif percent < 50:
        color = "yellow"
    elif percent < 75:
        color = "green"
    else:
        color = "brightgreen"

    return f'<img src="https://img.shields.io/badge/{label}-{solved}/{goal} ({percent}%)-{color}?style=for-the-badge&logo=leetcode" />'


def get_skill_bar(solved, goal, color):
    percent = round((solved / goal) * 100, 1) if goal > 0 else 0
    visual_width = percent if percent >= 3 else (3 if solved > 0 else 0)

    return f"""
    <div align="center">
        <p><b>{percent}%</b></p>
        <div style="width:90%;max-width:400px;height:10px;background:#1a1b27;border-radius:10px;border:1px solid #2f3542;">
            <div style="width:{visual_width}%;height:100%;background:linear-gradient(90deg,{color},#ffffff);border-radius:10px;"></div>
        </div>
    </div><br>
    """

# -------------------------------
# 5. WRITE README
# -------------------------------
with open("README.md", "w", encoding="utf-8") as f:

    # HEADER
    f.write('<div align="center">\n')
    f.write(f'<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=28&duration=3000&pause=1000&color=70A5FD&center=true&vCenter=true&width=600&lines=🚀+LeetCode+Dashboard;Solved+{total}+Problems;Ranking:+{ranking}" />\n')
    f.write('</div>\n\n')

    # TARGET
    f.write('<h2 align="center">🎯 Target Progress</h2>\n')
    f.write('<div align="center">\n')
    f.write(get_dynamic_badge(easy, 200, "Easy") + "<br><br>\n")
    f.write(get_dynamic_badge(medium, 500, "Medium") + "<br><br>\n")
    f.write(get_dynamic_badge(hard, 150, "Hard") + "\n")
    f.write('</div>\n\n')

    # BARS
    f.write(get_skill_bar(easy, 200, "#00b894"))
    f.write(get_skill_bar(medium, 500, "#fdcb6e"))
    f.write(get_skill_bar(hard, 150, "#ff7675"))

    # LEETCODE CARD
    f.write('<div align="center">\n')
    f.write(f'<img src="https://leetcard.jacoblin.cool/{USERNAME}?theme=dark&ext=heatmap" />\n')
    f.write('</div>\n\n')

    # GITHUB STATS
    f.write('## 🔥 GitHub Vibe Check\n\n')
    f.write('<p align="center">\n')
    f.write(f'<img src="https://github-readme-stats.vercel.app/api?username={GITHUB}&show_icons=true&theme=tokyonight" height="180"/>\n')
    f.write(f'<img src="https://github-readme-stats.vercel.app/api/top-langs/?username={GITHUB}&layout=compact&theme=tokyonight" height="180"/>\n')
    f.write('</p>\n\n')

    # STREAK
    f.write('<p align="center">\n')
    f.write(f'<img src="https://streak-stats.demolab.com?user={GITHUB}&theme=tokyonight" />\n')
    f.write('</p>\n\n')

    # RECENT SUBMISSIONS
    f.write('## 🕒 Recent Submissions\n\n')
    f.write('| # | Problem | Difficulty | Language |\n')
    f.write('|---|---------|------------|----------|\n')

    if recent_problems:
        for i, p in enumerate(recent_problems, 1):
            f.write(f"| {i} | [{p['title']}]({p['link']}) | {p['difficulty']} | {p['lang']} |\n")
    else:
        f.write("| 1 | No recent submissions | - | - |\n")

    # ANALYTICS
    if recent_problems:
        f.write('\n## 🧠 Recent Analytics\n\n')
        for lang, count in lang_counts.items():
            f.write(f"- {lang}: {count}\n")
        for diff, count in diff_counts.items():
            if count > 0:
                f.write(f"- {diff}: {count}\n")

    # FOOTER
    now = datetime.datetime.utcnow().strftime("%b %d, %Y %H:%M UTC")
    f.write(f"\n\n---\n⏱ Updated: {now}\n")

print("✅ README generated successfully!")
