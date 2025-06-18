n = int(input())
running = False
cur = 0
current_time = 0
for i in range(n):
    time = int(input())
    if running == False:
        running = True
        current_time = time
    else:
        running = False
        cur += time - current_time
        current_time = time
if running:
    print("still running")
else:
    print(cur)