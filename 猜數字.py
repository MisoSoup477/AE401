import random
num=input('1到10猜一個數字:')
num=int(num)
num2=random.randint(1,10)
num2=int(num2)
print('數字是:',num2)
if (num>10 or num<0):
    print('不要亂寫!')
elif num2==num:
    print('你猜對了!')
else:
    print('你猜錯了!')