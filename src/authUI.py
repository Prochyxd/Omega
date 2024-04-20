from auth import Registration, Login

class AuthenticationUI:
    def __init__(self):
        self.registration = Registration()
        self.login = Login()

    def show_menu(self):
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
