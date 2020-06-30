# 20
import json
data20 = ""
with open("jawiki-country.json", encoding="utf-8") as f:
    for line in f:
        if json.loads(line)["title"] == "イギリス":
            data20 = json.loads(line)
# print(data20["text"])

# 21
for line in data20["text"].split("\n"):
    if "Category" in line:
        # print(line)
        pass

# 22
import re
pattern = "^\[\[Category:(.*?)(|\|.*)\]\]$"
for line in data20["text"].split("\n"):
    if re.search(pattern, line):
        print(re.search(pattern, line).group(1))

