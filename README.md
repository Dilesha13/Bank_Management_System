# ABC Bank Customer Management System

This project is a console-based application for managing customer details at ABC Bank. It allows the user to add new customers, view customer details, deposit and withdraw money, and update customer information. The project uses Python and the `tabulate` module to display data in a tabular format.

## Features

- **Add Customer**: Add a new customer to the bank.
- **View Customer**: View details of a specific customer.
- **View All Customers**: View details of all customers.
- **Deposit Money**: Deposit money into a customer's account.
- **Withdraw Money**: Withdraw money from a customer's account.
- **Update Customer Details**: Update a customer's personal information.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/abc-bank-customer-management.git
    cd abc-bank-customer-management
    ```

2. Install the required Python packages:
    ```sh
    pip install tabulate
    ```

## Usage

1. Run the application:
    ```sh
    python customer.py
    ```

2. Follow the on-screen menu to navigate through the different features.

## Code Structure

- **Customer Class**: Represents a bank customer with methods for deposit, withdrawal, and updating personal information.
- **BankSystem Class**: Manages the collection of customers and provides methods for adding, viewing, updating customers, and handling deposits and withdrawals.
- **Main Menu**: A user-friendly interface that allows users to choose from different options and perform various actions.

## Example

Below is an example of the main menu displayed when running the application:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                              ABC Bank
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1) Add a new customer
2) View details of a customer
3) View details of all customers
4) Deposit money to a given account
5) Withdraw money from a given account
6) Update Customer Details
7) Exit
