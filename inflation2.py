from collections import defaultdict

n = int(input())
vals = [*map(int, input().split())]


prices = defaultdict(lambda:0)


cur_sum = 0
for i in range(n):
    prices[vals[i]] += 1
    cur_sum += vals[i]

inflation = 0

q = int(input())
for i in range(q):
    data = input().split()
    match data[0]:
        case "INFLATION":
            inflation += int(data[1])
            print(cur_sum + n*inflation)
        case _:
            x = int(data[1]) - inflation
            y = int(data[2]) - inflation
            if x == y:
                print(cur_sum + n*inflation)
                continue
            cur_sum -= prices[x] * (x + inflation)
            cur_sum -= prices[y] * (y + inflation)
            prices[y] += prices[x]
            
            cur_sum += prices[y] * (y + inflation)
            prices[x] = 0
            print(cur_sum + n*inflation)