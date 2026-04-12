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
except Exception:
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
except Exception:
    recent_problems = []

# -------------------------------
# PROGRESS BAR
# -------------------------------
def bar(val, total_val, color_hex):
    p = int((val/total_val)*100) if total_val else 0
    fill = int(p/10)
    return f"![{p}%](https://progress-bar.dev/{p}/?width=400&color={color_hex})"

# -------------------------------
# WRITE README
# -------------------------------
with open("README.md", "w", encoding="utf-8") as f:

    # HERO SECTION
    f.write('<div align="center">\n')
    f.write('<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=32&duration=2500&pause=1000&color=00F7FF&center=true&vCenter=true&random=false&width=900&lines=Hi+%F0%9F%91%8B+I%27m+Shubham+Pandey;Aspiring+AI+Engineer+%F0%9F%A4%96;DSA+Grinder+%7C+%F0%9F%94%A5+Problems+Solved%3A+{};Consistency+is+the+Key+%E2%9A%A1" alt="Typing SVG" /></a>\n'.format(total))
    f.write('</div>\n\n')

    # SOCIAL BADGES
    f.write('<div align="center">\n')
    f.write(f'<a href="https://leetcode.com/{USERNAME}/"><img src="https://img.shields.io/badge/LeetCode-{total}_Solved-FFA116?style=for-the-badge&logo=leetcode&logoColor=black"/></a> ')
    f.write(f'<a href="https://github.com/{GITHUB}"><img src="https://img.shields.io/badge/GitHub-Shubham_Pandey-181717?style=for-the-badge&logo=github&logoColor=white"/></a> ')
    f.write(f'<img src="https://img.shields.io/badge/Ranking-#{str(ranking) if isinstance(ranking, int) else "N/A"}-2196F3?style=for-the-badge&logo=serverfault&logoColor=white"/>\n')
    f.write('</div>\n\n')

    # ABOUT ME (With Blockquote styling)
    f.write('> ### 🧑‍💻 About Me\n')
    f.write('> - 🚀 Transforming lines of code into intelligent AI solutions.\n')
    f.write('> - 🧠 Deep-diving into **Machine Learning** & **Data Structures**.\n')
    f.write('> - 🎯 Target: SDE / AI Engineer at Top Product-Based Companies.\n')
    f.write('> - ⚡ I don\'t count the days, I make the days count.\n\n')

    # TECH STACK (Using sleek badges)
    f.write('### ⚙️ Tech Arsenal\n\n')
    f.write('<div align="center">\n')
    # Languages
    f.write('<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=c%2B%2B&logoColor=white"/> ')
    # Frameworks & Tools
    f.write('<img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white"/><br><br>\n')
    # AI/ML
    f.write('<img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/scikit_learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white"/>\n')
    f.write('</div>\n\n')

    # DSA PROGRESS (Using progress-bar.dev for crisp visuals)
    f.write('### 📊 DSA Progress Tracker\n\n')
    f.write('| Difficulty | Progress | Count |\n')
    f.write('|:-----------|:--------:|:-----:|\n')
    f.write(f'| 🟢 Easy   | {bar(easy, 200, "2ECC71")} | {easy}/200 |\n')
    f.write(f'| 🟡 Medium | {bar(medium, 500, "F1C40F")} | {medium}/500 |\n')
    f.write(f'| 🔴 Hard   | {bar(hard, 150, "E74C3C")} | {hard}/150 |\n\n')

    # LEETCARD
    f.write('<div align="center">\n')
    f.write('### 🧠 LeetCode Analytics\n')
    f.write(f'<img src="https://leetcard.jacoblin.cool/{USERNAME}?theme=dark&ext=heatmap&font=JetBrains%20Mono" width="600"/>\n')
    f.write('</div>\n\n')

    # GITHUB STATS (Side by Side)
    f.write('<div align="center">\n')
    f.write('### 📈 GitHub Metrics\n')
    f.write(f'<img src="https://github-readme-stats.vercel.app/api?username={GITHUB}&show_icons=true&theme=tokyonight&hide_border=true&ring_color=00F7FF&icon_color=00F7FF&title_color=C084FC" height="170"/> ')
    f.write(f'<img src="https://github-readme-stats.vercel.app/api/top-langs/?username={GITHUB}&layout=compact&theme=tokyonight&hide_border=true&title_color=C084FC&text_color=FFFFFF" height="170"/>\n\n')
    f.write(f'<img src="https://streak-stats.demolab.com?user={GITHUB}&theme=tokyonight&hide_border=true&ring=00F7FF&fire=FF6B6B&currStreakLabel=C084FC"/>\n')
    f.write('</div>\n\n')

    # ACTIVITY GRAPH
    f.write('<div align="center">\n')
    f.write(f'<img src="https://github-readme-activity-graph.vercel.app/graph?username={GITHUB}&bg_color=0D1117&color=C084FC&line=00F7FF&point=FFFFFF&area=true&hide_border=true" width="100%"/>\n')
    f.write('</div>\n\n')

    # RECENT SUBMISSIONS (Styled Table)
    f.write('### 🕒 Recent LeetCode Submissions\n\n')
    f.write('<table align="center">\n')
    f.write('<thead>\n')
    f.write('  <tr>\n')
    f.write('    <th>#</th>\n')
    f.write('    <th>Problem</th>\n')
    f.write('    <th>Difficulty</th>\n')
    f.write('    <th>Language</th>\n')
    f.write('  </tr>\n')
    f.write('</thead>\n')
    f.write('<tbody>\n')

    if recent_problems:
        for i, p in enumerate(recent_problems, 1):
            color_map = {"Easy": "2ECC71", "Medium": "F1C40F", "Hard": "E74C3C"}
            hex_color = color_map.get(p["difficulty"], "95A5A6")
            f.write(f'  <tr>\n')
            f.write(f'    <td align="center">{i}</td>\n')
            f.write(f'    <td><a href="{p["link"]}" target="_blank">{p["title"]}</a></td>\n')
            f.write(f'    <td align="center"><img src="https://img.shields.io/badge/{p["difficulty"]}-{hex_color}?style=flat-square"/></td>\n')
            f.write(f'    <td align="center">{p["lang"]}</td>\n')
            f.write(f'  </tr>\n')
    else:
        f.write('  <tr><td colspan="4" align="center">No recent submissions found</td></tr>\n')

    f.write('</tbody>\n')
    f.write('</table>\n\n')

    # CONNECT WITH ME
    f.write('<div align="center">\n')
    f.write('### 🌐 Let\'s Connect\n')
    f.write(f'<a href="https://github.com/{GITHUB}"><img src="https://img.shields.io/badge/GitHub-Follow_me-181717?style=for-the-badge&logo=github"/></a> ')
    f.write('<a href="mailto:Shubhampandey707906@gmail.com"><img src="https://img.shields.io/badge/Email-Drop_a_Hi-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/></a>\n')
    f.write('</div>\n\n')

    # FOOTER
    now = datetime.datetime.utcnow().strftime("%b %d, %Y %H:%M UTC")
    f.write('<div align="center">\n')
    f.write('---\n')
    f.write(f'<sub>✨ Profile last synced on: <b>{now}</b></sub>\n')
    f.write('</div>\n')

print("🔥 ULTIMATE NEON README GENERATED SUCCESSFULLY")
