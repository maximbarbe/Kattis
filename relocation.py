N, Q = map(int, input().split(" "))
initial_locations = list(map(int, input().split(" ")))
for i in range(Q):
    A, B, C = map(int, input().split(" "))
    if A == 1:
        initial_locations[B - 1] = C
    else:
        print(abs(initial_locations[B - 1] - initial_locations[C-1]))