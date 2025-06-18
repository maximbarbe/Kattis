wind = float(input())
if 0 <= wind <= 0.2:
    print("Logn")
elif 0.3 <= wind <= 1.5:
    print("Andvari")
elif 1.6 <= wind <= 3.3:
    print("Kul")
elif 3.4 <= wind <= 5.4:
    print("Gola")
elif 5.5 <= wind <= 7.9:
    print("Stinningsgola")
elif 8.0 <= wind <= 10.7:
    print("Kaldi")
elif 10.8 <= wind <= 13.8:
    print("Stinningskaldi")
elif 13.9 <= wind <= 17.1:
    print("Allhvass vindur")
elif 17.2 <= wind <= 20.7:
    print("Hvassvidri")
elif 20.8 <= wind <= 24.4:
    print("Stormur")
elif 24.5 <= wind <= 28.4:
    print("Rok")
elif 28.5 <= wind <= 32.6:
    print("Ofsavedur")
else:
    print("Farvidri")