print('삼육구게임 시작')

def start():
    _a= int(input(': '))
    _a1= _a+1
    _a2= str(_a1)
    _a3= str(_a)
    return _a, _a1, _a2, _a3

def yes3(a2):
    q= a2.count('3')
    print('짝'*q)
    w= a2.count('6')
    print('짝'*w)
    e= a2.count('9')
    print('짝'*e)

def no3(a2):
    print(a2)

while(True):
    a, a1, a2, a3 = start()
    
    if '3' in a3 or '6' in a3 or '9' in a3:
        print('술 마시세요')

    if '3' in a2 or '6' in a2 or '9' in a2:
        yes3(a2)
    else:
        no3(a2)
    
