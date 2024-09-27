def angles():
    while True:
        a = float(input("Enter degrees 1-179: "))
        if 0 < a < 180:
            break
        print("repeat please")

    degree_other_angels = (180 - a) / 2
    return degree_other_angels

print(angles())