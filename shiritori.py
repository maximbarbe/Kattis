n = int(input())
prev_letter = ""
said_words = set()
for i in range(n):
    string = input()
    if string.startswith(prev_letter) == False or string in said_words:
        print(f"Player {1 if i % 2 == 0 else 2} lost")
        exit()
    else:
        prev_letter = string[-1]
    said_words.add(string)
else:
    print("Fair Game")