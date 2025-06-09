l, r = map(int, input().split())

r = r - 9*((r-l)//9)

print(sum([i%9 for i in range(l, r+1)])%9)