wlist=[]
people=input('人數:')
high=0
low=100
for i in range(0,int(people)*2,2):
    num=input('名字:')
    score=input('輸入成績:')
    if int(score)>high:
        high=int(score)
    if int(score)<low:
        low=int(score)
    wlist.append(num)
    wlist.append(int(score))
print(wlist)
total=0
for t in range(1,int(people)*2,2):
    total=total+wlist[t]    
print('加總:',total,'分')
print('總平均:',total/int(people),'分')
print('最低分:',low,'分')
print('最高分:',high,'分')

    

