n = int(input())
for i in range(n):
    num = [int(char) for char in input()]
    for i in range(len(num) - 1, -1, -1):
        if num[i] > 0:
            num[i] -= 1
            break
    print(int("".join(map(str, num))))