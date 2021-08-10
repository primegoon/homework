a = [3, 4, ('a', 5, 'g'), (30, 'b', 'w'), (40, 2, 'd')]
lst1 = list(a[2])
lst1[2] = 'Tuple'
a[2] = lst1

lst2 = list(a[3])
lst2[2] = 'Tuple'
a[3] = lst2

lst3 = list(a[4])
lst3[2] = 'Tuple'
a[4] = lst3

print(a)