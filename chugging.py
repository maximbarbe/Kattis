n = int(input())
ta, da = map(int, input().split(" "))
tb, db = map(int, input().split(" "))
timea = ta*n + da*(n*(n-1))//2
timeb = tb*n + db*(n*(n-1))//2
if timea < timeb:
    print("Alice")
elif timeb < timea:
    print("Bob")
else:
    print("=")