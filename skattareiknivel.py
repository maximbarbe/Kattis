from math import floor

res = 0
ex_tax_base = 59665
supp = 0
l = float(input())/100
s = float(input())/100
for i in range(12):
    brut = int(input())
    base = brut - floor(brut * l) - floor(brut*s)
    withholding_tax = 0
    if 0 <= base <= 409986:
        withholding_tax = floor(0.3145 * base)
    elif 409987 <= base <= 1151012:
        withholding_tax = floor(0.3145*409986 + 0.3795*(base - 409986))
    else:
        withholding_tax = floor(0.3145*409986 + 0.3795*741026 + 0.4625*(base-1151012))
    if ex_tax_base + supp <= withholding_tax:
        withholding_tax -= ex_tax_base + supp
        supp = 0
    else:
        supp += ex_tax_base + supp - withholding_tax
        withholding_tax = 0
    base -= withholding_tax
    res += base
print(res)