import math
n = int(input())
vals = map(int, input().split(" "))
print(math.floor(sum(vals)/n))