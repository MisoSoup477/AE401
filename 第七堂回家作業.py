import random
w=random.randint(0,6)
wlist=[]
ww=random.randint(0,6)
www=random.randint(0,6)

for i in range(7):
    name=input('輸入姓名:')
    n=input('輸入名詞:')
    v=input('輸入動詞:')
    wlist.append([name,n,v])
print(wlist)
print(wlist[w][0],wlist[ww][2],wlist[www][1])