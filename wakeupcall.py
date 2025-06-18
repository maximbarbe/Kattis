n,m = map(int, input().split())
s1 =  map(int, input().split())
s2 =  map(int, input().split())
sum1 = sum(s1)
sum2 = sum(s2)
if sum1 > sum2:
    print("Button 1")
elif sum1 < sum2:
    print("Button 2")
else:
    print("Oh no")