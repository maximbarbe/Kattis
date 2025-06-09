# Brute force since the message is short 2**15 is only 32_768
def dfs(pA, pB, cur, n, float_value, start, end):
    if n == 0:
        if start == float_value:
            print(cur)
            exit()
        else:
            return False
    else:
         return dfs(pA, pB, cur + "A", n-1, float_value, start, start + pA*(end-start)) or dfs(pA, pB, cur + "B", n-1, float_value, start + pA*(end-start), end)
    
    
    
    
    
    
n = int(input())
D = int(input())
pA = D/8
pB = 1 - pA

bin_string = input()[2:]
float_value = 0
for i in range(len(bin_string)):
    float_value += int(bin_string[i])*(1/2**(i+1))


dfs(pA, pB, "", n, float_value, 0, 1)