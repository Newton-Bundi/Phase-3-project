from models import session, Product

# Product Management
def add_product(name, description, price,quantity,supplier_id):
    new_product = Product(name=name, description=description, price=price, quantity=quantity, supplier_id=supplier_id)
    session.add(new_product)
    session.commit()

def view_products():
    products = session.query(Product).all()
    for product in products:
        print(f"{product.id}: {product.name} - ${product.price} - Quantity: {product.quantity} - Supplier: {product.supplier_id}")
