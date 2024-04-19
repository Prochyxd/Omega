import unittest
from unittest.mock import patch
import datetime
import log_manager

class TestLogManager(unittest.TestCase):
    def test_log_activity(self):
        action = "User Login"
        details = "User 'john' logged in successfully"
        expected_log_entry = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {action}: {details}\n"
        expected_log_file_path = "log/activity_log.txt"

        with patch('builtins.open') as mock_open:
            mock_file = mock_open.return_value
            log_file_path = log_manager.log_activity(action, details)

            # Check if the log entry was written to the file
            mock_file.write.assert_called_once_with(expected_log_entry)

            # Check if the correct log file path was returned
            self.assertEqual(log_file_path, expected_log_file_path)

    def test_log_activity_exception(self):
        action = "User Logout"
        details = "User 'john' logged out"
        expected_log_file_path = None

        with patch('builtins.open') as mock_open:
            mock_file = mock_open.return_value
            mock_file.write.side_effect = Exception("File write error")
            log_file_path = log_manager.log_activity(action, details)

            # Check if the exception was caught and printed
            self.assertEqual(mock_file.write.call_count, 1)
            self.assertEqual(log_file_path, expected_log_file_path)
            mock_file.write.assert_called_once()

if __name__ == '__main__':
    unittest.main()