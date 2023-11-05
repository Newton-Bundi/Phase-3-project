from product import *
from order import *
from supplier import *

while True:
    print("Inventory Management System")
    print("1. Add Product")
    print("2. View Products")
    print("3. Add Supplier")
    print("4. View Suppliers")
    print("5. Create Order")
    print("6. View Orders")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Product Name: ")
        description = input("Product Description: ")
        price = float(input("Product Price: "))
        quantity = float(input("Quantity: "))   
        supplier_id = int(input("Supplier ID: "))
        add_product(name, description, price, quantity, supplier_id)

    elif choice == '2':
        view_products()

    elif choice == '3':
        name = input("Supplier Name: ")
        contact_info = input("Contact Information: ")
        add_supplier(name, contact_info)

    elif choice == '4':
        view_suppliers()

    elif choice == '5':
        product_id = int(input("Product ID for the Order: "))
        quantity = int(input("Quantity: "))
        create_order(product_id, quantity)

    elif choice == '6':
        view_orders()

    elif choice == '0':
        break