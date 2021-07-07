__foundby__ = "zabilsabri"

n = [5, 4, 5, 5, 3]
m = list(set(n))
o = []

for i in m:
    if i in n:
        n.remove(i)
    if i not in n:
        o.append(i)
        
if len(o) != 0:
    print(o)
else:
    print("THERE IS NO DOUBLE NUMBER THERE!")
