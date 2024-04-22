import datetime

class LogManager:
    """
    A class that provides logging functionality for recording activities and printing logs.
    """

    @staticmethod
    def log_activity(action, details):
        """
        Logs the specified activity with the given action and details.

        Parameters:
        - action (str): The action being performed.
        - details (str): Additional details about the activity.

        Returns:
        - str or None: The file path of the log file if the activity is logged successfully, None otherwise.
        """
        try:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"{timestamp} - {action}: {details}\n"
            log_file_path = "log/activity_log.txt"
            with open(log_file_path, "a") as log_file:
                log_file.write(log_entry)
            return log_file_path
        except Exception as e:
            print(f"Error logging activity: {e}")
            return None

    @staticmethod
    def print_log():
        """
        Prints the content of the log file.

        Raises:
        - FileNotFoundError: If the log file is not found.
        - Exception: If there is an error while printing the log.
        """
        try:
            log_file_path = "log/activity_log.txt"
            with open(log_file_path, "r") as log_file:
                log_content = log_file.read()
                print("Log content:")
                print(log_content)
        except FileNotFoundError:
            print("Log file not found.")
        except Exception as e:
            print(f"Error printing log: {e}")
