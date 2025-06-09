n = int(input())
k = int(input())
if n == k:
    print("impossible")
else:
    for i in range(1, k+1):
        print(f"open {i} using {i+1}")