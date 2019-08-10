def sumlist(list):
    return sum(val*(10-n) for n, val in enumerate(list))

def is_valid(isbn):
    digits = []
    for i in isbn:
        if i.isdigit():
            digits.append(int(i))
        elif i is 'X' and len(digits) is 9:
            digits.append(10)
    if len(digits) is 10 and sumlist(digits) % 11 is 0:
        return True
    return False
