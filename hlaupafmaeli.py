# Count how many leap years are between 2020 and the year given
# Try combinatorics
# Count the number of years divisible by 4, substract the number of years divisible by 100 and readd those divisible by 400 (inclusion-exclusion principle)



year = int(input())

# First check if year is leap:
is_leap = False
if year % 4 == 0:
    if year % 100 != 0:
        is_leap = True
    else:
        if year % 400 == 0:
            is_leap = True
if is_leap:
    number_of_leap_years_to_year = year // 4 - year // 100 + year//400
    print(number_of_leap_years_to_year - 490)
else:
    print("Neibb")