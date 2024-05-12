class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0

def register_user(accounts):
    username = input("Enter a username: ")
    if username in accounts:
        print("Username already exists.")
        return
    password = input("Enter a password: ")
    accounts[username] = Account(username, password)
    print("User registered successfully.")

def main():
    accounts = {"user1": Account("user1", "password1"), "user2": Account("user2", "password2")}
    current_user = None

    while True:
        print("\nWelcome to the Banking System")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username in accounts and accounts[username].password == password:
                current_user = accounts[username]
                print(f"Logged in as {username}")
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Logout")
                    choice = input("Enter your choice: ")

                    if choice == "1":
                        amount = float(input("Enter amount to deposit: "))
                        current_user.balance += amount
                        print("Amount deposited successfully.")

                    elif choice == "2":
                        amount = float(input("Enter amount to withdraw: "))
                        if amount <= current_user.balance:
                            current_user.balance -= amount
                            print("Amount withdrawn successfully.")
                        else:
                            print("Insufficient balance.")

                    elif choice == "3":
                        print(f"Your balance: {current_user.balance}")

                    elif choice == "4":
                        print("Logged out.")
                        current_user = None
                        break

                    else:
                        print("Invalid choice.")

            else:
                print("Invalid username or password.")

        elif choice == "2":
            register_user(accounts)

        elif choice == "3":
            print("Thank you for using our Banking System.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
