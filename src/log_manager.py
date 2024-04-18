import datetime

class LogManager:

    @staticmethod
    def log_activity(action, details):
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
