from unittest import TestCase
from combinatorics import fact, choices, stirling2, n_parts


class TestFact(TestCase):
    def test_negative_number(self):
        self.assertRaises(ValueError, fact, -5)

    def test_zero(self):
        self.assertEqual(fact(0), 1)

    def test_one(self):
        self.assertEqual(fact(1), 1)

    def test_other(self):
        self.assertEqual(fact(5), 120)
        self.assertEqual(fact(9), 362880)


class TestChoices(TestCase):
    def test_choices(self):
        self.assertEqual(choices(7, 0), 1)
        self.assertEqual(choices(7, 1), 7)
        self.assertEqual(choices(7, 5), 21)


class TestStirling2(TestCase):
    def test_8_5(self):
        self.assertEqual(stirling2(8, 5), 1050)

    def test_more_subsets_than_items(self):
        self.assertEqual(stirling2(3, 4), 0)


class TestNParts(TestCase):
    def test_zero(self):
        self.assertEqual(n_parts(0, 0), 1)

    def test_equal(self):
        self.assertEqual(n_parts(5, 5), 1)

    def test_n_le_k(self):
        self.assertEqual(n_parts(0, 3), 0)
        self.assertEqual(n_parts(3, 7), 0)

    def test_n_ge_k(self):
        self.assertEqual(n_parts(11, 5), 10)
        self.assertEqual(n_parts(11, 11), 1)
