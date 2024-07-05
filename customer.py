from tabulate import tabulate

class Customer:
    def __init__(self, account_number, nic, first_name, last_name, birth_date, address, phone, balance=0.0):
        self.account_number = account_number
        self.nic = nic
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.address = address
        self.phone = phone
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("\033[91m\n------Insufficient balance------\033[0m")

    def update_details(self, first_name=None, last_name=None, birth_date=None, address=None, phone=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if birth_date:
            self.birth_date = birth_date
        if address:
            self.address = address
        if phone:
            self.phone = phone

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"NIC: {self.nic}")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Birth Date: {self.birth_date}")
        print(f"Address: {self.address}")
        print(f"Phone: {self.phone}")
        print(f"Balance: {self.balance:.2f}")

    def display_basic(self):
        print(f"NIC: {self.nic}")
        print(f"Phone: {self.phone}")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Bank Balance: {self.balance:.2f}")


class BankSystem:
    def __init__(self):
        self.customers = []

    def add_customer(self):
        if len(self.customers) >= 5:
            print("Maximum number of customers reached")
            return
        print("\n")
        print("~"*66)
        print("\t\t\t    \033[1;3mABC Bank\033[0m")
        print("~"*66)
        while True:
            account_number = input("\nBank Account Number: ")
            if any(customer.account_number==account_number for customer in self.customers):
                print("\033[91m******Account number already added. Please enter a different account number.******\033[0m")
                continue
            if account_number.isdigit() and len(account_number) == 10:
                break
            else:
                print("\033[91m\n------Invalid account number. Please enter a 10-digit number.------\033[0m")
        while True:
            nic = input("NIC: ")
            if len(nic) == 10:
                break
            else:
                print("\033[91m\n------Invalid NIC. Please enter a 10-character NIC.------\n\033[0m")

        while True:
            first_name = input("First Name: ")
            if len(first_name) <= 10:
                break
            else:
                print("\033[91m\n------First Name too long. Please enter a maximum of 10 characters.------\n\033[0m")

        while True:
            last_name = input("Last Name: ")
            if len(last_name) <= 15:
                break
            else:
                print("\033[91m\n------Last Name too long. Please enter a maximum of 15 characters.------\n\033[0m")

        birth_date = input("Birth Date: ")

        while True:
            address = input("Permanent Address: ")
            if len(address) <= 15:
                break
            else:
                print("\033[91m\n------Address too long. Please enter a maximum of 15 characters.------\n\033[0m")

        while True:
            phone = input("Phone Number: ")
            if phone.isdigit() and len(phone) == 10:
                break
            else:
                print("\033[91m\n------Invalid phone number. Please enter a 10-digit number without letters or symbols.------\n\033[0m")

        while True:
            confirmation = input("\nDo you want to save the account (Yes/No)? ")
            if confirmation.lower() in ['yes', 'no']:
                break
            else:
                print("\033[91m\n------Invalid input. Please enter 'Yes' or 'No'.------\033[0m")

        if confirmation.lower() == 'yes':
            customer = Customer(account_number, nic, first_name, last_name, birth_date, address, phone)
            self.customers.append(customer)
            print("\033[92m\n******Customer added successfully.******\033[0m")
        else:
            print("\033[91m\n\n******Customer addition canceled******\033[0m")

    def view_customer(self):

        print("\n")
        print("~" * 66)
        print("\t\t\t    \033[1;3mABC Bank\033[0m")
        print("\t\t   View details of a customers")
        print("~" * 66)

        while True:
            while True:
                account_number = input("\n\033[1mBank Account Number: \033[1m")
                if account_number.isdigit() and len(account_number) == 10:
                    break
                else:
                    print("\033[91m\n------Invalid account number. Please enter a 10-digit number.------\033[0m")
            print("\n")
            customer = next((c for c in self.customers if c.account_number == account_number), None)
            if customer:
                customer.display_basic()
            else:
                print("\033[91m------Customer not found------\033[0m")

            while True:
                confirmation = input("\nDo you want to view another account details (Yes/No)?")
                if confirmation.lower() in ['yes','no']:
                    break
                else:
                    print("\033[91m\n------Invalid input. Please enter 'Yes' or 'No'.------\033[0m")

            if confirmation.lower() == 'no':
                break

    def view_all_customers(self):

        print("\n")
        print("~" * 66)
        print("\t\t\t    \033[1;3mABC Bank\033[0m")
        print("\t\t   View details of all customers")
        print("~" * 66)
        print("\n")
    
        if not self.customers:
            print("\033[91m------No customers to display.------\033[0m")
            return

        headers = ["NIC", "Account Number", "First Name", "Last Name", "Bank Balance"]
        data = [[c.nic, c.account_number, c.first_name, c.last_name, f"{c.balance:.2f}"] for c in self.customers]

        print(tabulate(data, headers=headers, tablefmt="grid"))

        while True:
            confirmation = input("\nDo you want to update the account details (Yes/No)? ")
            if confirmation.lower() in ['yes', 'no']:
                break
            else:
                print("\033[91m\n------Invalid input. Please enter 'Yes' or 'No'.------\033[0m")

        if confirmation.lower() == 'yes':
            self.update_customer_details()

    def deposit_money(self):

        print("\n")
        print("~" * 66)
        print("\t\t\t    \033[1;3mABC Bank\033[0m")
        print("\t\t   Deposit Money to a given account")
        print("~" * 66)
    
        while True:
            account_number = input("\033[1mBank Account Number:\033[1m")
            if account_number.isdigit() and len(account_number) == 10:
                break
            else:
                print("\033[91m\n------Invalid account number. Please enter a 10-digit number.------\033[0m")
        customer = next((c for c in self.customers if c.account_number == account_number), None)
        if customer:
            amount = float(input("Deposit Amount: "))
            customer.deposit(amount)
            print("\033[92m\n***Deposit successful***\033[0m")
            while True:
                confirmation = input("Do you want to save the deposit (Yes/No)? ")
                if confirmation.lower() in ['yes', 'no']:
                    break
                else:
                    print("\033[91m\n------Invalid input. Please enter 'Yes' or 'No'.------\033[0m")

            if confirmation.lower() == 'yes':
                print("\033[92m\n******Deposit saved successfully******\033[0m")
            else:
                customer.withdraw(amount)  # Revert the deposit
                print("\033[91m\n******Deposit canceled******\033[0m")
        else:
            print("\033[91m\n------Account not found. Please add your account first.------\033[0m")

    def withdraw_money(self):
                
        print("\n")
        print("~" * 66)
        print("\t\t\t    \033[1;3mABC Bank\033[0m")
        print("\t\t   Withdraw money from a given account")
        print("~" * 66)

        while True:
            account_number = input("\033[1mBank Account Number:\033[1m")
            if account_number.isdigit() and len(account_number) == 10:
                break
            else:
                print("\033[91m\n------Invalid account number. Please enter a 10-digit number.------\033[0m")
        customer = next((c for c in self.customers if c.account_number == account_number), None)
        if customer:
            amount = float(input("Withdraw Amount: "))
            if customer.balance >= amount:
                customer.withdraw(amount)
                print("\033[92m\n***Withdrawal successful***\033[0m")
                while True:
                    confirmation = input("Do you want to save the withdrawal (Yes/No)? ")
                    if confirmation.lower() in ['yes', 'no']:
                        break
                    else:
                        print("\033[91m\n------Invalid input. Please enter 'Yes' or 'No'.------\033[0m")

                if confirmation.lower() == 'yes':
                    print("\033[92m\n******Withdrawal saved successfully******\033[0m")
                else:
                    customer.deposit(amount)  # Revert the withdrawal
                    print("\033[91m\n******Withdrawal canceled******\033[0m")
            else:
                print("\033[91m\n******Insufficient balance******\033[0m")
        else:
            print("\033[91m\n------Account not found. Please add your account first.------\033[0m")


    def update_customer_details(self):
        
        print("\n")
        print("~" * 66)
        print("\t\t\t    \033[1;3mABC Bank\033[0m")
        print("\t\t   Update Customer Details")
        print("~" * 66)
        while True:
            account_number = input("\n\033[1mBank Account Number:\033[1m")
            if account_number.isdigit() and len(account_number) == 10:
                break
            else:
                print("\033[91m\n------Invalid account number. Please enter a 10-digit number.------\033[0m")
        customer = next((c for c in self.customers if c.account_number == account_number), None)
        if customer:
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            birth_date = input("Birth Date: ")
            address = input("Permanent Address: ")
            phone = input("Phone Number: ")

            original_details = (customer.first_name, customer.last_name, customer.birth_date, customer.address, customer.phone)

            customer.update_details(first_name, last_name, birth_date, address, phone)

            while True:
                confirmation = input("\nDo you want to save the new details (Yes/No)? ")
                if confirmation.lower() in ['yes', 'no']:
                    break
                else:
                    print("\033[91m\n------Invalid input. Please enter 'Yes' or 'No'.------\033[0m")

            if confirmation.lower() == 'yes':
                print("\033[92m\n******Customer details updated successfully******\033[0m")
            else:
                customer.update_details(*original_details)  # Revert to original details
                print("\033[91m\n******Update canceled******\033[0m")
        else:
            print("\033[91m\n------Customer not found------\033[0m")


    def main_menu(self):
        while True:
            print("\n")
            print("~"*66)
            print("\t\t\t    \033[1;3mABC Bank\033[0m")
            print("~"*66)
            print("\n\t1) Add a new customer")
            print("\t2) View details of a customer")
            print("\t3) View details of all customers")
            print("\t4) Deposit money to a given account")
            print("\t5) Withdraw money from a given account")
            print("\t6) Update Customer Details")
            print("\t7) Exit")


            choice = input("\nYour Choice: ")
            try:
                choice=int(choice)
                if choice == 1:
                    self.add_customer()
                elif choice == 2:
                    self.view_customer()
                elif choice == 3:
                    self.view_all_customers()
                elif choice == 4:
                    self.deposit_money()
                elif choice == 5:
                    self.withdraw_money()
                elif choice == 6:
                    self.update_customer_details()
                elif choice == 7:
                    print("*"*64)
                    print("\t\t\t   Good Bye!")
                    print("\t\t\tHave a Nice Day!")
                    print("*"*64)
                    break
                else:
                    print("\033[91m\n------Invalid choice, please enter a number between 1 and 7------\033[0m")
            except ValueError:
                print("\033[91m\n------Invalid input, please enter an integer------\033[0m")


if __name__ == "__main__":
    bank_system = BankSystem()
    bank_system.main_menu()
