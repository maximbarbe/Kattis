phone = False
keys = False
wallet = False
n = int(input())
for i in range(n):
    word = input()
    if word == "phone":
        phone = True
    if word == "keys":
        keys = True
    if word == "wallet":
        wallet = True
    
if phone and keys and wallet:
    print("ready")
else:
    if not keys:
        print("keys")
    if not phone:
        print("phone")
    if not wallet:
        print("wallet")