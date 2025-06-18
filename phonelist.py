t = int(input())


for i in range(t):
    n = int(input())
    phone = []
    for j in range(n):
        phone.append(input())
    phone.sort()
    for j in range(n- 1):
        if phone[j + 1].startswith(phone[j]):
            print("NO")
            break
    else:
        print("YES")