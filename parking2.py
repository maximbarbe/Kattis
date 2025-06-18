n = int(input())
for i in range(n):
    m = int(input())
    positions = list(map(int, input().split(" ")))
    park = (max(positions) - min(positions))/2
    print(int(park * 4))