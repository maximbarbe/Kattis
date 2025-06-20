import sys
MOD = 10**9 + 7
sys.set_int_max_str_digits(1000000)
target = int(sys.stdin.readline())%MOD

cur = 1
i = 1
while True:
    if cur == target:
        print(i)
        exit()
    i += 1
    cur = (cur * i)%MOD