#!/usr/bin/env python3

import unittest
from rearrange import rearrange_name

class TestRearrange(unittest.TestCase):
	
	def test_basic(self):
		testcase="Brijesh, Sajeev"
		expected="Sajeev Brijesh"
		self.assertEqual(rearrange_name(testcase),expected) 

unittest.main()
