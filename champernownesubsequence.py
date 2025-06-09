n = int(input())
idx = 0
digits = input()
k = 0
while idx != len(digits):
    k += 1
    s = str(k)
    for c in s:
        if idx == n:
            break
        if c == digits[idx]:
            idx += 1
        
    
print(k)