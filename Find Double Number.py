__foundby__ = "zabilsabri"

a = [5, 4, 4, 3, 3]
b = []
a.sort()

v = len(a)
p = a[v-1]
q = a[0]

for i in range(q, p+1):
    a.remove(i)
    if i not in a:
        b.append(i)

if len(b) == 0:
    print("All Number Is Double!")
else:
    print(b)