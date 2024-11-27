import unittest
from unittest.mock import patch
import sys
from windowslogparser import parse_args


class TestLogParser(unittest.TestCase):

    # Testing valid arguments.
    # Expected Outcome: Positive Result Scenario. The test should pass.
    def test_parse_args_valid(self):

        test_args = [
            "windowslogparser.py", 
            "--log", "Application", 
            "--event_types", "error", 
            "--read_mode", "forwards"
        ]
        
        # Simulate command line input
        with patch.object(sys, 'argv', test_args):
            args = parse_args()
        
        # Assertions
        self.assertEqual(args.log, "Application")
        self.assertIn("error", args.event_types)
        self.assertEqual(args.read_mode, "forwards")

    # Testing missing '--log' argument. If --log is missing, argparse should raise a SystemExit exception.
    # Expected Outcome: The test should pass if SystemExit is raised and sys.exit() was called.
    # Additional Info: The test will not actually terminate the process, as sys.exit() is mocked during the test.
    def test_parse_args_missing_log(self):
        test_args = [
            "windowslogparser.py", 
            "--event_types", "error", 
            "--read_mode", "forwards"
        ]
        
        # Mock sys.exit to prevent actual exit, capture SystemExit exception
        with patch("sys.exit") as mock_exit, patch.object(sys, 'argv', test_args):
            # Here, we expect the SystemExit to occur when the argument is missing
            try:
                parse_args()
            except SystemExit as e:
                # Check if sys.exit() was called as expected
                mock_exit.assert_called()
                # Optionally, check that the exit code matches the expected code
                self.assertEqual(e.code, 2)  # `argparse` usually exits with code 2 on error
        

if __name__ == "__main__":
    unittest.main()
