from collections import defaultdict
n = int(input())
for i in range(n):
    print(f"Recipe # {i+1}")
    recipe = defaultdict()
    R, P, D = map(int, input().split(" ")) 
    scaling_factor = D/P
    bakers_weight = 0
    for j in range(R):
        name, weight, percentage = input().split(" ")
        if percentage == "100.0":
            bakers_weight = float(weight) * scaling_factor
        recipe[name] = (float(weight), float(percentage))
    for key, val in recipe.items():
        print(f"{key} {recipe[key][1]/100 * bakers_weight:.1f}")
    print("-"*40)