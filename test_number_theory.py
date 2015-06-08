from unittest import TestCase
from number_theory import gcd, lcm, fib


class TestGcd(TestCase):
    def test_zero(self):
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(7, 0), 7)

    def test_other(self):
        self.assertEqual(gcd(1071, 1029), 21)


class TestLcm(TestCase):
    def test_zero(self):
        self.assertEqual(lcm(7, 0), 0)

    def test_one(self):
        self.assertEqual(lcm(7, 1), 7)

    def test_other(self):
        self.assertEqual(lcm(1071, 1029), 52479)


class TestFib(TestCase):
    def test_zero(self):
        self.assertEqual(fib(0), 0)

    def test_one(self):
        self.assertEqual(fib(1), 1)

    def test_nine(self):
        self.assertEqual(fib(9), 34)

    def test_nineteen(self):
        self.assertEqual(fib(19), 4181)
