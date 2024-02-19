# Note: Smays Code from homework solution video for 3b t-distribution

import math
from math import pi, sqrt
from SmaySimpsonIntegration import Simpson


# we will be using Table A9 for comparison

def FZ(args):
    """Function FZ computes the area below the t-distribution"""
    m, u = args
    k_m = km(m)

    def tPDF(args):
        x, m = args
        base = 1 + (x ** 2) / m
        epnt = -(m + 1) / 2
        return base ** epnt

    I = Simpson(tPDF, m, u - 100.0 * abs(u), u, 100000)

    return k_m * I


def gamma(alpha):
    """ Gamma Function computes the function for a positive m"""

    if alpha % 1 == 0:
        g = 1
        for i in range(1, int(alpha)):
            g *= i
        return g

    def fn(args):
        t, a = args
        return math.exp(-t) * math.pow(t, a - 1)

    g = Simpson(fn, alpha, 0, 50, 100000)
    return g


def km(m):
    """ Function to find Km constant as a function of gamma and degrees of freedom"""

    k_m = gamma((0.5 * m) + 0.5) / ((sqrt(m * pi)) * gamma(0.5 * m))
    return k_m


def main():
    """Main function for finding the  probability function"""

    getout = False
    while getout is False:
        m = input("Degrees of freedom (integer): ")
        u = input("Upper integration limit (float):")
        m = int(m)
        u = float(u)
        Fz = FZ((m, u))
        print("F({:0.3f})={:0.3f}".format(u, Fz))
        getout = input("Go Again (Y/N)?") == "N"
    pass


if __name__ == '__main__':
    main()
