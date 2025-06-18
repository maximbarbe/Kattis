def find_total_number(idx, string_idx, string, word):
    if idx == len(word):
        return 1
    if string_idx == len(string):
        return 0
    if word[idx] != string[string_idx]:
        return find_total_number(idx, string_idx + 1, string, word) % 10000
    else:
        return (find_total_number(idx + 1, string_idx + 1, string, word) + find_total_number(idx, string_idx + 1, string, word)) % 10000
    
    

n = int(input())
for i in range(n):
    string = input()
    res = find_total_number(0, 0, string, "welcome to code jam")
    print(f"Case #{i+1}: {'0' * (4 - len(str(res))) + str(res)}")