from functools import reduce
def gcd(n1, n2):
    if n1 == 0:
        return n2
    return gcd(n2%n1, n1)

def lcm(n1, n2):
    return (n1//gcd(n1, n2))*n2

def getTotal(n1, n2):
    l = reduce(lcm, n1)
    g = reduce(gcd, n2)

    s = 0
    for i in range(l, g+1, l):
        if g % i == 0:
            s += 1
    return s

if __name__ == '__main__':
    a = [2, 4]
    b = [16, 32, 96]
    print(getTotal(a, b))
