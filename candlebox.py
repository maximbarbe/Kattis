d = int(input())
boxr = int(input())
boxt = int(input())
age = 4
cur = 0
while True:
    rita_candles = (age*(age + 1))//2 - 6
    theo_candles = ((age - d)*(age -d  + 1))//2 - 3
    if rita_candles + theo_candles == boxr + boxt:
        print(boxr - rita_candles)
        exit()
    age += 1