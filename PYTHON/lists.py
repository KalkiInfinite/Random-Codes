l = []
n = int(input("Enter your no.s: "))
for i in range(n):
    l.append(int(input("Enter no.s to add: ")))
print("The list is", l)

p = []
for i in range(n):
    if l[i] not in p:
        p.append(l[i])
print("New list without duplicates", p)
