def steps(number, steps = 0):
    if number < 1:
        raise ValueError("it is not a positive number!")
    while number != 1:
        steps += 1
        number = number/2 if number%2 == 0 else number*3 + 1

    return steps
