import random
#名詞の活用語尾
suf=[["a","ae","am","ae","a","ae","arum","as","is","is"],["us","i","um","o","o","i","orum","os","is","is"]\
     ,["um","i","um","o","o","a","orum","a","is","is"]]
n=["単数","複数"]
s=["主格","属格","対格","与格","奪格"]
dic={}
def makedic(read):
    file=open(read,"r")
    f=file.read()
    file.close()
    f1=f.split("\n")
    while "" in f1:
        f1.remove("")
    for i in range(len(f1)):
            f1[i]=f1[i].split(",")
    for a in f1:
        dic[a[0]]=[int(a[1]),a[2],int(a[3])]

makedic("dicN.txt")
print("次の名詞を、指示された格の形でラテン語で書け")
while True:
    A1=random.randint(0,1)
    A2=random.randint(1,4)
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
        


