nums = [int(input()) for i in range(9)]
for i in range(len(nums) - 6):
    for j in range(i + 1, len(nums) - 5):
        for k in range(j + 1, len(nums) - 4):
            for l in range(k + 1, len(nums) -3):
                for m in range(l + 1, len(nums) - 2):
                    for n in range(m + 1, len(nums) - 1):
                        for o in range(n +1, len(nums)):
                            if nums[i] + nums[j] + nums[k] + nums[l] + nums[m] + nums[n] + nums[o] == 100:
                                print(nums[i])
                                print(nums[j])
                                print(nums[k])
                                print(nums[l])
                                print(nums[m])
                                print(nums[n])
                                print(nums[o])
                                exit()