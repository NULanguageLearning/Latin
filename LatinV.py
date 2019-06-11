import random
#動詞の活用語尾
suf=[["o","as","at","amus","atis","ant"],["o","s","t","mus","tis","nt"]\
     ,["o","is","it","imus","itis","unt"],["o","s","t","mus","tis","unt"],["o","s","t","mus","tis","unt"]]
#[変化の種類,意味]
dic={"am{}":[0,"愛する"],"can{}":[2,"歌う"],"habe{}":[1,"持つ"],"capi{}":[3,"捕らえる"],\
     "audi{}":[4,"聞く"],"voc{}":[0,"呼ぶ"],"vide{}":[2,"見る"],"veni{}":[3,"来る"]}
q=["一人称単数","二人称単数","三人称単数","一人称複数","二人称複数","三人称複数"]
print("次の動詞を現在形、能動相で、指示された形でラテン語で書け")
while True:
    A=random.randint(0,5)
    Question=q[A]
    QWard=random.choice(list(dic.keys()))
    QW=QWard.format("o")
    B=dic[QWard][0]
    QAns=QWard.format(suf[B][A])#答え
    ans=input("{0}({1})の{2}形\n".format(QW,dic[QWard][1],Question))
    if ans==QAns:
        print("正解")
    else:
        print("残念。正解は{}".format(QAns))
