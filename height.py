def count_steps(heights):
    res = 0
    sorted_heights = [heights[0]]
    for i in range(1, len(heights)):
        for j in range(len(sorted_heights)):
            if heights[i] < sorted_heights[j]:
                res += len(sorted_heights) - j
                sorted_heights.insert(j, heights[i])
                break
        else:
            sorted_heights.append(heights[i])
            
    return res
n = int(input())
for i in range(n):
    data = [*map(int, input().split(" "))]
    print(f"{data[0]} {count_steps(data[1:])}")