import requests
import datetime

USERNAME = "8AdxLDYG0y"
GITHUB = "Shubhampandey7079"

# ✅ Stable API
url = f"https://leetcode-api-faisalshohag.vercel.app/{USERNAME}"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200 and response.text.strip():
        try:
            data = response.json()
        except:
            print("Invalid JSON")
            data = {}
    else:
        print("API failed")
        data = {}

except Exception as e:
    print("Request error:", e)
    data = {}

# ✅ Safe extraction
total = data.get("totalSolved", 0)
easy = data.get("easySolved", 0)
medium = data.get("mediumSolved", 0)
hard = data.get("hardSolved", 0)
ranking = data.get("ranking", "N/A")

with open("README.md", "w") as f:
    f.write("# 🚀 LeetCode Dashboard\n\n")
    f.write(f"👤 Username: {USERNAME}\n")
    f.write(f"🏆 Ranking: {ranking}\n\n")

    f.write(f"✅ Total Solved: {total}\n\n")
    f.write(f"🟢 Easy: {easy}\n")
    f.write(f"🟡 Medium: {medium}\n")
    f.write(f"🔴 Hard: {hard}\n\n")

    f.write("## 🔥 Stats Cards\n")
    f.write(f"![Stats](https://github-readme-stats.vercel.app/api?username={GITHUB})\n\n")

    f.write("## 📊 Heatmap\n")
    f.write(f"![Heatmap](https://leetcard.jacoblin.cool/{USERNAME}?ext=heatmap)\n\n")

    f.write(f"⏱ Last Updated: {datetime.datetime.now()}\n")
