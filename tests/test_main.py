import unittest
from unittest.mock import patch
from io import StringIO

class TestRGBProgram(unittest.TestCase):

    @patch('builtins.input', side_effect=['255', '42', '103'])
    def test_valid_input(self, mock_input):
        from main import main
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue()
            self.assertIn("#ff2a67", output)
            self.assertIn("11111111", output)
            self.assertIn("00101010", output)
            self.assertIn("01100111", output)

    @patch('builtins.input', side_effect=['256', '42', '103'])
    def test_out_of_range(self, mock_input):
        from main import main
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue()
            self.assertIn("Couldn't perform the designed task", output)

    @patch('builtins.input', side_effect=['hello', '42', '103'])
    def test_non_numeric(self, mock_input):
        from main import main
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue()
            self.assertIn("Couldn't perform the designed task", output)

    @patch('builtins.input', side_effect=['3.14', '42', '103'])
    def test_float_input(self, mock_input):
        from main import main
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue()
            self.assertIn("Couldn't perform the designed task", output)

if __name__ == '__main__':
    unittest.main()
