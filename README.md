# Profit & Expense Tracker
#### Video Demo:  https://youtu.be/hxRzIWTu3u8?si=IdLgYjkaZQAvUym2
#### Description:
Profit & Expense Tracker is a secure and user-friendly web application built using Flask, SQL, HTML/CSS and Bootstrap. It allows users to manage their personal finances by recording incomes and expenses. Each user can create an account, log in securely, and view only their own data, ensuring privacy and separation between users. Users can add records with a type (credit or debit), a description, and an amount. The application keeps a running total of all transactions, helping users clearly see their current financial balance. It also offers features like searching records by keywords, deleting specific entries, and clearing all data if needed. To enhance user security, all passwords are stored using hashed encryption, and session management is used to keep users logged in securely. The application is designed to be simple, responsive, and functional on both desktop and mobile browsers using Bootstrap.This project demonstrates a practical use of full-stack development concepts and is created as a final project for CS50x.

Implementation Details:
Profit & Expense Tracker is a full-stack web application developed using Flask, SQL, HTML/CSS and Bootstrap.

Backend (Flask & SQL):
Flask Framework: Handles routing and user authentication.
Database (SQLite): Stores user data securely using hashed passwords. Also manages financial records categorized as credit or debit transactions.
Session Management: Ensures users stay logged in securely while preventing unauthorized data access.

Frontend (HTML/CSS & Bootstrap):
Bootstrap Integration: Provides a clean, responsive UI for both desktop and mobile users.
Forms & Validation: Ensures proper input handling when users register, login, or add financial records.

Security Features:
Hashed Passwords: Uses generate_password_hash() to encrypt passwords before storing them in the database.
Data Privacy: Users can only view and manage their own transactions, preventing cross-user access.
Session Handling: Keeps users logged in securely and prevents unauthorized actions.

Future Enhancements:
Graphical Reports: Generate charts and graphs to visualize spending patterns.
Budget Planning: Allow users to set monthly budgets and track their expenses against goals.
Export & Import Data: Enable users to download their transaction history or upload previous records.
Multi-Currency Support: Add options for users to enter transactions in different currencies.
Recurring Transactions: Automate entries for recurring expenses like rent or subscriptions.

User Guide:
Register using a unique username & password.
Login to access your personal dashboard.
Add transactions by specifying type (credit/debit), description, and amount.
Search records using keywords for faster tracking.
Delete transactions individually or clear all data if needed.
