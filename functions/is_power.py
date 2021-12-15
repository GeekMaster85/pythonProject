def is_power(a, b):
    if a > b:
        if a % b == 0:
            return is_power(a / b, b)
        else:
            return False
    else:
        if a % b == 0:
            return True
        else:
            return False


print(is_power(16, 8))
