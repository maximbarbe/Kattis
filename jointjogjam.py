from math import dist
kx_1, ky_1, ox_1, oy_1, kx_2, ky_2, ox_2, oy_2 = map(int, input().split(" "))

print(max(dist((kx_1, ky_1), (ox_1, oy_1)), dist((kx_2, ky_2), (ox_2, oy_2))))