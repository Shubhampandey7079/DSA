import requests
import datetime

USERNAME = "8AdxLDYG0y"
GITHUB = "Shubhampandey7079"

# -------------------------------
# FETCH LEETCODE STATS
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
# PROGRESS BAR
# -------------------------------
def bar(val, total):
    p = int((val/total)*100) if total else 0
    fill = int(p/10)
    return f"{p}% " + "▓"*fill + "░"*(10-fill)

# -------------------------------
# WRITE README
# -------------------------------
with open("README.md", "w", encoding="utf-8") as f:

    # HERO SECTION
    f.write('<div align="center">\n')
    f.write(f'<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=36&duration=2500&pause=800&color=00F7FF&center=true&vCenter=true&width=900&lines=Hi+I%27m+Shubham+🚀;AI+Engineer+in+Making;{total}+LeetCode+Problems+Solved;Never+Stop+Grinding+🔥" />\n')
    f.write('</div>\n\n')

    # SOCIAL BADGES
    f.write('<div align="center">\n')
    f.write(f'<img src="https://img.shields.io/badge/LeetCode-{total}_Solved-orange?style=for-the-badge&logo=leetcode"/>\n')
    f.write(f'<img src="https://img.shields.io/badge/GitHub-{GITHUB}-black?style=for-the-badge&logo=github"/>\n')
    f.write('</div>\n\n')

    # ABOUT
    f.write("## 🧑‍💻 About Me\n")
    f.write("""
- 🚀 Aspiring **AI Engineer**
- 🧠 Focused on **DSA + Machine Learning**
- 🎯 Goal: Crack FAANG / Top Tech
- ⚡ Consistency > Motivation
\n""")

    # SKILLS
    f.write("## ⚙️ Tech Stack\n")
    f.write("""
- 💻 Languages: Python, C++
- 📊 DSA & Problem Solving
- 🤖 AI / ML (Learning Phase)
- 📱 Flutter Development
\n""")

    # PROGRESS
    f.write("## 📊 DSA Progress\n\n")
    f.write(f"🟢 Easy   → {bar(easy,200)} ({easy}/200)\n\n")
    f.write(f"🟡 Medium → {bar(medium,500)} ({medium}/500)\n\n")
    f.write(f"🔴 Hard   → {bar(hard,150)} ({hard}/150)\n\n")

    # LEETCODE CARD
    f.write("## 🧠 LeetCode Analytics\n\n")
    f.write(f'<img src="https://leetcard.jacoblin.cool/{USERNAME}?theme=dark&ext=heatmap" width="100%"/>\n\n')

    # GITHUB STATS
    f.write("## 📈 GitHub Stats\n\n")
    f.write(f'<img src="https://github-readme-stats.vercel.app/api?username={GITHUB}&show_icons=true&theme=tokyonight" height="170"/>')
    f.write(f'<img src="https://github-readme-stats.vercel.app/api/top-langs/?username={GITHUB}&layout=compact&theme=tokyonight" height="170"/>\n\n')

    f.write(f'<img src="https://streak-stats.demolab.com?user={GITHUB}&theme=tokyonight"/>\n\n')

    # ACTIVITY GRAPH
    f.write("## 📊 Contribution Graph\n\n")
    f.write(f'<img src="https://github-readme-activity-graph.vercel.app/graph?username={GITHUB}&theme=tokyo-night" width="100%"/>\n\n')

    # RECENT
    f.write("## 🕒 Recent Submissions\n\n")
    f.write("| # | Problem | Difficulty | Language |\n")
    f.write("|---|---------|------------|----------|\n")

    if recent_problems:
        for i, p in enumerate(recent_problems, 1):
            emoji = {"Easy":"🟢","Medium":"🟡","Hard":"🔴"}.get(p["difficulty"],"⚪")
            f.write(f"| {i} | [{p['title']}]({p['link']}) | {emoji} {p['difficulty']} | {p['lang']} |\n")
    else:
        f.write("| 1 | No recent submissions | - | - |\n")

    # CONTACT / CTA
    f.write("""
## 🌐 Connect With Me

- 💼 GitHub: https://github.com/{}
- 📧 Email: Shubhampandey707906@gmail.com

🚀 *Open for opportunities & collaborations*
\n""".format(GITHUB))

    # FOOTER
    now = datetime.datetime.utcnow().strftime("%b %d, %Y %H:%M UTC")
    f.write(f"\n---\n✨ Last Updated: {now}\n")

print("🔥 ULTIMATE README GENERATED")
