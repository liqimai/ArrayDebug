#!/usr/bin/env python

"""Tests for `arraydebug` package."""

import numpy as np
import unittest
import arraydebug


class TestArraydebug(unittest.TestCase):
    def setUp(self) -> None:
        arraydebug.enable()

    def tearDown(self) -> None:
        arraydebug.enable()

    def test(self):
        self.assertEqual(repr(1), "1")
        self.assertEqual(repr("abc"), "'abc'")
        self.assertEqual(repr([1, 2, 3, 4]), "[1, 2, 3, 4]")

    def test_enable(self):
        arr = np.arange(4)

        arraydebug.enable()
        self.assertEqual(repr(arr), "<ndarray: shape=(4,), dtype=int64>\narray([0, 1, 2, 3])")

        arraydebug.disable()
        self.assertEqual(repr(arr), "array([0, 1, 2, 3])")
