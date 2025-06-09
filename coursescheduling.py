from collections import defaultdict
courses = defaultdict(lambda: set())

n = int(input())
for i in range(n):
    data = input().split(" ")
    courses[data[-1]].add(" ".join([data[0], data[1]]))
for key in sorted(courses.keys()):
    print(f"{key} {len(courses[key])}")