import requests
import datetime

USERNAME = "YOUR_LEETCODE_USERNAME"
GITHUB = "YOUR_GITHUB_USERNAME"

url = f"https://leetcode-stats-api.herokuapp.com/{USERNAME}"
data = requests.get(url).json()

total = data.get("totalSolved", 0)
easy = data.get("easySolved", 0)
medium = data.get("mediumSolved", 0)
hard = data.get("hardSolved", 0)
ranking = data.get("ranking", "N/A")

def bar(x):
    return "█" * (x // 10)

with open("README.md", "w") as f:
    f.write("# 🚀 ULTRA PRO LeetCode Dashboard\n\n")

    f.write(f"👤 Username: {USERNAME}\n")
    f.write(f"🏆 Ranking: {ranking}\n\n")

    f.write("## 📊 Stats\n")
    f.write(f"✅ Total Solved: {total}\n\n")
    f.write(f"🟢 Easy: {easy}\n")
    f.write(f"🟡 Medium: {medium}\n")
    f.write(f"🔴 Hard: {hard}\n\n")

    f.write("## 📈 Progress\n")
    f.write(f"Easy   [{bar(easy)}]\n")
    f.write(f"Medium [{bar(medium)}]\n")
    f.write(f"Hard   [{bar(hard)}]\n\n")

    f.write("## 🔥 Streak & Activity\n")
    f.write(f"![Streak](https://streak-stats.demolab.com/?user={GITHUB})\n\n")

    f.write("## 📊 Graph\n")
    f.write(f"![Graph](https://github-readme-activity-graph.vercel.app/graph?username={GITHUB})\n\n")

    f.write("## 🔥 LeetCode Heatmap\n")
    f.write(f"![Heatmap](https://leetcard.jacoblin.cool/{USERNAME}?ext=heatmap)\n\n")

    f.write("## 📊 Stats Card\n")
    f.write(f"![Stats](https://github-readme-stats.vercel.app/api?username={GITHUB})\n\n")

    f.write(f"⏱ Last Updated: {datetime.datetime.now()}\n")
