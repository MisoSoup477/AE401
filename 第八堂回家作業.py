dic={}
dic2={}

while True:
    print('1=設定','2=列出單字','3=英翻中','4=中翻英','5=測驗','6=離開','7=使用說明')
    settings=input('您要做什麼')
    if settings == '7':
        print('(如果還未輸入單字,請先按1)')
        print('(如果想要知道輸入了幾個單字或單字名稱,請按2)')
        print('(如果需要查詢所輸入單字的中文定義,請按3)')
        print('(如果需要查詢所輸入單字的英文定義,請按4)')
        print('()')
    if settings == '1':
        num=int(input('有幾個單字:'))
        for r in range(num):
            E=input('輸入單字的英文:')
            C=input('輸入單字的中文:')
            dic[E]=C
            dic[C]=E
        print('輸入完畢')
            
    elif settings == '2':
        print('排序:',sorted(dic, key=lambda x:x[1]))
    elif settings == '3':
        question=input('你要查甚麼單字(英文):')
        if question not in dic[C]:
            print('抱歉,您尚未輸入此英文單字')
        else:
            print('此單字的中文是:',dic[E])
    elif settings == '4':
        question=input('你要查甚麼單字(中文):')
        if question not in dic[E]:
            print('抱歉,您尚未輸入此中文單字')
        else:
            print('此單字的中文是:',dic[C])
    elif settings == '5':
        print(dic)
    elif settings == '6':
        print('謝謝惠顧,歡迎再來!')
        break
        
        
        
        