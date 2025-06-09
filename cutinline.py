queue = []
n = int(input())
for i in range(n):
    queue.append(input())
n = int(input())
for i in range(n):
    data = input().split(" ")
    if data[0] == "leave":
        for i in range(len(queue)):
            if queue[i] == data[1]:
                queue.pop(i)
                break
    else:
        first = data[1]
        second = data[2]
        if first not in queue:
            queue.insert(queue.index(second), first)
for person in queue:
    print(person)