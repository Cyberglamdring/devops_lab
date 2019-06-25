from unittest import TestCase

import task2


class TestPrime(TestCase):

    def setUp(self):
        """Init"""

    def test_calc_factorial1(self):
        """Checking the expected result"""
        self.assertEqual(task2.calc_factorial(5), 120)          # a == b
        self.assertNotEqual(task2.calc_factorial(5), 300)       # a != b

    def test_calc_factorial2(self):
        """Test calc_factorial function"""
        self.assertAlmostEqual(task2.calc_factorial(5), 120)    # round(a-b, 7) == 0
        self.assertGreaterEqual(task2.calc_factorial(5), 120)   # a >= b

    def tearDown(self):
        """Finsih"""
