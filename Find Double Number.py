__foundby__ = "zabilsabri"

a = [5,4,2,2,1,1]
b = []

for i in sorted(set(a)):
    count = a.count(i)
    if count == 1:
        b.append(i)
        
print(b)
