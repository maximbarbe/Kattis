def get_shortest_sum(list_idx, current_sum, target, numbers, fib):
    if current_sum > target:
        return
    if current_sum == target:
        numbers.sort()
        print(*numbers)
        exit()
    get_shortest_sum(list_idx, current_sum + fib[list_idx], target, numbers + [fib[list_idx]], fib)
    get_shortest_sum(list_idx - 1, current_sum, target, numbers, fib)
    get_shortest_sum(list_idx - 1, current_sum + fib[list_idx], target, numbers + [fib[list_idx]], fib)


fib = [1, 1]
n = int(input())
while fib[-1] < n:
    fib.append(fib[-1] + fib[-2])
        
get_shortest_sum(len(fib) - 1, 0, n, [], fib)