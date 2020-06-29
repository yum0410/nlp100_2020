# 00
data00 = "stressed"
print(data00[::-1])

# 01
data01 = "パタトクカシーー"
print("".join([x for i, x in enumerate(data01) if i%2==0]))

# 02
print("".join([x + y for x, y in zip("パトカー", "タクシー")]))

# 03
data03 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print([len(x) for x in data03.split(" ")])

# 04
from collections import defaultdict
data04 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
one_id = [1, 5, 6, 7, 8, 9, 15, 16, 19]
result_04 = defaultdict(int)
for i, x in enumerate(data04.split(" ")):
    if i+1 in one_id:
        result_04[x[:1]] = i+1
    else:
        result_04[x[:2]] = i+1
print(result_04)

# 05
data05 = "I am an NLPer"
words = data05.split(" ")
print([words[i] +"-"+ words[i+1] for i in range(0, len(words)-1)])
print([data05[i] +"-"+ data05[i+1] for i in range(0, len(data05)-1)])

# 06
data06_X = "paraparaparadise"
data06_Y = "paragraph"
X = [data06_X[i] +"-"+ data06_X[i+1] for i in range(0, len(data06_X)-1)]
Y = [data06_Y[i] +"-"+ data06_Y[i+1] for i in range(0, len(data06_Y)-1)]
print("和", set(X + Y))
print("積", set(X) & set(Y))
print("差", set(X) - set(Y))
print("X has se:", "s-e" in X)
print("Y has se:", "s-e" in Y)

# 07
def func07(x, y, z):
    return "{}時の{}は{}".format(x, y, z)
print(func07(x=12, y="気温", z=22.4))

# 08
def cipher(text):
    # convert ascii char number
    return "".join([chr(219 - ord(x)) if x.islower() else x for x in text])
print(cipher("title：NLP100本ノック-lesson08"))

# 09
import random
def typoglycemia(word):
    if len(word) > 4:
        random.seed(0)
        return word[0]+"".join(random.sample(word[1:-1], len(word[1:-1])))+word[-1]
    return word
data09 = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(" ".join(map(typoglycemia, data09.split(" "))))
