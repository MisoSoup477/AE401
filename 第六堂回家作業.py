scorelist=[]
people=input('輸入全班人數:')  #輸入人數

def gradefunction ():
    for i in range(int(people)):
        name=input('輸入姓名:')
        grade=input('輸入成績:')
        scorelist.append(name) 
        scorelist.append(int(grade))
    return scorelist

def avgfunction (scorelist):
    total=0
    for k in range(1,int(people)*2,2):
        total=total+scorelist[k]
    avg=total/int(people)
    print('平均:',avg)

def scorefunction ():
    highest=0
    lowest=100
    for k in range(1,int(people)*2,2):
        if int(scorelist)>highest:
            highest=int(scorelist)
        if int(3,scorelist)<lowest:
            lowest=int(scorelist)
    print('最高分:',highest)
    print('最低分:',lowest)
    

scorelist = gradefunction()
avgfunction(scorelist)
