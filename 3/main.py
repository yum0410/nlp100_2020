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
# pprint.pprint(OrderedDict(template_list))

# 26
template_list_drop_markup = []
for x in template_list:
    template_list_drop_markup.append((x[0].strip(), re.sub("'{2,5}", "", x[1].strip())))
template_list_drop_markup = OrderedDict(template_list_drop_markup)
# pprint.pprint(template_list_drop_markup)

# 27
template_list_drop_internal_link = []
p1 = re.compile("\[\[(?:[^|]*?\|)??([^|]*?)\]\]", re.MULTILINE + re.VERBOSE)
for key, value in template_list_drop_markup.items():
    if p1.search(value):
        template_list_drop_internal_link.append((key, p1.sub(r'\1', value)))
    else:
        template_list_drop_internal_link.append((key, value))
template_list_drop_internal_link = OrderedDict(template_list_drop_internal_link)
pprint.pprint(template_list_drop_internal_link)

# 28
# 外部リンクの除去  [http://xxxx] 、[http://xxx xxx]
template_list_drop_outer_link = []
p1 = re.compile("\[http:\/\/(?:[^\s]*?\s)?([^]]*?)\]", re.MULTILINE + re.VERBOSE)
for key, value in template_list_drop_internal_link.items():
    if p1.search(value):
        template_list_drop_outer_link.append((key, p1.sub(r'\1', value)))
    else:
        template_list_drop_outer_link.append((key, value))
template_list_drop_outer_link = OrderedDict(template_list_drop_outer_link)
# <br>、<ref>の除去
p2 = re.compile("<\/?[br|ref][^>]*?>")
for key, value in template_list_drop_outer_link.items():
    if p2.search(value):
        template_list_drop_outer_link[key] = p2.sub("", value)
    else:
        template_list_drop_outer_link[key] = value
pprint.pprint(template_list_drop_outer_link)
