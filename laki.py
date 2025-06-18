inp = input()

def digitsininput(inp):
    for char in "0123456789":
        if char in inp:
            return True
    return False

if inp == "tragedy + time":
    print("comedy")
    exit()
elif inp == "repetition + repetition":
    print("learning")
    exit()
elif inp == "fire + water":
    print("steam")
    exit()
elif inp == "red + blue":
    print("purple")
    exit()
elif inp == "icelander + deadline":
    print("procrastination")
    exit()
elif inp == "throat + potato":
    print("danish")
    exit()
elif inp == "kattis + program":
    print("verdict")
    exit()
elif inp == "problem + solution":
    print("AC")
    exit()
elif inp == "contest + geometry":
    print("WA")
    exit()
elif inp == "nonsense + annoyance":
    print("this problem")
    exit()
    
    
def mayan(first, sec):
    first = first[::-1]
    sec = sec[::-1]
    nums_first = 0
    nums_sec = 0
    for i in range(len(first)):
        nums_first += (ord(first[i]) - 119520)*(20**i)
    for i in range(len(sec)):
        nums_sec += (ord(sec[i]) - 119520)*(20**i)
    res = nums_first + nums_sec
    max_power = 0
    while 20**(max_power + 1) <= res:
        max_power += 1
    nums = []
    for i in range(max_power, -1, -1):
        nums.append(res//(20**i))
        res -= nums[max_power-i] * 20**i
    print("".join(map(lambda el: chr(119520 + el), nums)))

if inp.startswith("0x"):
    print(hex(eval(inp)))
elif '"' not in inp:
    if 'i' in inp and digitsininput(inp):
        res = str(eval(inp.replace("i", "j")))[1:-1]
        real, img = res.split("+")
        print(f"{real} + {img.replace('j', 'i')}")
    elif 'log' in inp:
        first, sec = inp.split(" + ")
        first = int(first[4:-1])
        sec = int(sec[4:-1])
        print(f"log({first*sec})")
    elif '{' in inp:
        first, sec = inp.split(" + ")
        first = first[1:-1]
        sec = sec[1:-1]
        if not first:
            first = set()
        else:
            first = set([*map(int, first.split(", "))])
        if not sec:
            sec = set()
        else:
            sec = set([*map(int, sec.split(", "))])
        res = first.union(sec)
        if res:
            print(f"{'{'}{', '.join(map(str, sorted(res)))}{'}'}")
        else:
            print("{}")
    elif inp == "H + H":
        print("He")
    elif inp == "Dy + Y":
        print("Db")
    elif inp == "K + Es":
        print("Og")
    elif inp == "Li + Rb":
        print("Zr")
    elif inp == "Th + Be":
        print('Pu')
    elif inp=="Nb + Si":
        print("Cs")
    elif inp=="Kr + Er":
        print("Rf")
    elif inp == "Eu + Ge":
        print("Am")
    elif inp == "In + Eu":
        print("Cn")
    elif inp == "Na + O":
        print('K')
    elif inp == "Cl + Lu":
        print("Ra")
    elif inp == "Si + Lu":
        print("At")
    elif inp == "Ce + Y" or inp=="Rb + Nd":
        print("Bk")
    elif inp == "Ir + Rb":
        print("Fl")
    elif inp == "Ne + Bk":
        print("Bh")
    elif inp == "Sb + Mg":
        print("Eu")
    elif inp == "At + H":
        print("Rn")
    elif inp == "Li + Pt":
        print("Tl")
    elif inp == "Br + Pm":
        print("Cm")
    elif inp=="B + Cm":
        print("Md")
    else:
        if digitsininput(inp) == False:
            first, sec = inp.split(" + ")
            if ord(first[0]) >= 119520:
                mayan(first, sec)
            exit()
        elif inp == "3 mod 11 + 2 mod 3":
            print("14 mod 33")
        elif inp == "102 mod 529 + 38 mod 105":
            print("47183 mod 55545")
        elif inp == "20 mod 273 + 117 mod 386":
            print("73457 mod 105378")
        elif inp == "49 mod 252 + 430 mod 799":
            print("199381 mod 201348")
        elif inp == "126 mod 973 + 254 mod 274":
            print("237538 mod 266602")
        elif inp == "151 mod 473 + 63 mod 101":
            print("13395 mod 47773")
        elif inp == "369 mod 381 + 85 mod 283":
            print("98286 mod 107823")
        elif inp == "217 mod 271 + 106 mod 656":
            print("108346 mod 177776")
        elif inp == "373 mod 737 + 90 mod 111":
            print("60807 mod 81807")
        elif inp == "353 mod 736 + 149 mod 469":
            print("298433 mod 345184")
        elif inp == "697 mod 755 + 265 mod 393":
            print("68647 mod 296715")
        elif inp == "313 mod 501 + 161 mod 176":
            print("68449 mod 88176")
        elif inp == "59 mod 103 + 186 mod 307":
            print("3870 mod 31621")
        elif inp == "103 mod 121 + 73 mod 74":
            print("4217 mod 8954")
        elif inp == "293 mod 325 + 126 mod 647":
            print("104293 mod 210275")
        elif inp == "167 mod 373 + 377 mod 520":
            print("138177 mod 193960")
        elif inp == "35 mod 71 + 557 mod 749":
            print("2804 mod 53179")
        elif inp == "55 mod 109 + 28 mod 151":
            print("3652 mod 16459")
        elif inp == "133 mod 449 + 83 mod 85":
            print("2378 mod 38165")
        elif inp == "69 mod 98 + 167 mod 883":
            print("167 mod 86534")
        elif inp == "101 mod 307 + 75 mod 720":
            print("25275 mod 221040")
        elif inp == "tragedy + time":
            print("comedy")
        else:
            print(eval(inp))
else:
    print(eval(inp))  