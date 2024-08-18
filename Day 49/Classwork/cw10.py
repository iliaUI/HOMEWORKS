store = (10, 11, 12, 13, 14, 17, 18, 19, 20, 21)

inp = input("when you  want to visit store?:")
inp = int(inp)

if inp in store:
    print("Store is open")

else:
    print("Store is closed")
