from sample_module0 import isStringLong
import unittest

class TestSampleModule(unittest.TestCase):
    def test_string_long_1(self):
        r = isStringLong('anything')
        self.assertTrue(r)
    def test_string_long_2(self):
        r = isStringLong('')
        self.assertFalse(r)
    def test_string_long_3(self):
        self.assertRaises(TypeError, isStringLong, 1)
    def test_string_long_4(self):
        self.assertRaises(TypeError, isStringLong, None)

if __name__ == "__main__":
    unittest.main()