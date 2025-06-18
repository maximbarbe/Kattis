n = int(input())
expected_times = []
actual_times = []
for i in range(n):
    expected, actual = map(int, input().split(" "))
    expected_times.append(expected)
    actual_times.append(actual/60)
if sum(actual_times) <= sum(expected_times):
    print("measurement error")
else:
    print(sum(actual_times)/sum(expected_times))