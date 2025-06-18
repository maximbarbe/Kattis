from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)
@lru_cache
def find_sol(cur, idx, streets):
    #cur: 0 == north, 1 == south
    
    if idx == len(streets):
        if cur != "N":
            return 1
        else:
            return 0
    else:
        if streets[idx] == "B":
            return min(1 + find_sol(cur, idx+1, streets), 2+ find_sol("S" if cur == "N" else "N", idx + 1, streets))
        elif streets[idx] == "N":
            if cur == "N":
                return min(1+find_sol("N", idx + 1, streets), 1+find_sol("S", idx + 1, streets))
            else:
                return min(2+find_sol("N", idx + 1, streets), find_sol("S", idx + 1, streets))
        else:
            if cur == "N":
                return min(find_sol("N", idx + 1, streets), 2+find_sol("S", idx + 1, streets))
            else:
                return min(1+find_sol("N", idx + 1, streets), 1+find_sol("S", idx + 1, streets))
streets = input()
if len(streets) == 0:
    print(0)
    exit()
print(find_sol("N", 0, streets))