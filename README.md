**ATM Management System (Python + MySQL)**
            **-By Vikramaditya and Anish**

**📌 Project Overview**
This is a Python-based ATM simulation system that interacts with a MySQL database to perform various banking operations such as withdrawals, deposits, account updates, and transaction history viewing.
It mimics the working of a real ATM with support for different account types (savings, current, credit) and includes rules like minimum balance requirement and withdrawal limits.

**🛠 Features**
1.Account Login System (Account Number + PIN Authentication)
2.Check Balance
3.Withdraw Money
4.Savings accounts maintain a minimum balance of ₹5000.
5.Single withdrawal limit of ₹10,000 for savings accounts.
6.Credit accounts respect credit limits.
7.Current accounts allow withdrawals up to available balance.
8.Deposit Money
9.Update PIN
10.Update Mobile Number
11.Mini Statement (last 10 transactions)
12.MySQL Database Integration for persistent data storage.

**🚀 How to Run**
1.Clone the repository and open the project folder.
2.Create a MySQL database named atm and add the atm_user and atm_transaction tables using the schema given above.
3.Install the mysql-connector-python package.
4.Run the Python file atm_management.py to start the program.
