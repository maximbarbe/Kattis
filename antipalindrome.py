
def isPalindrome(start, end, string):
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True

string = input().replace(" ", "").lower()
if len(string) == 1:
    print("Anti_palindrome")
for i in range(len(string) - 1):
    for j in range(i+1, len(string)):
        if string[i] == string[j]:
            if isPalindrome(i, j, string):
                print("Palindrome")
                exit()
else:
    print("Anti-palindrome")