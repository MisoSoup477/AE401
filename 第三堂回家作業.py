import random
eee=0
eee+=1
num2=random.randint(1,20)

while eee<6:
    num=input('1到20猜一個數字:')
    num=int(num)
    if (num>20 or num<0):
        print('不要亂寫!')
        eee+=1
    elif num>num2:
        print('再小一點')
        eee+=1
    elif num<num2:
        print('再大一點')
        eee+=1
    else:
        print('數字是:',num2)
        print('猜了幾次:',eee)
        print('你猜對了!')
        break

