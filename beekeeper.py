while True:
    n = int(input())
    if n == 0:
        break
    vowels = ["a", "e", "i", "o", "u", "y"]
    max_vowels = 0
    res = None
    for i in range(n):
        
        string = input()
        if n == 1:
            res = string
            break
        count = 0
        for j in range(len(string) - 1):
            if string[j] in vowels:
                if string[j + 1] == string[j]:
                    count += 1
        if count > max_vowels:
            max_vowels = count
            res = string
    print(res)