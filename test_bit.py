from unittest import TestCase
from bit import bit_no


class TestBitNo(TestCase):
    def test_zero(self):
        self.assertEqual(bit_no(0), 0)

    def test_other(self):
        self.assertEqual(bit_no(int('10010010011', 2)), 5)



