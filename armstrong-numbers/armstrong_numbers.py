def is_armstrong_number(number):
    sum = 0
    power = len(str(number))
    for digit in str(number):
        sum += int(digit) ** power
    if sum == number:
        return True
    return False
