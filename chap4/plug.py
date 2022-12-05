def plug():
    x = -100
    while x < 100:
        print(x)
        if 2*x + 5 == 13:
            print("x =", x)
            break;
        x += 1

plug()