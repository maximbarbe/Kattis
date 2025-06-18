#Source: https://en.wikipedia.org/wiki/Clock_angle_problem
angle = int(input())
angle /= 10
rev = False
if angle > 180:
    angle = 360 - angle
    rev = True
diff =0
minutes = 0

while diff != angle:
    minutes += 1
    diff = (diff + 5.5) % 360
if rev:
    minutes = 720 - minutes

    
hours = minutes // 60
minutes %= 60  
print(f"{'0' if hours < 10 else ''}{hours}:{'0' if minutes < 10 else ''}{minutes}")