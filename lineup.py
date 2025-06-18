def is_decreasing(words):
    for i in range(len(words) - 1):
        if words[i + 1] > words[i]:
            return False
    return True

def is_increasing(words):
    for i in range(len(words) - 1):
        if words[i + 1] < words[i]:
            return False
    return True

n = int(input())
words = []
for i in range(n):
    words.append(input())
    
if is_increasing(words):
    print("INCREASING")
elif is_decreasing(words):
    print("DECREASING")
else:
    print("NEITHER")