from sample_module2 import parse
import unittest

class TestParse(unittest.TestCase):
    def test_parse_1(self):
        r = parse('5')
        self.assertEqual(5, r)
    def test_parse_2(self):
        self.assertRaises(ValueError, parse, '')
    def test_parse_3(self):
        self.assertRaises(ValueError, parse, 'helloworld')
    
if __name__ == "__main__":
    unittest.main()