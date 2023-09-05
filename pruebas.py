x = 0
while True:
    x += 1
    if x == 6 or x == 4 or x == 10:
        print(f"se saltea {x}")
    else:
        print(x)
    if x == 15:
        print("se corta")
        break

    if x >= 30:
        break
