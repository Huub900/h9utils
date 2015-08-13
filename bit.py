def bit_no(number):
    result = 0
    while number:
        number &= number - 1
        result += 1
        # result += number & 1
        # number >>= 1
    return result
