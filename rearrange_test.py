#!/usr/bin/env python3

import unittest
from rearrange import rearrange_name

class TestRearrange(unittest.TestCase):
	
	def test_basic(self):
		testcase="Brijesh, Sajeev"
		expected="Sajeev Brijesh"
		self.assertEqual(rearrange_name(testcase),expected) 
	def test_empty(self):
		testcase=""
		expected=""
		self.assertEqual(rearrange_name(testcase),expected)
	def test_single_name(self):
		t="brijesh"
		e="brijesh"
		self.assertEqual(rearrange_name(t),e)

unittest.main()
