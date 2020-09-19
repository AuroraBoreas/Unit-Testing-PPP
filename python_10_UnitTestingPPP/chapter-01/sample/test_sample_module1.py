from sample_module1 import StringLong
import unittest

class TestStringLong(unittest.TestCase):
    def setUp(self):
        self.sl = StringLong()
    def test_string_long_1(self):
        self.assertEqual(0, self.sl._wasLastStringLong)
    def test_string_long_2(self):
        r = self.sl.isStringLong('anything')
        self.assertTrue(r)
        self.assertEqual(True, self.sl._wasLastStringLong)
    def test_string_long_3(self):
        r = self.sl.isStringLong('')
        self.assertFalse(r)
        self.assertEqual(False, self.sl._wasLastStringLong)

if __name__ == "__main__":
    unittest.main()