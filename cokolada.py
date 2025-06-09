from math import ceil ,log2

n = int(input())

size = 2**(ceil(log2(n)))
cur_bar_size = size
num_breaks = 0
while n != 0:
    if cur_bar_size > n:
        num_breaks += 1
        cur_bar_size //= 2
    else:
        n -= cur_bar_size
print(f"{size} {num_breaks}")