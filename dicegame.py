gunnar_dice = list(map(int, input().split(" ")))
emma_dice = list(map(int, input().split(" ")))
e_val_e = 0
e_val_g = 0
for i in range(len(emma_dice)):
    e_val_e += emma_dice[i]/len(emma_dice)
    e_val_g += gunnar_dice[i]/len(gunnar_dice)
if e_val_e > e_val_g:
    print("Emma")
elif e_val_e == e_val_g:
    print("Tie")
else:
    print("Gunnar")