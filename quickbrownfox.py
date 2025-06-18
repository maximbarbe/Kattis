alphabet = "abcdefghijklmnopqrstuvwxyz"
n = int(input())
for i in range(n):
    string = input().lower()
    missing = []
    for char in alphabet:
        if char not in string:
            missing.append(char)
    if len(missing) == 0:
        print("pangram")
    else:
        print(f"missing {''.join(missing)}")