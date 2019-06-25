import random
#名詞の活用語尾
suf=[["a","ae","am","ae","a","ae","arum","as","is","is"],["us","i","um","o","o","i","orum","os","is","is"]\
     ,["um","i","um","o","o","a","orum","a","is","is"]]
#[変化の種類,意味,性別]
dic={"statu{}":[0,"像",0],"domin{}":[1,"主人",1],"verb{}":[2,"言葉",2],\
     "naut{}":[0,"水夫",1],"epistul{}":[0,"手紙",0],"serv{}":[1,"奴隷",1],"bell{}":[2,"戦争",2]}
n=["単数","複数"]
s=["主格","属格","対格","与格","奪格"]
print("次の名詞を、指示された格の形でラテン語で書け")
while True:
    A1=random.randint(0,1)
    A2=random.randint(0,4)
    num=n[A1]
    stat=s[A2]
    QWard=random.choice(list(dic.keys()))
    B=dic[QWard][0]
    QW=QWard.format(suf[B][0])
    QAns=QWard.format(suf[B][A1*5+A2])#答え
    ans=input("{0}({1})の{2}{3}\n".format(QW,dic[QWard][1],num,stat))
    if ans==QAns:
        print("正解")
    else:
        print("残念。正解は{}".format(QAns))
        #file=open("wrong.txt","a")
        #file.write("{0},{1},{2}\n".format(QW,A1,A2))
        #file.close()
