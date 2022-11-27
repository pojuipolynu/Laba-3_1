import math


class Rational:
    def __init__(self, numerator=1, denominator=1):
        if not isinstance(numerator, int):
            raise Exception('Your numerator is invalid')
        else:
            self.__numerator = numerator
        if not isinstance(denominator, int) or denominator == 0:
            raise Exception('Your denominator is invalid')
        else:
            self.__denominator = denominator

    def __checkfrac(self, frac1):
        if not isinstance(frac1, Rational):
            raise Exception('Your variables aren`t fractions')

    def __str__(self):
        n = math.gcd(self.__denominator, self.__numerator)
        return f'Fraction: {self.__numerator//n}/{self.__denominator//n}' \
               f'\nDecimal: {self.__numerator/self.__denominator}'

    def __add__(self, frac1):
        self.__checkfrac(frac1)
        return Rational(frac1.__numerator*self.__denominator+self.__numerator*frac1.__denominator,
                        frac1.__denominator*self.__denominator)

    def __sub__(self, frac1):
        self.__checkfrac(frac1)
        return self + -frac1

    def __neg__(self):
        return Rational(-self.__numerator, self.__denominator)

    def __mul__(self, frac1):
        self.__checkfrac(frac1)
        return Rational(self.__numerator*frac1.__numerator, self.__denominator*frac1.__denominator)

    def __truediv__(self, frac1):
        self.__checkfrac(frac1)
        return Rational(self.__numerator*frac1.__denominator, self.__denominator*frac1.__numerator)

    def __lt__(self, frac1):
        self.__checkfrac(frac1)
        return self.__numerator * frac1.__denominator < self.__denominator * frac1.__numerator

    def __le__(self, frac1):
        self.__checkfrac(frac1)
        return self.__numerator * frac1.__denominator <= self.__denominator * frac1.__numerator

    def __gt__(self, frac1):
        self.__checkfrac(frac1)
        return self.__numerator * frac1.__denominator > self.__denominator * frac1.__numerator

    def __ge__(self, frac1):
        self.__checkfrac(frac1)
        return self.__numerator * frac1.__denominator >= self.__denominator * frac1.__numerator

    def __eq__(self, frac1):
        self.__checkfrac(frac1)
        return self.__numerator * frac1.__denominator == self.__denominator * frac1.__numerator

    def __ne__(self, frac1):
        self.__checkfrac(frac1)
        return self.__numerator * frac1.__denominator != self.__denominator * frac1.__numerator


fract1 = Rational(21, 39)
fract2 = Rational(2, 5)
fract3 = fract1 + fract2
fract4 = fract1 - fract2
fract5 = fract1*fract2
fract6 = fract1/fract2
fract7 = fract1 > fract2
fract8 = fract1 == fract2
fract9 = fract1 != fract2
print(f'{fract3};\n{fract4};\n{fract5};\n{fract6};\n{fract7}\n{fract8}\n{fract9}.')
