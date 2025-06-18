s1 = input()
s2 = input()

    
if len(s1) == len(s2):
    equal_characters = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            equal_characters += 1
        else:
            break
    print((len(s1) - equal_characters)*2)
elif len(s1) < len(s2):
    equal_characters = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            equal_characters += 1
        else:
            break
    print(len(s2) - len(s1) + (len(s1) - equal_characters)*2)
else:
    equal_characters = 0
    for i in range(len(s2)):
        if s1[i] == s2[i]:
            equal_characters += 1
        else:
            break

    print(len(s1) - len(s2) + (len(s2) - equal_characters)*2)