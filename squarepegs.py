n, m, k = map(int, input().split(" "))
diameters = [*map(lambda el: 2*int(el), input().split())]

circular_houses_diameters = [*map(lambda el: 2*int(el), input().split())]
square_houses_diameters = [*map(lambda el: (int(el)**2 + int(el)**2)**0.5, input().split())]
houses = circular_houses_diameters + square_houses_diameters

diameters.sort(reverse=True)
houses.sort(reverse=True)

res = 0
house_idx = 0
diameters_idx = 0
while diameters_idx != len(diameters) and house_idx != len(houses):
    if houses[house_idx] < diameters[diameters_idx]:
        res += 1
        house_idx += 1
        diameters_idx += 1
    else:
        house_idx += 1
print(res)