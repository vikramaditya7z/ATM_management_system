# 🏦 ATM Management System (Python + MySQL)

### A simple yet powerful command-line ATM simulator built with Python and MySQL.
### Perform secure banking operations like withdrawals, deposits, balance checks, and PIN updates — all while enforcing real-world rules for savings, credit, and current accounts.


---

## 🚀 Features

### 🔐 Secure Login

Account number & PIN verification before any operation.


### 💳 Multiple Account Types

Savings – Enforces minimum ₹5000 balance & ₹10,000 withdrawal limit.

Credit – Checks against available credit limit.

Current – Simple balance-based transactions.


### 💼 Banking Operations

Check account balance

Withdraw money

Deposit money

Update PIN

Update mobile number

View mini statement (last 10 transactions)


### 📝 Transaction Logging

Every deposit & withdrawal recorded with a unique transaction ID.




---

## 🛠 Tech Stack

Language: Python 3.x

Database: MySQL

Libraries:

mysql.connector – Database connectivity

random – Transaction ID generation


---


## 🚀 How to Run  
1. Clone the repository and open the project folder.  
2. Create a MySQL database named **atm** and add the `atm_user` and `atm_transaction` tables using the schema given above.  
3. Install the **mysql-connector-python** package.  
4. Run the Python file **atm_management.py** to start the program.

   
## 📌 Notes

Savings accounts must maintain a minimum ₹5000 balance.

Maximum withdrawal limit for savings accounts: ₹10,000 at a time.

Credit account withdrawals cannot exceed available credit limit.

PIN must be a 3-digit number.

Mobile numbers must be 10 digits.


---
