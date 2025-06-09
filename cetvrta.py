from collections import defaultdict
x = defaultdict(lambda: 0)
y = defaultdict(lambda: 0)

for i in range(3):
    x_1, y_1 = map(int, input().split(" "))
    x[x_1] += 1
    y[y_1] += 1
m_x, m_y = 0, 0
for _ in x.keys():
    if x[_] == 1:
        m_x = _
for _ in y.keys():
    if y[_] == 1:
        m_y = _
        
print(f"{m_x} {m_y}")