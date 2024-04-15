import datetime

class LogManager:

    @staticmethod
    def log_activity(action, details):

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {action}: {details}\n"
        log_file_path = "log/activity_log.txt"
        with open(log_file_path, "a") as log_file:
            log_file.write(log_entry)
        return log_file_path

    @staticmethod
    def print_log():

        try:
            with open("log/activity_log.txt", "r") as log_file:
                log_content = log_file.read()
                print("Log content:")
                print(log_content)
        except FileNotFoundError:
            print("Log file not found.")
