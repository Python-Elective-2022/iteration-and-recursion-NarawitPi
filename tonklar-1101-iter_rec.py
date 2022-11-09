def iterativePower(base, exp):
    result = 1
    for time in range(int(exp)):
        result *= base

    return round(result, 2)

def recursivePower(base, exp):
    result = 1
    if exp > 0:
        if exp == 1:
            result = base
        else:
            result = base * recursivePower(base, int(exp) - 1)
    return round(result, 2)


for i in range(0,5):
    n = iterativePower(3.3, i)
    print("n", n)

for i in range(0,5):
    n = recursivePower(3.3, i)
    print("n", n)
