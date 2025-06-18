from math import sqrt, floor

R, B = map(int, input().split())

for height in range(1, floor(sqrt(B)) + 1):
    width  = B // height
    if height * width == B:
        if (height + 2) * (width + 2) - B == R:
            print(max(height, width) + 2, min(height, width) + 2)
            exit()