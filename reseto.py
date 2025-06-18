n, k = map(int, input().split(" "))
nums = [False for i in range(n+1)]
crossed_out = 0
for i in range(2, n+1):
    if nums[i] == False:
        mult = 1
        while i * mult <= n:
            if nums[i * mult] == False:
                crossed_out +=1
                nums[i * mult] = True
                if crossed_out == k:
                    print(i*mult)
                    exit()
            mult += 1