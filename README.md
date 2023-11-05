# Inventory Management System

A CLI application that allows businesses to keep track of their products, suppliers, and orders. 
This project incorporates Object-Oriented Programming (OOP), Object-Relational Mapping (ORM) to interact with a database.
Users can manage their inventory, create purchase orders, and track product availability.

# Steps on running the application

1. Kindly clone the repository and navigate to the directory.
2. Run **pipenv install** to install all the dependancies
3. Run **pipenv shell** to access the virtual environment
4. Navigate to the lib folder using 'cd lib'
5. Run **python app.py** to execute the application
6. You'll then be prompted to provide inputs including
     - **Add product** - Adds a new product to the inventory.
     - **View products** - Displays all the products in the inventory
     - **Add supplier** - Adds a new supplier 
     - **View Suppliers** - Displays all the products
     - **Create order** - Create a new order
     - **View orders** - Dispalays all the orders
     - **Exit** - Exits the application
7. Kindly provide all the requested information, which will be persisted in the database.

# Features of the applications
1. A Pipfile contains all needed dependencies and no unneeded dependencies. -
2. Utilizes 2 external libraries - SQLachemy and Alembic
3. Uses SQLAlchemy ORM to create 3 tables: Products, Suppliers and Orders
4. Uses Alembic to manage migrations
5. Uses SQLAlchemy ORM to execute queries and convert data into CLI-usable format.
6. A CLI that validates user input: Supplier email
7. A CLI that provides detailed prompts and messages to the user throughout the execution of the CLI.
