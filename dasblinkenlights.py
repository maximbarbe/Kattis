n, q, borne = map(int, input().split(" "))
first = set()
second = set()
sum = 0
while sum + n <= borne:
    sum += n
    first.add(sum)
sum = 0
while sum + q<= borne:
    sum += q
    second.add(sum)
if len(first.intersection(second)) != 0:
    print("yes")
else:
    print("no")