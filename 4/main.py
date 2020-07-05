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
print(sorted(set(verbs)))