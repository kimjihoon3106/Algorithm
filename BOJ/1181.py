n = int(input())

words = []

# [5,4,3,2,1]
# i = 0 - [4,5,3,2,1], [4,3,5,2,1], [4,3,2,5,1], [4,3,2,1,5]
# i = 1 - [3,4,2,1,5], [3,2,4,1,5], [3,2,1,4,5]
# i = 2 - [2,3,1,4,5], [2,1,3,4,5]
# i = 3 - [1,2,3,4,5]
# i = 4 - [1,2,3,4,5]

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(lst[j]) > len(lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            elif len(lst[j]) == len(lst[j + 1]):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def main():
    words = []
    for i in range(n):
        raw = input().strip()
        if raw not in words:
            words.append(raw)

    result = bubble_sort(words)

    for i in range(len(result)):
        print(result[i])


if __name__ == "__main__":
    main()