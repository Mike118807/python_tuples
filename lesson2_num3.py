# Problem Statement: You are given a list of tuples, each representing 
# a customer's order. Each tuple contains the customer's name, the product ordered,
# and the quantity. Your task is to unpack each tuple and print the order details
# in a user-friendly format.

def process_orders(orders):
    for customer_name, product, quantity in orders:
        print(f"{customer_name} orders {quantity} {product}(s)")


# Order Data:

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

# Usage

process_orders(orders)