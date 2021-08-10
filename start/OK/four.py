a = [1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 6, 7]
new = []

for i in a:
    if i not in new:
        new.append(i)
print(new)
