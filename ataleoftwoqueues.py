n, m = map(int, input().split())
left =  sum([*map(int, input().split())])
right = sum([*map(int, input().split())])

if left < right:
    print("left")
elif right < left:
    print("right")
else:
    print("either")