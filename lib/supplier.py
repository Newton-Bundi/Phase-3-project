from models import session, Supplier

# Supplier Management
def add_supplier(name, contact_info):
    new_supplier = Supplier(name=name, contact_info=contact_info)
    session.add(new_supplier)
    session.commit()

def view_suppliers():
    suppliers = session.query(Supplier).all()
    for supplier in suppliers:
        print(f"{supplier.id}: {supplier.name} - Contact: {supplier.contact_info}")
