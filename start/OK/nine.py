a = input("숫자를 입력하세요: ")

a = (a.replace("," , " "))
b = a.split()
c = list(map(int,b))
result = sum(c)
print(result)