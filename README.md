# SuperMart-Billing-System-In-Python-With-File-Handing.
# Overview:
The Supermart Billing System is a Python console-based application designed to manage billing operations for a grocery store. Built using Object-Oriented Programming (OOP) principles, it provides functionalities for both administrators and buyers, including product management and receipt generation. The system features a user-friendly interface with colorful ASCII art (using the colorama library) and supports file-based data storage for persistent product information.

# Features:
# 1.Administrator Mode:
Add, modify, or delete products in the inventory.
Secured with a hardcoded username and password (default: AdilTufail / Adil2903).
# 2.Buyer Mode:
Generate receipts for purchased products.
Input buyer and cashier details, along with date and time.
Apply discounts and calculate total amounts.

# 3.Product Management:
Store product details (code, name, price, discount, quantity) in a text file (Database7.txt).
List all available products.

# User Interface:
Colorful console output using colorama for enhanced visuals.
Custom ASCII logo and title for branding.

# Data Persistence:
Uses file I/O to save and retrieve product data.

# Project Structure
# 1.Classes:
Bill: Base class handling core functionalities like menu navigation, logo display, and receipt generation.
Product: Derived class extending Bill to manage product-specific operations (add, edit, delete).

# Key Methods:
print_title(): Displays the Supermart title in ASCII art.
logo(): Shows the store's logo with contact and location details.
menu(): Main menu for selecting Administrator or Buyer mode.
administrator(): Admin menu for product management.
buyer(): Buyer menu for placing orders and generating receipts.
add_product(), edit_product(), remove_product(): Manage inventory.
list_of_item(): Displays all products.
receipt(): Generates a detailed receipt for purchases.


# File Handling:
Product data is stored in Database7.txt.
Temporary files are used for editing and deleting products.

# Clone the repository:git clone https://github.com/Adil-Tufail-Chandio110/SuperMart-Billing-System-In-Python-With-File-Handing./tree/main

# Navigate to the project directory:cd supermart-billing-system
# Install the required dependency:pip install colorama
# Run the program:python main.py

# Usage:
1.Run the Program:
Execute python main.py to start the application and access the main menu.
2.Main Menu Options:
Administrator: Log in with username AdilTufail and password Adil2903 to manage products.
3.Buyer: Enter buyer and cashier details, then place orders to generate receipts.
Exit: Close the program.
4.Administrator Actions:
Add, modify, or delete products in the inventory.
View the product list.
5.Buyer Actions:
View available products.
Enter product codes and quantities to create a receipt with calculated totals and discounts.

# File Structure:

main.py: Source code containing the entire program.
Database7.txt: Text file for storing product data (created automatically).
TempDatabase.txt: Temporary file used during product modification/deletion.

# Limitations:
Basic authentication with hardcoded credentials.
Limited error handling for invalid inputs (e.g., non-numeric values).
File-based storage may not scale for large datasets.
Console-based interface limits user interaction compared to GUI applications.

# Future Improvements:
Enhance input validation for robust error handling.
Implement a secure authentication system.
Support a database (e.g., SQLite) for better scalability.
Add features like sales reports or low-stock alerts.
Develop a graphical user interface (GUI) for improved user experience.

# Contributing:
Contributions are welcome! Please fork the repository and submit a pull request with your changes.
# License:
This project is licensed under the BSD 3-Clause License. See below for details:
BSD 3-Clause License

Copyright (c) 2025, Adil Tufail
All rights reserved.

# Author:
Developed by Adil Tufail.
