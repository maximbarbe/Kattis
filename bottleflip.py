from math import sqrt
h, r, da, dw = map(int, input().split(" "))
# Source for the formula: https://math.stackexchange.com/questions/1028946/finding-the-center-of-mass-of-a-cylinder
# Author of the comment: https://math.stackexchange.com/users/95860/narasimham
print(h - (h - h*(sqrt(da/dw)/(1+sqrt(da/dw)))))