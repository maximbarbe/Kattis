from bisect import bisect_left

n, n_errors = map(int, input().split(" "))
error_values = [*map(int, input().split(" "))]
correct_lines = []
error_lines = []
for i in range(1, n+1):
    idx = bisect_left(error_values, i)
    if idx == len(error_values) or error_values[idx] != i:
        if correct_lines != [] and i - correct_lines[-1][-1] == 1:
            correct_lines[-1].append(i)
        else:
            correct_lines.append([i])
    else:
        if error_lines != [] and i - error_lines[-1][-1] == 1:
            error_lines[-1].append(i)
        else:
            error_lines.append([i])

print("Errors: ", end="")
if len(error_lines) == 1:
    print(f"{error_lines[0][0]}-{error_lines[0][-1]}" if len(error_lines[0]) > 1 else error_lines[0][0])
else:
    print(", ".join([f"{error_lines[i][0]}-{error_lines[i][-1]}" if len(error_lines[i]) > 1 else str(error_lines[i][0]) for i in range(len(error_lines) - 1)]), end="")
    print(f" and {str(error_lines[-1][0])+'-'+str(error_lines[-1][-1]) if len(error_lines[-1]) > 1 else error_lines[-1][0]}")
    
print("Correct: ", end="")
if len(correct_lines) == 1:
    print(f"{correct_lines[0][0]}-{correct_lines[0][-1]}" if len(correct_lines[0]) > 1 else correct_lines[0][0])
else:
    print(", ".join([f"{correct_lines[i][0]}-{correct_lines[i][-1]}" if len(correct_lines[i]) > 1 else str(correct_lines[i][0]) for i in range(len(correct_lines) - 1)]), end="")
    print(f" and {str(correct_lines[-1][0])+'-'+str(correct_lines[-1][-1]) if len(correct_lines[-1]) > 1 else correct_lines[-1][0]}")