import random
from fractions import Fraction

print('选择难度（输入简单或者困难）')
level = input()
if level =='简单':
     n = 50
else:
     n = 100
     
def integer():
    fh = ['＋', '－', '×', '÷']
    k = random.randint(0, 3)
    n1 = random.randint(1, n)
    n2 = random.randint(1, n)
    result = 0
    if k == 0:
        result = n1 + n2
    elif k == 1:
        n1, n2 = max(n1, n2), min(n1, n2)
        result = n1 - n2
    elif k == 2:
        result = n1 * n2
    elif k == 3:
        n1, n2 = max(n1, n2), min(n1, n2)
        while n1 % n2 != 0:
            n1 = random.randint(1,20)
            n2 = random.randint(1,20)
            n1, n2 = max(n1, n2), min(n1, n2)
        result = int(n1/n2)
    print(n1, fh[k], n2, '=', end='')
    return result

def fraction():
    fh = ['＋', '－', '×', '÷']
    k = random.randint(0, 3)
    t1 = random.randint(1, n)
    t2 = random.randint(t1, n)
    n1 = Fraction(t1, t2)
    t3 = random.randint(1, n)
    t4 = random.randint(t1, n)
    n2 = Fraction(t3, t4)
    result = 0
    if k == 0:
        result = n1 + n2
    elif k == 1:
        n1, n2 = max(n1, n2), min(n1, n2)
        result = n1 - n2
    elif k == 2:
        result = n1 * n2
    elif k == 3:
        n1, n2 = max(n1, n2), min(n1, n2)
        result = n1 / n2
    print(n1, fh[k], n2, '=', end='')
    return result

print('自动生成四则运算')
print('输入exit退出')
while True:
    a = random.randint(0, 4)
    if a == 0:
        result = fraction()
        jg = input()
        if jg == 'exit':
            break;
        sr = Fraction(jg)
        if sr == result:
            print('正确')
        else:
            print('错误，正确结果是:', result)
    else:
        result = integer()
        jg = input()
        if jg == 'exit':
            break;
        sr = int(jg)
        if sr == result:
            print('正确')
        else:
            print('错误，正确结果是:', result)
            
