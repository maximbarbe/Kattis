n = int(input())
for i in range(n):
    deg1 = int(input())
    nums1 = [*map(int, input().split(" "))]
    
    deg2 = int(input())
    nums2 = [*map(int, input().split(" "))]
    
    res = [0 for i in range(deg1 + deg2 + 1)]
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            res[(i) + (j)] += nums1[i] * nums2[j]
    print(deg1 + deg2)
    print(" ".join(map(str, res)))