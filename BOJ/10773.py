n = int(input())
stack = []

for i in range(n):
    num = input()
    if num == "0":
        stack.pop()
    else:
        stack.append(int(num))

print(sum(stack))