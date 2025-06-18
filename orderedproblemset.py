n = int(input())
nums = []
valid = []
for i in range(n):
    nums.append(int(input()))

for i in range(1, n):
    if n % i != 0:
        continue
    else:
        temp = []
        j = 0
        while j != n:
            temp.append(nums[j:j+i])
            j += i
        for j in range(len(temp) - 1):
            if max(temp[j]) >= min(temp[j + 1]):
                break
        else:
            valid.append(n//i)
valid.sort()
if len(valid)  == 0:
    print(-1)
else:
    for val in valid:
        print(val)