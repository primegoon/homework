a , b = input('두 숫자를 입력하세요: ').split()
a = int(a)
b = int(b)
if(a > b):
    print(a,'>',b)
elif(a < b):
    print(a,'<',b)
else:
    print(a,'=',b) 