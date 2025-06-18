A, B, C = map(int, input().split(" "))
i,j,k = map(int, input().split(" "))

ratio_a = A/i
ratio_b = B/j
ratio_c = C/k
ratio = min([ratio_a, ratio_b, ratio_c])
print(f"{A - ratio*i} {B- ratio*j} {C - ratio*k}")