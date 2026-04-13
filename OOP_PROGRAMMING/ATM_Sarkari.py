class Exception_ATM(Exception):
    def __init__(self,msg):
        print(msg)





class ATM:
    def __init__(self):
        self.balance = 0
        self.pin = ""
        self.menu()

    def menu(self):
        user_input = input("""
Welcome to the ATM!
Please choose an option:
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Exit
""")

        if user_input == "1":
            self.create_account()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            print("Thank you for using the ATM. Goodbye!")
            exit()
        else:
            raise Exception_ATM("Invalid option! Please try again.")
            self.menu()

    def create_account(self):
        self.pin = input("Set your 4-digit PIN: ")
        print("Account created successfully!")
        self.menu()

    def deposit(self):
        if self.pin == "":
            print("Please create an account first.")
        else:
            amount = float(input("Enter the amount to deposit: "))
            self.balance += amount
            print(f"Deposit successful! Your new balance is: {self.balance}")
        self.menu()

    def withdraw(self):
        if self.pin == "":
            print("Please create an account first.")
        else:
            amount = float(input("Enter the amount to withdraw: "))
            if amount > self.balance:
                raise Exception_ATM("Insufficient funds! Please try again.")
            else:
                self.balance -= amount
                print(f"Withdrawal successful! Your new balance is: {self.balance}")
        self.menu()

    def check_balance(self):
        if self.pin == "":
            print("Please create an account first.")
        else:
            print(f"Your current balance is: {self.balance}")
        self.menu()

try:
    obj = ATM()
except Exception_ATM as e:
    print("An error occurred. Please try again.")
else:
    print("Thank you for using the ATM.")
finally:
    print("Done By Kunal")