from fractions import*;o=lambda k:print(k[0],Fraction(k[2]).limit_denominator(int(k[1])))
for i in [1]*int(input()):o(input().split())