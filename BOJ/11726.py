n = int(input())
lst = [1, 2]

# n = 1, 넓이 = 2, 1
# n = 2, 넓이 = 4, 2
# n = 3, 넓이 = 6, 3
# n = 4, 넓이 = 8, 5
# n = 5, 넓이 = 10, 8
# n = 6, 넓이 = 12, 13

if n <= 2:
        print(lst[n-1] % 10007)
else:
    for j in range(2, n):
        lst.append(lst[j-1] + lst[j-2])
    print(lst[n-1] % 10007)