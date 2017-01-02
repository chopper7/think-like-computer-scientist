def toStr10(n):
    convString = "0123456789"
    if n < 10:
        return convString[n]
    else:
        divisor = n // 10
        remainder = n % divisor
        return toStr10(divisor) + convString[remainder]


def toStr(n, base):
    if base not in range(2, 16):
        print("{} is not a base I can use".format(base))
    else:
        convString = "0123456789ABCDEF"
        if n < base:
            return convString[n]
        else:
            divisor = n // base
            remainder = n % base
            return toStr(divisor, base) + convString[remainder]
