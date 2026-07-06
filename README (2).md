# Bank Management System

A mini console-based **Bank Management System** developed in **Python**
using **Object-Oriented Programming (OOP)** and dictionary-based
customer record management.

## Overview

The application models basic banking operations through `Customer` and
`Bank` classes. It allows users to create and delete customer accounts,
deposit and withdraw money, check balances, transfer funds between
accounts, and generate bank receipts.

## Features

-   Add new customers with unique customer IDs
-   Store customer name, address, account type, password, and balance
-   Enforce a minimum opening balance
-   Delete customer records
-   Deposit money with password verification
-   Withdraw money with transaction limits
-   Check account balances
-   Transfer money between customer accounts
-   Generate bank receipts with customer details and date
-   Handle invalid numeric input using exception handling
-   Menu-driven interface for banking operations

## OOP Design

### `Customer` Class

Stores customer information including:

-   Customer ID
-   Customer name
-   Customer address
-   Account type
-   Password
-   Account balance
-   Withdrawal limit

### `Bank` Class

Manages:

-   Customer registration
-   Customer deletion
-   Deposits
-   Withdrawals
-   Balance enquiries
-   Money transfers
-   Receipt generation
-   Menu-driven operations

## Concepts Used

-   Python
-   Object-Oriented Programming
-   Classes and Objects
-   Dictionaries
-   Exception Handling
-   Conditional Logic
-   Loops
-   Date and Time Handling
-   Modular Methods

## Project Structure

``` text
bank-management-system/
├── Bank.py
└── README.md
```

## How to Run

Make sure Python 3 is installed.

``` bash
python Bank.py
```

## Main Menu

``` text
1. Add a new customer
2. Delete customer record
3. Customer needs
4. Exit
```

## Customer Operations

``` text
1. Print bank receipt
2. Add money to the account
3. Withdraw money from the account
4. Print account balance
5. Money transfer
6. Exit
```

## Author

**Goutham Gaman**

B.Tech Computer Science and Engineering student\
Visvesvaraya National Institute of Technology, Nagpur
