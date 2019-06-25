"""
読み込むテキストファイルは行ごとに読み込みます。行ごとに

ラテン語,変化の種類,日本語での意味

を読み取ります。ラテン語の活用語尾は{}になってます。

活用の種類の指定については、語尾が次のようになる語を
0→"o","as","at","amus","atis","ant"（第一変化動詞）
1→"o","s","t","mus","tis","nt"（第二変化動詞）
2→"o","is","it","imus","itis","unt"（第三変化動詞a）
3→"o","s","t","mus","tis","unt"（第三変化動詞b）
4→"o","s","t","mus","tis","unt"（第四変化動詞）
"""

import random
#動詞の活用語尾
hutei=["are","re","ere","ere","ire"]
suf=[["o","as","at","amus","atis","ant"],["o","s","t","mus","tis","nt"]\
     ,["o","is","it","imus","itis","unt"],["io","is","it","imus","itis","iunt"],["o","s","t","mus","tis","unt"]]
q=["一人称単数","二人称単数","三人称単数","一人称複数","二人称複数","三人称複数"]
dic={}
file=open("dicV.txt","r")
f=file.read()
file.close()
f1=f.split("\n")
while "" in f1:
    f1.remove("")

for i in range(len(f1)):
	f1[i]=f1[i].split(",")
for a in f1:
    dic[a[0]]=[int(a[1]),a[2]]



print("次の動詞を現在形、能動相で、指示された形でラテン語で書け")
while True:
    A=random.randint(0,5)
    Question=q[A]
    QWard=random.choice(list(dic.keys()))
    B=dic[QWard][0]
    QW=QWard.format(hutei[B])
    QAns=QWard.format(suf[B][A])#答え
    ans=input("{0}({1})の{2}形\n".format(QW,dic[QWard][1],Question))
    if ans==QAns:
        print("正解")
    else:
        print("残念。正解は{}".format(QAns))
