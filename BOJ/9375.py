n = int(input())
result = []

for j in range(n):
    count = {}
    sum = 1

    num = int(input())

    for j in range(num):
        value, category = input().split()

        if category not in count:
            count[category] = 0
            
        count[category] += 1
    
    for key in count:
        sum *= (count[key] + 1)
    
    result.append(sum - 1)

print("\n".join(map(str, (result))))