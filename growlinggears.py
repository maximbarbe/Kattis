from sys import maxsize


t = int(input())
for i in range(t):
    n = int(input())
    max_torque = -1 * maxsize
    max_idx = 0
    for i in range(1, n + 1):
        a, b, c = map(int, input().split(" "))
        R = b/(2*a)
        T = -a * R**2 + b*R + c
        if T > max_torque:
            max_torque = T
            max_idx = i
    print(max_idx)