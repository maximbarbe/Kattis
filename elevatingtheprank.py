a, b = map(int, input().split())
if a > b:
    a, b = b,a 
buttons_pressed = []
n = int(input())
for i in range(n):
    buttons_pressed.append(int(input()))
buttons_pressed.sort()
res = (b - a)*4
for i in range(len(buttons_pressed)):
    if buttons_pressed[i] > a and buttons_pressed[i] < b:
        res += 10
print(res)