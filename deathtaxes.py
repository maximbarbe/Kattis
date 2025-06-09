buy_prices = []
amounts = []

average = 0
number_of_shares = 0
profit = 0
command = None
while command := input():
    command = command.split(" ")
    if command[0] == "buy":
        n = int(command[1])
        price = int(command[2])
        number_of_shares += n
        buy_prices.append(price)
        amounts.append(n)
        average = 0
        for i in range(len(buy_prices)):
            average += buy_prices[i] * amounts[i]/number_of_shares
    elif command[0] == "sell":
        n = int(command[1])
        number_of_shares -= n
        buy_prices = [average]
        amounts = [number_of_shares]
    elif command[0] == "split":
        n = int(command[1])
        number_of_shares *= n
        average /= n
        buy_prices = [average]
        amounts = [number_of_shares]
    elif command[0] == "merge":
        n = int(command[1])
        if number_of_shares % n != 0:
            number_of_shares -= number_of_shares % n
        number_of_shares/= n
        average *= n
        buy_prices = [average]
        amounts = [number_of_shares]
    else:
        if average > int(command[1]):
            print(number_of_shares * int(command[1]))
        else:
            profit = int(command[1]) - average
            print(number_of_shares * (int(command[1]) - profit * 0.3))
        exit()