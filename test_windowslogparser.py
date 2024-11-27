import unittest
from unittest.mock import patch
import sys
from windowslogparser import parse_args


class TestLogParser(unittest.TestCase):

    # Testing valid arguments -- this should always pass!
    def test_parse_args_valid(self):

        test_args = [
            "windowslogparser.py", 
            "--log", "Application", 
            "--event_types", "error", 
            "--read_mode", "forwards"
        ]
        
        # Patch sys.argv to simulate command line input
        with patch.object(sys, 'argv', test_args):
            args = parse_args()
        
        # Assertions
        self.assertEqual(args.log, "Application")
        self.assertIn("error", args.event_types)
        self.assertEqual(args.read_mode, "forwards")
        

if __name__ == "__main__":
    unittest.main()
