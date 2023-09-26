import unittest
from sol import solution  # Replace 'your_module' with the actual module name where your function is defined

class TestBrailleTranslator(unittest.TestCase):

    def test_case_1(self):
        input_text = "The quick brown fox jumps over the lazy dog"
        expected_output = "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
        self.assertEqual(solution(input_text), expected_output)

    def test_case_2(self):
        input_text = "code"
        expected_output = "100100101010100110100010"
        self.assertEqual(solution(input_text), expected_output)

    def test_case_3(self):
        input_text = "Braille"
        expected_output = "000001110000111010100000010100111000111000100010"
        self.assertEqual(solution(input_text), expected_output)

if __name__ == '__main__':
    unittest.main()
