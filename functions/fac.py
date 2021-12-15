def fac(n):
    if not isinstance(n, int):
        print("Factorial is only defined for integers.")
    elif n < 0:
        print("Factorial is not defined for negative integers.")
    elif n == 0:
        return 1
    else:
        return n * fac(n - 1)


print(fac("s"))
print(fac(-5))
print(fac(5))
