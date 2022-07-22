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
        assert repr(1) == "1"
        assert repr("abc") == "'abc'"
        assert repr([1, 2, 3, 4]) == "[1, 2, 3, 4]"

    def test_enable(self):
        arr = np.arange(4)

        arraydebug.enable()
        assert repr(arr) == "<ndarray: shape=(4,), dtype=int64>\narray([0, 1, 2, 3])"

        arraydebug.disable()
        assert repr(arr) == "array([0, 1, 2, 3])"

    def test_register_repr(self):
        class A:
            def __init__(self, x):
                self.x = x

        info_fn = lambda a: f"<class A object with x={a.x}>"
        arraydebug.register_repr(A, info_fn)
        assert repr(A(5)) == "<class A object with x=5>"
