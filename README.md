 
 # The SupermarketDAO Project

This project is developed the Supermarket Self-Service-Checkout *system* with **Python** to streamline inventory management, enhance customer experience, automate transactions, and improve overall operational efficiency within the supermarket.


![python](https://github.com/user-attachments/assets/731900ce-f1b1-439c-99fc-1dce37794963)

# Overview

<h2>Purpose</h2>

The system use an **Object Oriented (OO)** approach that will require the use of several Classes to implement the final system.
The project is for develop the details of all Product and Transaction entities related to this system be saved in text files until a decision can be made as to what `database(sqlite3)` should be used to store these two entities.

<h2>Features</h2>

- **User login and authentication**
- **Add, list, and search for products**
- **Track transactions**
- **Generate bar charts of products sold**
- **Generate Excel reports of all transactions**

<h2>Debugging Process</h2>

To ensure the Supermarket Management System's reliability, we implemented several debugging steps:

- **Code Review**: Regular reviews and tools like pylint and flake8 ensured code quality.
- **Interactive Debugging**: Leveraged PyCharm's debugger for step-by-step code inspection.
- **Exception Handling**: Added try-except blocks for error management and detailed logging.
- **Database Debugging**: Used SQLite viewers to verify data integrity and tested SQL queries.

# Getting Started
<h2>System Requirements</h2>

To operate this supermarket system, you will need the following:

- **PyCharm IDE**: An integrated development environment for Python.
- **Python 3.10**: The programming language used for this project.
- **SQLite3**: A lightweight, disk-based database used for managing the system's data.

<h2>Installation</h2>
<h3>Steps to Set Up:</h3>

1. **Install PyCharm**:
   Download and install PyCharm from the [official website](https://www.jetbrains.com/pycharm/download/).

2. **Install Python 3.10**:
   Download and install Python 3.10 from the [official Python website](https://www.python.org/downloads/release/python-3100/).

3. **Install SQLite3**:
   SQLite3 is included with Python, but you can verify installation and get more information from the [SQLite website](https://www.sqlite.org/download.html).

4. **Clone the Repository**:
   ```bash
   git clone https://github.com/ChungmanPARK12/SupermarketDAO.git
   cd <python>

# The concept of design

The Supermarket Self-Service_Checkout made up of multiple parts.

<h2>Front end</h2>

![image description](https://github.com/ChungmanPARK12/SupermarketDAO/assets/162090754/95d1f0d5-c846-4860-a753-9696b7457dd8)

* ### Supermarket Class

This Class initializes a `Supermarket` class as a main, manages product scanning, processes payments, prints receipts, and saves transactions, simulating a supermarket checkout system.

* ### Product Class

Defines a `Product` class with attributes for barcode, name, description, and price. Includes methods for printing details and comparing products by barcode.

* ### Transactions Class

Defines a `Transactions` class with attributes for date, barcode, and amount. Includes methods to retrieve the transaction date, barcode, and amount.

* ### CheckoutRegister Class

Defines a `CheckoutRegister` class to manage product scanning, payment processing, and transaction saving. Integrates with `SupermarketDAO` for database operations and handles shopping cart functionality.

<h2>Back End</h2>

![image description](https://github.com/ChungmanPARK12/SupermarketDAO/assets/162090754/d9e2a6e5-dacf-428f-ab48-50aa280b16b4)

* ### SupermarketDAO

Defines a `SupermarketDAO` class to manage supermarket data, including users, products, and transactions, using SQLite3 and OpenPyxl for database operations and report generation. 


* ### StartUp Login

This Class manages the supermarket data with `SupermarketDAO`, offering user login, product management, transaction tracking, and report generation, including bar charts and Excel reports, using SQLite3 and OpenPyxl.

## Summary

This Data Structure and Algorithm project provides a comprehensive collection of essential **algorithms and data structures**. It includes implementations and explanations for **sorting**, **searching**, **graphs**, **trees**, and more. Designed for efficiency and clarity, this project serves as a valuable resource for learning and applying fundamental concepts in computer science.

## Thank you

Thank you for visiting my github :)

