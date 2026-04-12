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

# Headers are REQUIRED, otherwise LeetCode blocks the script as a bot
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
        # Create clickable markdown links
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
# Instead of guessing topics from titles, track actual Language & Difficulty stats
lang_counts = {}
diff_counts = {"Easy": 0, "Medium": 0, "Hard": 0}

for p in recent_problems:
    lang = p["lang"]
    diff = p["difficulty"]
    
    lang_counts[lang] = lang_counts.get(lang, 0) + 1
    diff_counts[diff] = diff_counts.get(diff, 0) + 1

# -------------------------------
# 4. WRITE README
# -------------------------------
with open("README.md", "w") as f:
    
    # Header & Badges
    f.write('<h1 align="center">🚀 LeetCode Dashboard</h1>\n\n')
    f.write('<p align="center">\n')
    f.write(f'  <img src="https://img.shields.io/badge/Username-{USERNAME}-orange?style=for-the-badge&logo=leetcode" />\n')
    f.write(f'  <img src="https://img.shields.io/badge/Ranking-{ranking}-blue?style=for-the-badge" />\n')
    f.write(f'  <img src="https://img.shields.io/badge/Total_Solved-{total}-green?style=for-the-badge" />\n')
    f.write(f'  <img src="https://img.shields.io/badge/Acceptance-{acceptance}%25-brightgreen?style=for-the-badge" />\n')
    f.write('</p>\n\n')

    # Auto-update trigger (Visible only if run via GitHub Actions)
    f.write('<details>\n<summary>⚡ Automation Info</summary>\n\n')
    f.write(f'_⏱ Dashboard auto-updated on: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")}_\n\n')
    f.write('</details>\n\n')

    # ---------------------------
    # UI Cards (Moved to top for better visual hierarchy)
    # ---------------------------
    f.write('## 🔥 GitHub Stats\n\n')
    f.write('<p align="center">\n')
    f.write(f'  <img src="https://github-readme-stats.vercel.app/api?username={GITHUB}&show_icons=true&theme=tokyonight&hide_border=true" height="180"/>\n')
    f.write(f'  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={GITHUB}&layout=compact&theme=tokyonight&hide_border=true&langs_count=8" height="180"/>\n')
    f.write('</p>\n\n')
    
    f.write('<p align="center">\n')
    f.write(f'  <img src="https://streak-stats.demolab.com/?user={GITHUB}&theme=tokyonight&hide_border=true" />\n')
    f.write('</p>\n\n')

    f.write('<p align="center">\n')
    f.write(f'  <img src="https://github-readme-activity-graph.vercel.app/graph?username={GITHUB}&bg_color=1a1b27&color=70a5fd&line=38bdf8&point=38bdf8&area=true&hide_border=true" />\n')
    f.write('</p>\n\n')

    # ---------------------------
    # LeetCode Progress
    # ---------------------------
    f.write('## 📊 LeetCode Progress\n\n')
    
    # Custom Progress Bars using HTML/CSS
    def progress_bar(solved, total_out_of, color):
        percent = (solved / total_out_of) * 100 if total_out_of > 0 else 0
        return f'<img src="https://img.shields.io/badge/{solved}/{total_out_of}-{color}?style=flat-square" />'

    # Note: You can adjust the "/X" numbers to your actual goal (e.g., 500/800 Easy)
    f.write(f'- 🟢 Easy: {progress_bar(easy, 800, "success")}\n')
    f.write(f'- 🟡 Medium: {progress_bar(medium, 1500, "yellow")}\n')
    f.write(f'- 🔴 Hard: {progress_bar(hard, 500, "critical")}\n\n')

    f.write(f'![Heatmap](https://leetcard.jacoblin.cool/{USERNAME}?ext=heatmap&theme=dark&font=Lato)\n\n')

    # ---------------------------
    # Recent Problems (Clickable & Clean)
    # ---------------------------
    f.write('## 🕒 Recent Submissions\n\n')
    f.write('| # | Problem | Difficulty | Language |\n')
    f.write('|:---:|---------|:----------:|:--------:|\n')

    if recent_problems:
        for idx, p in enumerate(recent_problems, 1):
            # Add emojis based on difficulty for visual pop
            diff_emoji = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}.get(p["difficulty"], "⚪")
            f.write(f'| {idx} | [{p["title"]}]({p["link"]}) | {diff_emoji} {p["difficulty"]} | `{p["lang"]}` |\n')
    else:
        f.write('| 1 | _No recent submissions found_ | - | - |\n')

    f.write('\n')

    # ---------------------------
    # Recent Analytics (Accurate Data)
    # ---------------------------
    f.write('## 🧠 Recent Analytics (Last 5 Solves)\n\n')
    
    f.write('**Language Distribution:**\n')
    for lang, count in lang_counts.items():
        f.write(f'- `{lang}`: {count} solve{"s" if count > 1 else ""}\n')
        
    f.write('\n**Difficulty Breakdown:**\n')
    for diff, count in diff_counts.items():
        if count > 0:
            f.write(f'- {diff}: {count} solve{"s" if count > 1 else ""}\n')
            
    f.write('\n---\n')
    f.write(f'<p align="center"><i>Built with ❤️ by <a href="https://github.com/{GITHUB}">{GITHUB}</a></i></p>\n')

print("✅ README.md generated successfully!")
