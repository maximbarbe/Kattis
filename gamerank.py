games = input()
stars = 0
above_20 = False
legend = False
rank = 25
consecutive_wins = 0
ranks = [1000, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2]

    
for game in games:
    if legend:
        break
    else:
        if game == "W":
            stars += 1
            consecutive_wins += 1
            if 6 <= rank <= 25:
                if consecutive_wins >= 3:
                    stars += 1
        else:
            if 1 <= rank <= 20:
                stars -= 1
            consecutive_wins = 0
            
        if stars > ranks[rank]:
            startswith = stars - ranks[rank]
            rank -= 1
            stars = startswith
            if rank <= 20:
                above_20 = True
        if stars < 0:
            if rank == 20:
                stars = 0
            else:
                rank += 1
                stars = ranks[rank] - 1
        if rank == 0:
            legend = True  
        
            
if legend:
    print("Legend")
else:
    print(rank)