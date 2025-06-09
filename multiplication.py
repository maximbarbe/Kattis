def form_grid(A, B):
    product = list(str(A * B))
    string = ""    
    digitsA = []
    digitsB = []
    if A == 0:
        digitsA.append(0)
    while A != 0:
        digitsA.append(A%10)
        A //= 10
    if B == 0:
        digitsB.append(0)
    while B != 0:
        digitsB.append(B%10)
        B //= 10
    cur = len(digitsB)
    row_length = 2 +  len(digitsA) + (len(digitsA) + 1)*3
    string +="+"+"-"*(len(digitsA) + (len(digitsA) + 1)*3) + "+"+"\n"
    string +="|" + " " * 3
    for i in range(len(digitsA)-1, -1, -1):
        string+=f"{digitsA[i]}" + 3*" "
    string+="|"+"\n"
    string+="| " + "+---"*len(digitsA) + "+ |"+"\n"
    overflow = False
    for j in range(len(digitsB) - 1, -1, -1):
        mult_digit = []
        for i in range(len(digitsA) -1, -1, -1):
            mult_digit.append(digitsA[i] * digitsB[j])
        string+=f"|{'/' if overflow else ' '}|"
        for k in range(len(mult_digit)):
            string+=f"{mult_digit[k]//10} /|"
        string+=" |"+"\n"
        string+="| " + "| / " *len(digitsA) + f"|{digitsB[j]}|"+"\n"
        if len(product) == len(digitsA) + cur:
            overflow = True
        string+=f"|{product[0] if overflow else ' '}|"
        if overflow:
            product.pop(0)
            
        for k in range(len(mult_digit)):
            string+=f"/ {mult_digit[k]%10}|"
        string+=" |"+"\n"
        string+="| " + "+---"*len(digitsA) + "+ |"+"\n"
        cur -= 1
    
    row_length -= 2
    string+=f"|{'/' if overflow else ' '}"
    for i in range(len(product)):
        if i == len(product) - 1:
           string+=f" {product[i]}"
           row_length -= 2 
        else:
            string+=f" {product[i]} /"
            row_length -= 4
    string+=" " * (row_length - 1) + "|"+"\n"
    string+="+"+"-"*(len(digitsA) + (len(digitsA) + 1)*3) + "+"+"\n"
    print(string, end="")
while True:
    nums = input().split(" ")
    A = int(nums[0])
    B = int(nums[1])
    if A == 0 and B == 0:
        break
    form_grid(A, B)