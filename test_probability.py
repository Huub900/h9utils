from unittest import TestCase
from probability import binom


class TestBinom(TestCase):
    def test_05_3_1(self):
        self.assertEqual(binom(0.5, 3, 1), 0.375)
