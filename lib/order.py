from models import session, Order
from datetime import datetime

# Order Management
def create_order(product_id, quantity):
    order_date = datetime.now().date()
    new_order = Order(product_id=product_id, order_date=order_date, quantity=quantity)
    session.add(new_order)
    session.commit()

def view_orders():
    orders = session.query(Order).all()
    for order in orders:
        print(f"Order Date: {order.order_date} - Product ID: {order.product_id} - Quantity: {order.quantity}")