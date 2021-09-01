a = int(input("숫자를 입력하세요: "))
a = a + 1
blank = -1
while True:
    a -= 1 
    blank += 1

    if 0 >= a: 
        break   
    print(" " * blank , end='')
    print("*" * a) 