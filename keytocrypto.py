message = input()
key = input()
if len(key) >= len(message):
    key = key[:len(message)]
keys = [None for i in range(len(message))]
decoded = [None for i in range(len(message))]
for i in range(len(key)):
    keys[i] = (ord(message[i]) - ord(key[i])  + 26) % 26
    decoded[i] = chr(ord("A") + keys[i])
for i in range(len(key), len(message)):
    keys[i] = ord(decoded[i - len(key)]) - ord("A")
    temp = (ord(message[i]) - ord("A") - keys[i]  + 26) % 26
    decoded[i] = chr(ord("A") + temp)
print("".join(decoded))