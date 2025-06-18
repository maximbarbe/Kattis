#https://stackoverflow.com/questions/73693104/valueerror-exceeds-the-limit-4300-for-integer-string-conversion
import sys
sys.set_int_max_str_digits(0)

print(int(input()) + int(input()))