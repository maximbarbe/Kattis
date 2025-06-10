encrypted = input()
key = input()
decoded =""
for i in range(len(encrypted)):
    if i % 2 == 1:
        decoded += chr((ord(encrypted[i]) + (ord(key[i]) - ord("A")) - ord("A") + 26)%26 +  ord("A"))
    else:
        shift = ord(key[i]) - ord("A")
        shifted = ((ord(encrypted[i]) - ord("A") - shift) + 26) % 26
        decoded += chr(shifted + ord("A"))
print(decoded)