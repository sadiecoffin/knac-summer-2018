def sqrt(number, x=1):
    # x = (1/2) * number
    for i in range(100):
        x = 1/2 * (x + number/x)
    if x == (1/2) * number:
        print("Correct!")
    return x
