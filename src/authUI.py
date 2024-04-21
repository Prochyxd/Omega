from auth import Registration, Login

class AuthenticationUI:
    """
    A class representing the user interface for authentication.

    Attributes:
        registration (Registration): An instance of the Registration class.
        login (Login): An instance of the Login class.
    """

    def __init__(self):
        self.registration = Registration()
        self.login = Login()

    def show_menu(self):
        """
        Displays the authentication menu and handles user input.

        The menu options are:
        1. Login
        2. Register
        3. Exit

        Returns:
            None
        """
        while True:
            print("\nWelcome to the Authentication System")
            print("1. Login")
            print("2. Register")
            print("3. Exit")
            choice = input("Please enter your choice: ")

            if choice == "1":
                self.login.login()
                break
            elif choice == "2":
                self.registration.register()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please choose again.")

def run_auth_ui():
    auth_ui = AuthenticationUI()
    auth_ui.show_menu()
