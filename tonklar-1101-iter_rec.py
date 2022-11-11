"""
function iterativePower
    parameter: base -> base number
               exp  -> number of the power
    result = 1
    loop exp time:
        result = result * base
    :return result
function recursivePower
    parameter: base -> base number
               exp  -> number of the power
    if power is 0:
        result = 1
    else:
        result = base * recursivePower
    :return result
"""

def iterativePower(base, exp):
    exp = int(exp)
    if exp >= 0:
        result = 1
        for time in range(int(exp)):
            result *= base

    return round(result, 2)

def recursivePower(base, exp):
    exp = int(exp)
    if exp >= 0:
        if exp == 0:
            result = 1
        else:
            result = base * recursivePower(base, int(exp) - 1)
    return round(result, 2)

# test case
for i in range(0,5):
    n = iterativePower(3.3, i)
    print("n", n)

for i in range(0,5):
    n = recursivePower(3.3, i)
    print("n", n)
