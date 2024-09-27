def point(L, W):
    a = [
        (-L/2, -W/2),
        (-L/2, W/2),
        (L/2, W/2),
        (L/2, -W/2)
    ]
    return a
L = int(input("Num 1 "))
W = int(input("Num 2 "))
print(point(L, W))