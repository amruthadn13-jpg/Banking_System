# Banking System

## Project Overview

The Banking System is a web-based application built using Flask and SQLite that simulates basic banking operations. Users can create bank accounts, deposit money, withdraw funds, and view transaction history.

This project demonstrates real-world backend development concepts such as database integration, transaction handling, business logic implementation, and input validation.

---

## Features

- Create a new bank account
- Set an initial balance
- Deposit money into an account
- Withdraw money from an account
- Prevent withdrawals when funds are insufficient
- View account balances
- View transaction history with timestamps

---

## Technologies Used

- Python
- Flask
- SQLite
- HTML (Jinja Templates)

---

## Project Structure

banking_system/
│
├── app.py
├── bank.db
├── requirements.txt
├── templates/
│   ├── home.html
│   ├── create_account.html
│   ├── deposit.html
│   ├── withdraw.html
│   ├── transactions.html
│
└── README.md

---

## Database Schema

### accounts Table

| Column  | Type    | Description |
|--------|--------|--------|
| id | INTEGER PRIMARY KEY AUTOINCREMENT | Unique account ID |
| name | TEXT | Account holder name |
| balance | REAL | Current account balance |

### transactions Table

| Column | Type | Description |
|------|------|------|
| id | INTEGER PRIMARY KEY AUTOINCREMENT | Unique transaction ID |
| account_id | INTEGER | Linked account ID |
| type | TEXT | Deposit or Withdraw |
| amount | REAL | Transaction amount |
| timestamp | TEXT | Date and time of transaction |

---

## Installation

1. Clone the repository:

   git clone https://github.com/your-username/banking_system.git

2. Navigate to the project directory:

   cd banking_system

3. Install dependencies:

   pip install -r requirements.txt

---

## requirements.txt

flask

---

## Running the Application

Run the Flask application:

python app.py

Open your browser and visit:

http://127.0.0.1:5000/

---

## How to Use

1. Create a new account with an initial balance.
2. View all accounts on the home page.
3. Deposit money into an account.
4. Withdraw money from an account.
5. View transaction history for each account.

---

## Skills Demonstrated

- Python programming
- Flask web development
- SQLite database operations
- SQL queries
- CRUD operations
- Business logic implementation
- Transaction management
- Jinja template rendering

---

## Key Concepts Used

- Flask Routing
- Form Handling
- SQLite Database Integration
- SQL CREATE, INSERT, SELECT, and UPDATE
- Redirects and URL Generation
- Timestamp Recording with datetime

---

## Use Cases

- Personal finance applications
- Banking and fintech prototypes
- Transaction management systems
- Financial record keeping

---

## Future Enhancements

- User authentication and authorization
- Account number generation
- Fund transfer between accounts
- Interest calculation
- PDF statement generation
- Admin dashboard
- REST API support

---

## Interview Questions You Can Answer

1. Why did you choose SQLite for this project?
2. How do you prevent withdrawing more than the available balance?
3. What is the purpose of the transactions table?
4. How are timestamps stored?
5. What SQL operations are used in this project?
6. How would you implement money transfer between two accounts?
7. How would you add authentication?
8. How would you deploy this application?

---

## Resume Description

Developed a Banking System web application using Flask and SQLite that supports account creation, deposits, withdrawals, balance tracking, and transaction history. Implemented database design, business logic, and timestamp-based transaction recording.

---

## Author

Amrutha D N
