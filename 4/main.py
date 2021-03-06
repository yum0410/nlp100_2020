# 30
import MeCab
file_name = "neko.txt"
parsed_file_name = "neko.txt.mecab"

def parse_neko():
    with open(file_name) as f, open(parsed_file_name, mode="w") as out:
            mecab = MeCab.Tagger()
            out.write(mecab.parse(f.read()))

# 形態素解析
parse_neko()

# 30
def split_parse_text():
    with open(parsed_file_name) as f:
        morphemes = []
        for line in f:
            cols = line.split("\t")
            if len(cols) < 2:
                break
            res_cols = cols[1].split(",")

            morpheme = {
                "surface": cols[0],
                "base": res_cols[6],
                "pos": res_cols[0],
                "pos1": res_cols[1]
            }
            morphemes.append(morpheme)

            if res_cols[1] == "句点":
                yield morphemes
                morphemes = []

parse_neko_text = split_parse_text()

# 31
verbs = []
for line in parse_neko_text:
    for morpheme in line:
        if morpheme["pos"] == "動詞":
            verbs.append(morpheme["surface"])
# print(sorted(set(verbs)))

# 32
parse_neko_text = split_parse_text()
verbs = []
for line in parse_neko_text:
    for morpheme in line:
        if morpheme["pos"] == "動詞":
            verbs.append(morpheme["base"])
# print(sorted(set(verbs)))

# 33
parse_neko_text = split_parse_text()
noun_phrase = []
for line in parse_neko_text:
    for i in range(len(line)-3):
        if line[i]["pos"] == "名詞" and line[i+1]["surface"] == "の" and line[i+2]["pos"] == "名詞":
            noun_phrase.append(line[i]["surface"]+line[i+1]["surface"]+line[i+2]["surface"])
# print(sorted(set(noun_phrase)))

# 34
parse_neko_text = split_parse_text()
noun_phrase = []
for line in parse_neko_text:
    join_noun = []
    for l in line:
        if l["pos"] == "名詞":
            join_noun.append(l["surface"])
        else:
            if len(join_noun) > 1:
                noun_phrase.append("".join(join_noun))
                join_noun = []
    else:
        if len(join_noun) > 1:
            noun_phrase.append("".join(join_noun))
# print(sorted(set(noun_phrase)))

# 35
from collections import Counter
parse_neko_text = split_parse_text()
words = []
for line in parse_neko_text:
    for l in line:
        words.append(l["surface"])
# print(Counter(words).most_common())

# 36
import matplotlib.pyplot as plt
TOP10 = Counter(words).most_common(10)
plt.bar([x[0] for x in TOP10], [x[1] for x in TOP10])
