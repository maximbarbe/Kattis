from math import dist

gopherx, gophery, dogx, dogy = map(float, input().split(" "))
while True:
    try:
        xhole, yhole = map(float, input().split(" "))
        if dist((xhole, yhole), (gopherx, gophery))*2 < dist((dogx, dogy), (xhole, yhole)):
            print(f"The gopher can escape through the hole at ({xhole},{yhole}).")
            exit()
    except EOFError:
        break

print("The gopher cannot escape.")