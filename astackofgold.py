amount, n = map(int, input().split())
tungsten=[29260*i for i in range(1, n+1)]
s = sum(tungsten)
for i in range(1, n+1):
    gold = 29370 * i
    if s - tungsten[i - 1] + gold == amount:
        print(i)
        exit()