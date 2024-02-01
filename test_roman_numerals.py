import unittest
from roman_numerals import arabic_to_roman, roman_to_arabic

class TestRomanNumerals(unittest.TestCase):

    def test_arabic_to_roman(self):
        # Test cases for arabic_to_roman function
        self.assertEqual(arabic_to_roman(1), 'I')
        # Add more test cases as needed

    def test_roman_to_arabic(self):
        # Test cases for roman_to_arabic function
        self.assertEqual(roman_to_arabic('I'), 1)
        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
