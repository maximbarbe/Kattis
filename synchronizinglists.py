while True:
    n = int(input())
    if n == 0:
        break
    first_list = []
    second_list = []
    for i in range(n):
        first_list.append(int(input()))
    for i in range(n):
        second_list.append(int(input()))
    first = list(sorted(first_list))
    second = list(sorted(second_list))
    for i in range(len(first)):
        second_list[first_list.index(first[i])] = second[i]
    for num in second_list:
        print(num)
    print()