n = int(input())
lst = list(input())
sum = 0
current = 1

lst = lst[:n]

for i in lst:
    sum += (ord(i.upper()) - 64) * current
    current *= 31

print(sum)