a, b, c, d, e = map(int, input().split(" "))
grade = int(input())
if a <= grade <= 100:
    print("A")
elif b <= grade < a:
    print("B")
elif c <= grade < b:
    print("C")
elif d <= grade < c:
    print("D")
elif e <= grade < d:
    print("E")
else:
    print("F")