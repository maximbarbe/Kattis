key, password = input().split(" ")
key = [char for char in key]
for char in password:
    if len(key) == 0:
        print("PASS")
        exit()
    if char in key and char != key[0]:
        print("FAIL")
        exit()
    elif char == key[0]:
        key.pop(0)
    
else:
    if len(key) == 0:
        print("PASS")
    else:
        print("FAIL")