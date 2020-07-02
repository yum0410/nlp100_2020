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
        # print(re.search(pattern, line).group(1))
        pass

# 23
pattern = "^(=+)\s*(.*?)\s*(=+)"
for line in data20["text"].split("\n"):
    section_line = re.search(pattern, line) 
    if section_line is not None:
        # print(section_line.group(2), len(section_line.group(1))-1)
        pass

# 24
pattern = "(ファイル):(.*?)\|"
for line in data20["text"].split("\n"):
    section_line = re.search(pattern, line) 
    if section_line is not None:
        # print(section_line.group(2))
        pass

# 25
import pprint
from collections import OrderedDict
p1 = re.compile("\{\{基礎情報")
p2 = re.compile("\|(?P<key>.*?)=(?P<value>.*)")
p3 = re.compile("^\}\}")
base_info_flag = False
template_list = []
for line in data20["text"].split("\n"):
    if p1.match(line):
        base_info_flag = True
    if base_info_flag:
        data = p3.match(line)
        if p2.match(line):
            template_list.append((p2.match(line).group(1), p2.match(line).group(2)))
        elif p3.match(line):
            break
pprint.pprint(OrderedDict(template_list))