from collections import Counter

string = input()

counter_sub = Counter(string)
counter = Counter(string)

for i in range(len(string)):
    counter_sub[string[i]] += 1
    counter[string[i]] -= 1
    factors = set()
    flag = False
    for key, val in counter_sub.items():
        if val == 0:
            flag = True
            break
        else:
            factor = counter[key]/val
            if factor == 0:
                flag = True
                break
            else:
                factors.add(factor)
    if not flag:
        if len(factors) == 1:
            print(string[:i+1])
            exit()
else:
    print(-1)