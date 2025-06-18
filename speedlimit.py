while True:
    n = int(input())
    if n == -1:
        break
    distance = 0
    cur_time = 0
    for i in range(n):
        a, b = map(int, input().split(" "))
        distance += a * (b - cur_time)
        cur_time = b
    print(f"{distance} miles")