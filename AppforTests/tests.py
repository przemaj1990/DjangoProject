# app/testPosts.py

from django.test import TestCase
import unittest
import datetime
from django.utils import timezone

class TestBasic(unittest.TestCase):
    "Basic tests"

    def test_basic(self):
        a = 1
        self.assertEqual(1, a)

    def test_basic_2(self):
        a = 1
        assert a == 1

