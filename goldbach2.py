from bisect import bisect_left

def miller_rabin_prime_test(n):
    
    # Pour cet implémentation, comme on testera des nombres qui ne seront pas extrêmement grands, alors on a pas besoin d'utiliser la version probabiliste, on peut utiliser celle déterministe.
    # Sources: Milosz, R. (2024). IFT 2125 - Algorithmes probabilistes [notes de cours]. Département d'informatique et de recherche opérationnelle, Université de Montréal. StudiUM. https://studium.umontreal.ca/ 

    # Les valeurs dans a_values sont celles qui sont nécessaires pour tester un nombre inférieur à 3_474_749_660_383
    # Source: Miller–Rabin primality test. (2024, 12 mars). Dans Wikipédia. https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test. 
    # Certaines valeurs telles que 2 et 5 ont été enlevées puisqu'elles ne sont pas nécessaires.
    a_values = [ 3, 5, 7, 11, 13, 17]
    if n in a_values:
        return True
    s, d, n_copy = 0, 0, n - 1
    while n_copy % 2 == 0:
        s += 1
        n_copy //= 2
    d = n_copy
    for val in a_values:
        x = pow(val, d, n)
        for i in range(s):
            y = pow(x, 2, n)
            if y == 1 and x not in [1, n-1]:
                return False
            x = y
        if y != 1:
            return False
    return True



n = int(input())
for i in range(n):
    m = int(input())
    primes = [2,3]
    sols = []
    for j in range(5, m, 2):
        if miller_rabin_prime_test(j) == True:
            primes.append(j)
    for i in range(len(primes)):
        to_find = m - primes[i]
        idx = bisect_left(primes, to_find)
        if idx < i:
            continue
        if idx == len(primes):
            continue
        else:
            if primes[idx] == to_find:
                sols.append([primes[i], to_find])
    print(f"{m} has {len(sols)} representation(s)")
    for sol in sols:
        print(f"{sol[0]}+{sol[1]}")
    print()