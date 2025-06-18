first_time = input()
second_time = input()
first = [*map(int, first_time.split(":"))]
second = [*map(int, second_time.split(":"))]
res = [None for i in range(3)]
if first[0] > second[0]:
    second[0] += 24
sec_elapsed_first = first[0] * 3600 + first[1] * 60 + first[2]
sec_elapsed_second = second[0] * 3600 + second[1] * 60 + second[2]
diff = sec_elapsed_second - sec_elapsed_first

hours = diff // 3600
diff -= hours * 3600

minutes = diff // 60
diff -= minutes * 60

secondes = diff
if hours == minutes==secondes == 0:
    print("24:00:00")
else:
    print(f"{'0' if hours<10 else ''}{hours}:{'0' if minutes<10 else''}{minutes}:{'0' if secondes<10 else ''}{secondes}")