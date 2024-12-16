import math

def create_fraction(numerator, denominator):
    return simplify_fraction((numerator, denominator))

def print_fraction(fraction):
    print(fraction[0], "/", fraction[1])

def fraction_minus(fraction1, fraction2):
    result = (fraction1[0]*fraction2[1] - fraction2[0]*fraction1[1], fraction1[1]*fraction2[1])
    return simplify_fraction(result)

def fraction_multiply(fraction1, fraction2):
    result = (fraction1[0]*fraction2[0], fraction1[1]*fraction2[1])
    return simplify_fraction(result)

def fraction_divide(fraction1, fraction2):
    result = (fraction1[0]*fraction2[1], fraction1[1]*fraction2[0])
    return simplify_fraction(result)

def simplify_fraction(fraction):
    gcd = math.gcd(fraction[0], fraction[1])
    return (fraction[0] // gcd, fraction[1] // gcd)


if __name__ == "__main__":
    a = create_fraction(8,10)
    b = create_fraction(1,5)

    print_fraction(a)
    print_fraction(b)
    print_fraction(fraction_minus(a,b))
    print_fraction(fraction_multiply(a,b))
    print_fraction(fraction_divide(b,a))