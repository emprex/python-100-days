# Cashier Billing System
# This script accepts multiple product purchases, collects membership type,
# applies the appropriate discount, and prints the final bill.

def collect_products():
    """
    Collects product details from the user.
    Loops until the user chooses to stop adding products.
    Returns a list of product dictionaries.
    """
    products = []
    while True:
        name = input("Enter product name: ")
        
        # Validate quantity input
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                break
            except ValueError:
                print("Error: Please enter a valid NUMBER for quantity.")

        # Validate price input
        while True:
            try:
                price = float(input("Enter price per item: £"))
                break
            except ValueError:
                print("Error: Please enter a valid PRICE.")

        # Store product details in a dictionary and append to the list
        products.append({'name': name, 'quantity': quantity, 'price': price})

        # Ask if user wants to add another product
        more = input("Add another product? (yes/no): ").strip().lower()
        if more != "yes":
            break
    return products

def get_membership():
    """
    Collects membership type from the user.
    Returns the membership as a formatted string.
    If invalid, defaults to 'No' membership.
    """
    membership = input("Membership type (NO, Gold, Silver, Bronze): ").strip().capitalize()
    if membership not in ['No', 'Gold', 'Silver', 'Bronze']:
        print("Invalid membership; defaulting to NO membership.")
        membership = 'No'
    return membership

def calculate_total(products):
    """
    Given a list of products, calculates and returns the subtotal.
    """
    subtotal = 0
    for prod in products:
        line_total = prod['quantity'] * prod['price']
        subtotal += line_total
    return subtotal

def get_discount_rate(membership):
    """
    Returns the discount rate (as a decimal) associated with the given membership tier.
    """
    rates = {
        'No': 0.00,      # No membership: 0% discount
        'Gold': 0.30,    # Gold: 30% discount
        'Silver': 0.10,  # Silver: 10% discount
        'Bronze': 0.05   # Bronze: 5% discount
    }
    return rates.get(membership, 0.00)

def print_bill(products, subtotal, discount_rate):
    """
    Prints a detailed receipt, showing each item, subtotal, applied discount, and final total.
    """
    print("\n--- Final Receipt ---")
    for item in products:
        line_total = item['quantity'] * item['price']
        print(f"{item['quantity']} x {item['name']} @ £{item['price']:.2f} = £{line_total:.2f}")
    print(f"Subtotal: £{subtotal:.2f}")
    print(f"Discount: {int(discount_rate * 100)}%")
    print(f"Discounted amount: -£{subtotal * discount_rate:.2f}")
    print(f"Total to pay: £{subtotal - (subtotal * discount_rate):.2f}")

# --- Main Program Entry Point ---
if __name__ == "__main__":
    # Step 1: Gather all purchased products
    products = collect_products()
    
    # Step 2: Get the customer's membership type
    membership = get_membership()
    
    # Step 3: Calculate subtotal (sum of all products)
    subtotal = calculate_total(products)
    
    # Step 4: Determine discount rate based on membership
    discount_rate = get_discount_rate(membership)
    
    # Step 5: Print the final bill with proper formatting
    print_bill(products, subtotal, discount_rate)
