import sys

def simulate(n, M, P, L, eggs, survival_larvae, survival_pupae):
    M = M
    P = P
    L = L
    eggs = eggs
    survival_larvae = survival_larvae
    survival_pupae = survival_pupae
    for i in range(n):
        new_val_L = M * eggs
        new_val_P = L // survival_larvae
        new_val_M = P //survival_pupae
        M = new_val_M
        P = new_val_P
        L = new_val_L
        
    return M

for line in sys.stdin:
    M, P, L, E, R, S, N = map(int, line.strip("\n").split(" "))
    print(simulate(N, M, P, L, E, R, S))