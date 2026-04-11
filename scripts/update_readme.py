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
except:
    stats = {}

total = stats.get("totalSolved", 0)
easy = stats.get("easySolved", 0)
medium = stats.get("mediumSolved", 0)
hard = stats.get("hardSolved", 0)
ranking = stats.get("ranking", "N/A")

# -------------------------------
# 2. RECENT SUBMISSIONS (GraphQL)
# -------------------------------
recent_url = "https://leetcode.com/graphql"

query = {
    "query": """
    query recentAcSubmissions($username: String!) {
        recentAcSubmissionList(username: $username) {
            title
            difficulty
            lang
        }
    }
    """,
    "variables": {"username": USERNAME}
}

recent_problems = []

try:
    res = requests.post(recent_url, json=query, timeout=10)
    data = res.json()
    recent = data["data"]["recentAcSubmissionList"]

    for p in recent[:5]:
        recent_problems.append((p["title"], p["difficulty"], p["lang"]))
except:
    recent_problems = []

# -------------------------------
# 3. TOPIC DETECTION (BASIC)
# -------------------------------
topics = {
    "Array": 0,
    "String": 0,
    "DP": 0,
    "Graph": 0
}

for p in recent_problems:
    name = p[0].lower()

    if "array" in name:
        topics["Array"] += 1
    elif "string" in name:
        topics["String"] += 1
    elif "graph" in name:
        topics["Graph"] += 1
    else:
        topics["DP"] += 1

# -------------------------------
# 4. WRITE README
# -------------------------------
with open("README.md", "w") as f:
    f.write("# 🚀 LeetCode Dashboard\n\n")

    f.write(f"👤 Username: {USERNAME}\n")
    f.write(f"🏆 Ranking: {ranking}\n\n")

    f.write("## 📊 Stats\n")
    f.write(f"✅ Total: {total}\n")
    f.write(f"🟢 Easy: {easy}\n")
    f.write(f"🟡 Medium: {medium}\n")
    f.write(f"🔴 Hard: {hard}\n\n")

    # ---------------------------
    # Recent Problems
    # ---------------------------
    f.write("## 📌 Recent Submissions\n")
    f.write("| Problem | Difficulty | Language |\n")
    f.write("|--------|------------|----------|\n")

    if recent_problems:
        for p in recent_problems:
            f.write(f"| {p[0]} | {p[1]} | {p[2]} |\n")
    else:
        f.write("| No data | - | - |\n")

    f.write("\n")

    # ---------------------------
    # Topics
    # ---------------------------
    f.write("## 🧠 Topic Breakdown\n")
    for k, v in topics.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n")

    # ---------------------------
    # UI CARDS
    # ---------------------------
    f.write("## 🔥 Stats Cards\n")
    f.write(f"![Stats](https://github-readme-stats.vercel.app/api?username={GITHUB}&show_icons=true&theme=tokyonight)\n\n")

    f.write(f"![Streak](https://streak-stats.demolab.com/?user={GITHUB}&theme=tokyonight)\n\n")

    f.write("## 📊 Activity Graph\n")
    f.write(f"![Graph](https://github-readme-activity-graph.vercel.app/graph?username={GITHUB}&theme=tokyo-night)\n\n")

    f.write("## 🔥 LeetCode Heatmap\n")
    f.write(f"![Heatmap](https://leetcard.jacoblin.cool/{USERNAME}?ext=heatmap)\n\n")

    f.write(f"⏱ Last Updated: {datetime.datetime.now()}\n")
