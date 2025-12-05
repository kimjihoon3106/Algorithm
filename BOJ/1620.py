import sys
input = sys.stdin.readline

n, m = map(int, input().split())

name_to_num = {}
num_to_name = {}

for i in range(1, n + 1):
    name = input().rstrip()
    name_to_num[name] = i
    num_to_name[i] = name

result = []

for _ in range(m):
    pocket = input().rstrip()

    if pocket.isdigit():
        result.append(num_to_name[int(pocket)])
    else:
        result.append(str(name_to_num[pocket]))

print("\n".join(result))