import datetime

class Customer:
    def __init__(self, customer_id, customer_name, customer_address, account_type,  password,balance, withdrawal_limit=5000):

        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.account_type = account_type
        self.password = password
        self.balance = balance
        self.withdrawal_limit = withdrawal_limit

class Bank:
    def __init__(self):
        self.customers = {}  # A dictionary to store the details of the customer by their ID values.

    def add_customer(self):
        while True:
            try:
                customer_id = int(input("Enter customer ID: "))
                if customer_id < 0:
                    print("Enter a valid ID. ID cannot be negative.")
                    return
                if customer_id not in self.customers:
                    customer_name = input("Enter customer name : ")
                    customer_address = input("Enter customer address : ")
                    account_type = input("Enter account type (savings/current) : ")
                    password = int(input("Create a four digit password."))
                    balance = int(input("Enter your opening account balance : "))
                    while True:
                        
                        if balance < 1000:
                            print("The minimum opening balance should be more than 1000.")
                            balance = int(input("Enter your opening account balance : "))
                        else:
                            break
                                   
                    customer = Customer(customer_id, customer_name, customer_address, account_type, password,balance)
                    self.customers[customer_id] = customer
                    print(f"***Hello, {customer_name}! welcome to Magadha bank. You have successfully opened a {account_type} account.\n")
                    break
                else:
                    print("The customer's ID already exists, so enter a new ID.")
            except ValueError:
                print("Invalid ID.Enter again.")
    def delete_customer(self):
        try:
            customer_id = int(input("Enter the customer ID."))
            if customer_id in self.customers:
                del self.customers[customer_id]
                print(f"ID no. {customer_id} is no longer a customer of ABC bank.")
            else:
                print(f"customer with ID {customer_id} not found.")
        except ValueError:
            print("Invalid customer ID. Enter a valid customer ID.")

    def add_money(self):
        try:
            customer_id = int(input("Enter the customer ID."))
            if customer_id in self.customers:
                deposit = int(input("Enter the amount for deposition."))
                while True:
                    password = int(input("Enter your password : "))
                    if password == self.customers[customer_id].password:
                        self.customers[customer_id].balance += deposit
                        print(f"The amount {deposit} added to account no. {customer_id} successfully.")
                        print(f"Current balance of account no. {customer_id} is {self.customers[customer_id].balance}")
                        break
                    else:
                        print("Oops!. Wrong password. !try again!.")
            else:
                print(f"customer with ID {customer_id} not found.")
        except ValueError:
            print("Invalid customer ID. Enter a valid customer ID.")
        
    def withdraw_money(self):
        try:
            customer_id = int(input("Enter the customer ID."))
            if customer_id in self.customers:
                withdraw = int(input("Enter the amount for withdrawal."))
                while True:
                    password = int(input("Enter your password : "))
                    if password == self.customers[customer_id].password:
                        if withdraw >= 5000:
                            print("Withdrawal amount should not exceed 5000.")
                            withdraw = int(input("Enter the amount for withdrawal."))
                            self.customers[customer_id].balance -= withdraw
                            print(f"The amount {withdraw} withdrawed from account {customer_id} successfully.")
                            print(f"Current balance of ID {customer_id} is {self.customers[customer_id].balance}")   
                        else:
                            self.customers[customer_id].balance -= withdraw
                            print(f"The amount {withdraw} withdrawed from account {customer_id} successfully.")
                            print(f"Current balance of ID {customer_id} is {self.customers[customer_id].balance}")
                        break
                    else:
                        print("Oops!. Wrong password. !try again!.")
                
            else:
                print(f"Customer with ID {customer_id} not found.")        
        except ValueError:
            print("Invalid customer ID. Enter a valid customer ID.")

    def print_balance(self):
        try:
            customer_id = int(input("Enter the customer ID."))
            if customer_id in self.customers:
                print(f"The customer with ID {customer_id} has a balance : {self.customers[customer_id].balance}")
            else:
                print(f"Customer with ID {customer_id} not found.")
        except ValueError:
            print("Invalid customer ID. Enter a valid customer ID.")

    def customer_needs(self):
        customer_id = int(input("Enter your ID : "))
        if customer_id in self.customers:
            while True:
                print("1.Print bank receipt.")
                print("2.Add money to the account.")
                print("3.Withdraw money from the account.")
                print("4.print the balance of the customer.")
                print("5.Money transfer.")
                print("6.Exit.")
                try:
                    key = int(input("Please select an option (1-6): "))
                    if key == 1:
                        self.bank_receipt()
                    elif key == 2:
                        self.add_money()
                    elif key == 3:
                        self.withdraw_money()
                    elif key == 4:
                        self.print_balance()
                    elif key == 5:
                        self.money_transfer()
                    elif key == 6:
                        print("Exiting from the customer needs.....")
                        break
                    else:
                        print("Invalid choice. Please select a number between 1 and 3.")
                except ValueError:
                    print("Invalid choice. Enter a valid choice(1-3).")


    def bank_receipt(self):
        now = datetime.datetime.now()
        try:
            customer_id = int(input("Enter the customer ID."))
            if customer_id in self.customers:
                while True:
                        password = int(input("Enter your password : "))
                        if password == self.customers[customer_id].password:
                            print(f"Customer ID : {customer_id}\nCustomer name : {self.customers[customer_id].customer_name}")
                            print(f"Customer address : {self.customers[customer_id].customer_address}")
                            print(f"Customer acccount type : {self.customers[customer_id].account_type}\nCustomer account balance : {self.customers[customer_id].balance}")
                            print(now.strftime("%d-%m-%y"))
                            break
                        else:
                            print("Oops!. Wrong password. !try again!.")
            else:
                print(f"Customer with ID {customer_id} not found.")
        except ValueError:
            print("Invalid customer ID. Enter a valid customer ID.")
    def money_transfer(self):
        customer_id = int(input("Enter the customer ID : "))
        try:
            if customer_id in self.customers:
                customer_id2 = int(input("Enter the customer ID whom youwant to transfer money : "))
                if customer_id2 in self.customers:
                    while True:
                        amount = int(input("Enter the amount fro transfer : "))
                        if amount < self.customers[customer_id].balance and amount < 100000:
                            while True:
                                password = int(input("Enter the password."))
                                if password == self.customers[customer_id].password:
                                    self.customers[customer_id2].balance += amount
                                    self.customers[customer_id].balance -= amount
                                    print(f"you have successfully transfered {amount} ruppees to customer {customer_id2}. ")
                                    print(f"Your current balance : {self.customers[customer_id].balance}")
                                    break
                                else:
                                    print("You have entered wrong password. Try again.")
                            break
                        else:
                            print("You doesn't have sufficient balance.")
                else:
                    print(f"Customer with ID {customer_id2} not found.")        
            else:
                print(f"Customer with ID {customer_id} not found.")
        except ValueError:
            print("Invalid customer ID. Enter a valid customer ID.")
    def menu(self):
        while True:
            print("MENU <--------------------------------------->")
            print("1.Add a new customer.")
            print("2.Delete customer record.")
            print("3.Customer needs")
            print("4.Exit the menu drive.")

            try:
                choice = int(input("Please select an option (1-4): "))
                if choice == 1:
                    self.add_customer()
                elif choice == 2:
                    self.delete_customer()
                elif choice == 3:
                    self.customer_needs()
                elif choice == 4:
                    print("Exiting from the menu drive.....")
                    break
                else:
                    print("Invalid choice. Please select a number between 1 and 4.")
            except ValueError:
                print("Invalid choice. Enter a valid choice(1-4).")

bank = Bank()
bank.menu()