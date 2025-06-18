string = input()
if ":)" in string and ":(" not in string:
    print("alive")
elif ":)" not in string and ":(" in string:
    print("undead")
elif ":)" in string and ":(" in string:
    print("double agent")
else:
    print("machine")