n = int(input())
choice = input()
rice = []
for i in range(n):
    num, size = map(int, input().split(" "))
    rice.append((num, size, i + 1))
if choice == "antal":
    rice.sort(key = lambda el: (-(el[0] + el[1]), -el[0]))
else:
    rice.sort(key = lambda el: (-(el[0] + el[1]), -el[1]))
print(rice[0][2])