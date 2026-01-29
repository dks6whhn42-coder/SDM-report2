#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))
        
        def test_sample5(self):
                """同値分割: 小数x + 小さいy → エラー(-1)期待"""
                self.assertEqual(-1, calc(0.5, 5))

        def test_sample6(self):
                """同値分割: 整数x + 小さいy → 乗算期待"""  
                self.assertEqual(10, calc(2, 5))

        def test_sample7(self):
                """境界値: x=0.0 → エラー(-1)期待"""
                self.assertEqual(-1, calc(0.0, 999))

        def test_sample8(self):
                """境界値: x=1.0 → 乗算期待"""
                self.assertEqual(999, calc(1.0, 999))

