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
acceptance = stats.get("acceptanceRate", "N/A")
streak = stats.get("streak", 0)
contribution = stats.get("contributionPoints", 0)

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
            timestamp
        }
    }
    """,
    "variables": {"username": USERNAME, "limit": 6}
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
        ts = p.get("timestamp", 0)
        time_str = datetime.datetime.fromtimestamp(ts).strftime("%b %d") if ts else ""
        recent_problems.append({
            "title": p["title"],
            "link": f"https://leetcode.com/problems/{p['titleSlug']}/",
            "difficulty": p["difficulty"],
            "lang": p["lang"],
            "time": time_str
        })
except Exception:
    recent_problems = []

# -------------------------------
# PROGRESS BAR
# -------------------------------
def bar(val, total_val, color_hex):
    p = int((val/total_val)*100) if total_val else 0
    return f"![{p}%](https://progress-bar.dev/{p}/?width=400&color={color_hex})"

# -------------------------------
# WRITE README
# -------------------------------
with open("README.md", "w", encoding="utf-8") as f:

    # ========== HERO BANNER ==========
    f.write('<div align="center">\n\n')
    f.write('<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00F7FF&1:7B2FFF&2:C084FC&height=180&section=header&text=Shubham%20Pandey&fontSize=42&fontColor=ffffff&animation=twinkling&fontAlignY=35&desc=Aspiring%20AI%20Engineer%20%7C%20DSA%20Grinder%20%7C%20Full%20Stack%20Developer&descSize=18&descAlignY=55" width="100%" />\n\n')
    f.write('</div>\n\n')

    # ========== TYPING ANIMATION ==========
    f.write('<div align="center">\n')
    f.write('<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=28&duration=2500&pause=1000&color=00F7FF&center=true&vCenter=true&random=false&width=900&lines=Hi+%F0%9F%91%8B+I%27m+Shubham+Pandey;Aspiring+AI+Engineer+%F0%9F%A4%96;DSA+Grinder+%7C+%F0%9F%94%A5+Problems+Solved%3A+{};Consistency+is+the+Key+%E2%9A%A1" alt="Typing SVG" /></a>\n'.format(total))
    f.write('</div>\n\n')

    # ========== SOCIAL BADGES ==========
    f.write('<div align="center">\n')
    f.write(f'<a href="https://leetcode.com/{USERNAME}/"><img src="https://img.shields.io/badge/LeetCode-{total}_Solved-FFA116?style=for-the-badge&logo=leetcode&logoColor=black"/></a> ')
    f.write(f'<a href="https://github.com/{GITHUB}"><img src="https://img.shields.io/badge/GitHub-Shubham_Pandey-181717?style=for-the-badge&logo=github&logoColor=white"/></a> ')
    f.write(f'<a href="mailto:Shubhampandey707906@gmail.com"><img src="https://img.shields.io/badge/Email-Contact_Me-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/></a> ')
    f.write(f'<a href="https://linkedin.com/in/shubhampandey7079"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>\n')
    f.write('</div>\n\n')

    # ========== STATS CARDS ROW ==========
    f.write('<div align="center">\n\n')
    f.write('<table>\n')
    f.write('  <tr>\n')
    f.write(f'    <td><img src="https://img.shields.io/badge/Ranking-#{str(ranking) if isinstance(ranking, int) else "N/A"}-00F7FF?style=for-the-badge&logo=serverfault&logoColor=white"/></td>\n')
    f.write(f'    <td><img src="https://img.shields.io/badge/Streak-{streak}_Days-FF6B6B?style=for-the-badge&logo=fire&logoColor=white"/></td>\n')
    f.write(f'    <td><img src="https://img.shields.io/badge/Acceptance-{acceptance}%-C084FC?style=for-the-badge&logo=check-circle&logoColor=white"/></td>\n')
    f.write(f'    <td><img src="https://img.shields.io/badge/Contributions-{contribution}-2ECC71?style=for-the-badge&logo=codeforces&logoColor=white"/></td>\n')
    f.write('  </tr>\n')
    f.write('</table>\n\n')
    f.write('</div>\n\n')

    # ========== SEPARATOR ==========
    f.write('<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>\n\n')

    # ========== DSA PROGRESS TRACKER ==========
    f.write('<div align="center">\n')
    f.write('### 📊 DSA Progress Tracker\n\n')
    f.write('<table>\n')
    f.write('  <thead>\n')
    f.write('    <tr>\n')
    f.write('      <th align="center">Difficulty</th>\n')
    f.write('      <th align="center">Progress</th>\n')
    f.write('      <th align="center">Count</th>\n')
    f.write('    </tr>\n')
    f.write('  </thead>\n')
    f.write('  <tbody>\n')
    f.write(f'    <tr>\n')
    f.write(f'      <td align="center"><img src="https://img.shields.io/badge/🟢_Easy-2ECC71?style=flat-square"/></td>\n')
    f.write(f'      <td align="center">{bar(easy, 200, "2ECC71")}</td>\n')
    f.write(f'      <td align="center"><code>{easy}/200</code></td>\n')
    f.write(f'    </tr>\n')
    f.write(f'    <tr>\n')
    f.write(f'      <td align="center"><img src="https://img.shields.io/badge/🟡_Medium-F1C40F?style=flat-square"/></td>\n')
    f.write(f'      <td align="center">{bar(medium, 500, "F1C40F")}</td>\n')
    f.write(f'      <td align="center"><code>{medium}/500</code></td>\n')
    f.write(f'    </tr>\n')
    f.write(f'    <tr>\n')
    f.write(f'      <td align="center"><img src="https://img.shields.io/badge/🔴_Hard-E74C3C?style=flat-square"/></td>\n')
    f.write(f'      <td align="center">{bar(hard, 150, "E74C3C")}</td>\n')
    f.write(f'      <td align="center"><code>{hard}/150</code></td>\n')
    f.write(f'    </tr>\n')
    f.write('  </tbody>\n')
    f.write('</table>\n\n')
    f.write('</div>\n\n')

    # ========== LEETCARD ==========
    f.write('<div align="center">\n')
    f.write('### 🧠 LeetCode Analytics\n\n')
    f.write(f'<img src="https://leetcard.jacoblin.cool/{USERNAME}?theme=dark&ext=heatmap&font=JetBrains%20Mono" width="600"/>\n\n')
    f.write('</div>\n\n')

    # ========== SEPARATOR ==========
    f.write('<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>\n\n')

    # ========== GITHUB METRICS ==========
    f.write('<div align="center">\n')
    f.write('### 📈 GitHub Metrics\n\n')
    f.write(f'<img src="https://github-readme-stats.vercel.app/api?username={GITHUB}&show_icons=true&theme=tokyonight&hide_border=true&ring_color=00F7FF&icon_color=00F7FF&title_color=C084FC&bg_color=0D1117" height="180"/> ')
    f.write(f'<img src="https://github-readme-stats.vercel.app/api/top-langs/?username={GITHUB}&layout=compact&theme=tokyonight&hide_border=true&title_color=C084FC&text_color=FFFFFF&bg_color=0D1117" height="180"/>\n\n')
    f.write(f'<img src="https://streak-stats.demolab.com?user={GITHUB}&theme=tokyonight&hide_border=true&ring=00F7FF&fire=FF6B6B&currStreakLabel=C084FC&background=0D1117"/>\n\n')
    f.write('</div>\n\n')

    # ========== ACTIVITY GRAPH ==========
    f.write('<div align="center">\n')
    f.write(f'<img src="https://github-readme-activity-graph.vercel.app/graph?username={GITHUB}&bg_color=0D1117&color=C084FC&line=00F7FF&point=FFFFFF&area=true&hide_border=true&radius=8" width="100%"/>\n\n')
    f.write('</div>\n\n')

    # ========== SEPARATOR ==========
    f.write('<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>\n\n')

    # ========== TECH STACK ==========
    f.write('<div align="center">\n')
    f.write('### ⚡ Tech Arsenal\n\n')

    # Languages
    f.write('<details open>\n')
    f.write('<summary><b>💻 Programming Languages</b></summary>\n')
    f.write('<br>\n')
    f.write('<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/> ')
    f.write('<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white"/>\n')
    f.write('<br><br>\n')
    f.write('</details>\n\n')

    # Frontend
    f.write('<details open>\n')
    f.write('<summary><b>🎨 Frontend Development</b></summary>\n')
    f.write('<br>\n')
    f.write('<img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB"/> ')
    f.write('<img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>\n')
    f.write('<br><br>\n')
    f.write('</details>\n\n')

    # Backend
    f.write('<details open>\n')
    f.write('<summary><b>⚙️ Backend Development</b></summary>\n')
    f.write('<br>\n')
    f.write('<img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/Express.js-000000?style=for-the-badge&logo=express&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/REST_API-FF6C37?style=for-the-badge&logo=postman&logoColor=white"/>\n')
    f.write('<br><br>\n')
    f.write('</details>\n\n')

    # Databases
    f.write('<details open>\n')
    f.write('<summary><b>🗄️ Databases</b></summary>\n')
    f.write('<br>\n')
    f.write('<img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white"/>\n')
    f.write('<br><br>\n')
    f.write('</details>\n\n')

    # Tools
    f.write('<details open>\n')
    f.write('<summary><b>🛠️ Tools & Platforms</b></summary>\n')
    f.write('<br>\n')
    f.write('<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"/> ')
    f.write('<img src="https://img.shields.io/badge/VS_Code-0078D4?style=for-the-badge&logo=visualstudiocode&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white"/> ')
    f.write('<img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white"/>\n')
    f.write('<br><br>\n')
    f.write('</details>\n\n')

    f.write('</div>\n\n')

    # ========== SEPARATOR ==========
    f.write('<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>\n\n')

    # ========== RECENT SUBMISSIONS ==========
    f.write('<div align="center">\n')
    f.write('### 🕒 Recent LeetCode Submissions\n\n')
    f.write('<table>\n')
    f.write('  <thead>\n')
    f.write('    <tr>\n')
    f.write('      <th>#</th>\n')
    f.write('      <th>Problem</th>\n')
    f.write('      <th>Difficulty</th>\n')
    f.write('      <th>Language</th>\n')
    f.write('      <th>Solved</th>\n')
    f.write('    </tr>\n')
    f.write('  </thead>\n')
    f.write('  <tbody>\n')

    if recent_problems:
        color_map = {"Easy": "2ECC71", "Medium": "F1C40F", "Hard": "E74C3C"}
        for i, p in enumerate(recent_problems, 1):
            hex_color = color_map.get(p["difficulty"], "95A5A6")
            f.write(f'    <tr>\n')
            f.write(f'      <td align="center"><b>{i}</b></td>\n')
            f.write(f'      <td><a href="{p["link"]}" target="_blank" style="color:00F7FF;text-decoration:none;">{p["title"]}</a></td>\n')
            f.write(f'      <td align="center"><img src="https://img.shields.io/badge/{p["difficulty"]}-{hex_color}?style=flat-square"/></td>\n')
            f.write(f'      <td align="center"><code>{p["lang"]}</code></td>\n')
            f.write(f'      <td align="center"><sub>{p["time"]}</sub></td>\n')
            f.write(f'    </tr>\n')
    else:
        f.write('    <tr><td colspan="5" align="center">No recent submissions found</td></tr>\n')

    f.write('  </tbody>\n')
    f.write('</table>\n\n')
    f.write('</div>\n\n')

    # ========== SEPARATOR ==========
    f.write('<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>\n\n')

    # ========== CONNECT SECTION ==========
    f.write('<div align="center">\n')
    f.write('### 🌐 Let\'s Connect\n\n')
    f.write('<table>\n')
    f.write('  <tr>\n')
    f.write(f'    <td><a href="https://github.com/{GITHUB}"><img src="https://img.shields.io/badge/GitHub-Follow_me-181717?style=for-the-badge&logo=github"/></a></td>\n')
    f.write('    <td><a href="mailto:Shubhampandey707906@gmail.com"><img src="https://img.shields.io/badge/Email-Drop_a_Hi-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/></a></td>\n')
    f.write('    <td><a href="https://linkedin.com/in/shubhampandey7079"><img src="https://img.shields.io/badge/LinkedIn-Let\'s_Talk-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a></td>\n')
    f.write('  </tr>\n')
    f.write('</table>\n\n')
    f.write('</div>\n\n')

    # ========== QUOTE ==========
    f.write('<div align="center">\n')
    f.write('<img src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=tokyonight" />\n\n')
    f.write('</div>\n\n')

    # ========== FOOTER ==========
    f.write('<div align="center">\n\n')
    f.write('<img src="https://capsule-render.vercel.app/api?type=waving&color=0:C084FC&1:7B2FFF&2:00F7FF&height=120&section=footer" width="100%"/>\n\n')
    now = datetime.datetime.utcnow().strftime("%b %d, %Y %H:%M UTC")
    f.write(f'<sub>✨ Profile last synced on: <b>{now}</b></sub>\n\n')
    f.write('</div>\n')

print("🔥 ULTIMATE NEON README GENERATED SUCCESSFULLY")
