words = input().split(" ")
count = 0
for i in range(len(words)):
    if "ae" in words[i]:
        count += 1
if count/len(words) >= 0.4:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")