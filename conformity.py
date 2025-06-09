from collections import defaultdict

courses = defaultdict(lambda: 0)
n = int(input())
for i in range(n):
    course = "".join(list(map(str, sorted(map(int, input().split(" "))))))
    courses[course] += 1
res = 0
max_value = max(courses.values())
for key, value in courses.items():
    if courses[key] == max_value:
        res += courses[key]
print(res)