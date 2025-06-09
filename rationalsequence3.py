n = int(input())
# Source for algorithm: https://epires2mth311.wordpress.com/wp-content/uploads/2015/09/enumerating_the_rationals_via_the_stern_brocot_tree-1.pdf
for i in range(n):
    k, el = map(int, input().split(" "))
    el = bin(el)[3:]
    num, denom = 1, 1
    for char in el:
        if char == '0':
            denom += num
        else:
            num += denom
    print(f'{k} {num}/{denom}')