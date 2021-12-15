def gcd(a, b):
    if b != 0:
        r = a % b
        return gcd(b, r)
    else:
        return a


print(gcd(624, 768))
print(gcd(9, 16))
