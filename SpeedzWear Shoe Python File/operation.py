from datetime import datetime
from write_file import print_sale_invoice, print_restock_invoice, write_stock_file

def find_shoe(shoes, shoe_type):
    """Find shoe in stock list and validate required fields."""
    for shoe in shoes:
        if shoe['type'].lower() == shoe_type.lower():
            # Validate required fields
            if not all(key in shoe for key in ['type', 'brand', 'quantity', 'price', 'origin']):
                print(f"Error: Shoe {shoe_type} missing required fields.")
                return None
            # Normalize origin to lowercase for consistency
            shoe['origin'] = shoe['origin'].lower().strip()
            return shoe
    print(f"Error: Shoe {shoe_type} not found in stock.")
    return None

def process_sale(shoes):
    """Handle selling multiple shoes with discount and proper validation."""
    while True:
        customer = input("Customer name: ")
        if customer.strip() == "":
            print("Error: Customer name must be valid.")
        else:
            try:
                int(customer)  # If this succeeds, it's only a number
                print("Error: Customer name cannot be only numbers.")
            except ValueError:  # Conversion failed → contains letters
                break

    sold_items = []
    while True:
        shoe_type = input("Enter shoe type to sell (or 'done' to finish): ")
        if shoe_type.lower() == "done":
            break

        # Find shoe
        shoe = find_shoe(shoes, shoe_type)
        if not shoe:
            continue

        # Validate quantity
        try:
            qty = int(input(f"Enter quantity to sell for {shoe['type']}: "))
            if qty <= 0:
                print("Quantity must be greater than 0!")
                continue
        except ValueError:
            print("Quantity must be a number.")
            continue

        if qty > shoe['quantity']:
            print(f"Not enough stock. Available quantity: {shoe['quantity']}")
            continue

        # Apply discount logic according to the product and quantity
        discount = 0
        if qty >= 10:
            if shoe['origin'] == "international":
                discount = 0.05  # 5% discount for international shoes when qty >= 10
                print(f"Applying 5% discount for {qty} international {shoe['type']}")
            elif shoe['origin'] == "domestic":
                discount = 0.07  # 7% discount for domestic shoes when qty >= 10
                print(f"Applying 7% discount for {qty} domestic {shoe['type']}")
            else:
                print(f"Warning: Unknown origin '{shoe['origin']}' for {shoe['type']}. No discount applied.")

        total = qty * shoe['price']
        discounted_total = total * (1 - discount)
        print(f"Item: {shoe['type']}, Qty: {qty}, Price: ${shoe['price']}, "
              f"Discount: {discount*100}%, Total before: ${total:.2f}, Total after: ${discounted_total:.2f}")

        sold_items.append({
            "type": shoe['type'],
            "brand": shoe['brand'],
            "quantity": qty,
            "price": shoe['price'],
            "origin": shoe['origin'],
            "discount": discount * 100,  # Store as percentage for invoice
            "total": discounted_total
        })

        # Update stock
        shoe['quantity'] -= qty

    if sold_items:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        invoice_file = f"sale_invoice_{customer.replace(' ', '')}_{timestamp}.txt"
        print_sale_invoice(invoice_file, sold_items, customer)
        write_stock_file("shoes.txt", shoes)
        print(f"Sale completed! Invoice saved as {invoice_file}")
    else:
        print("No items were sold.")

def process_restock(shoes):
    """Handle restocking multiple shoes"""
    try:
        while True:
            vendor = input("Vendor name: ")
            if vendor.strip() == "":
                print("Error: Vendor name must be valid.")
            else:
                try:
                    int(vendor)  # If this succeeds, it's only a number
                    print("Error: Vendor name cannot be only numbers.")
                except ValueError:  # Conversion failed → contains letters
                    break

        restocked_items = []
        item_counter = 1
        
        while True:
            shoe_type = input("Shoe type to restock (or 'done' to finish): ")
            if shoe_type.lower() == "done":
                break

            shoe = find_shoe(shoes, shoe_type)
            if shoe:
                try:
                    qty = int(input(f"Quantity to add for {shoe['type']}: "))
                    if qty <= 0:
                        print("Quantity must be greater than 0!")
                        continue

                    shoe['quantity'] += qty
                   
                    restocked_items.append({
                        "id": item_counter,
                        "type": shoe['type'],
                        "brand": shoe['brand'],
                        "quantity": qty,
                        "price": shoe['price'],
                        "origin": shoe['origin']
                    })
                    item_counter += 1
                    print(f"Restocked {qty} {shoe['type']}")

                except ValueError:
                    print("Invalid input! Please enter a number.")
            else:
                continue

        if restocked_items:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"invoice_restock_{vendor.replace(' ', '')}_{timestamp}.txt"
            print_restock_invoice(vendor, restocked_items, filename)
            write_stock_file("shoes.txt", shoes)
            print(f"Restock completed! Invoice saved as {filename}")
        else:
            print("No items were restocked.")

    except Exception as e:
        print("Error in process_restock:", e)

    return shoes
