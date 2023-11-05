from models import session, Supplier
import re

# Supplier Management
def is_valid_email(email):
    # Basic email format validation using a regular expression
    email_regex = r'^\S+@\S+\.\S+'
    return re.match(email_regex, email)

def add_supplier():
    name = input("Supplier Name: ")
    contact_info = input("Contact Information (Email): ")

    if is_valid_email(contact_info):
        new_supplier = Supplier(name=name, contact_info=contact_info)
        session.add(new_supplier)
        session.commit()
        print("Supplier added successfully.")
    else:
        print("Invalid email address format. Supplier not added.")

def view_suppliers():
    suppliers = session.query(Supplier).all()
    for supplier in suppliers:
        print(f"{supplier.id}: {supplier.name} - Contact: {supplier.contact_info}")
