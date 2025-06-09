n = int(input())
hours = n//3600
n %= 3600
minutes = n // 60
n %= 60
print(f"{hours} : {minutes} : {n}")