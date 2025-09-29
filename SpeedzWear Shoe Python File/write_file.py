#write_file
from datetime import datetime

def print_sale_invoice(filename, items, customer):
    print("\n================== SALE INVOICE ==================")
    print("Date:\t", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Customer:" + customer + "\n")
    print("-" * 95)
    print(f"{'Type':<15}{'Brand':<15}{'Qty':<5}{'Price':<10}"
          f"{'Origin':<15}{'Discount':<10}{'Total':<10}")
    print("-" * 95)

    total_amount = 0
    for item in items:
        original_total = item['quantity'] * item['price']
        discount_amount = original_total - item['total']  # Calculate discount amount
        total_amount += item['total']
        
        print(f"{item['type']:<15}{item['brand']:<15}{item['quantity']:<5}"
              f"{item['price']:<10.2f}{item['origin']:<15}"
              f"{item['discount']:.1f}%{'':<4}{item['total']:<10.2f}")
           

    print("-" * 95)
    print("Total Amount =", total_amount)
    print("=" * 95)

    # Save invoice to file
    with open(filename, "w") as f:
        f.write("\n================== SALE INVOICE ==================\n")
        f.write("Date:\t" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        f.write("Customer: " + customer + "\n")
        f.write("-" * 80 + "\n")
        f.write(f"{'Type':<15}{'Brand':<15}{'Qty':<5}{'Price':<10}"
                f"{'Origin':<20}{'Discount':<10}{'Total':<10}\n")
        f.write("-" * 80 + "\n")

        for item in items:
            f.write(f"{item['type']:<15}{item['brand']:<15}{item['quantity']:<5}"
                    f"{item['price']:<10.2f}{item['origin']:<20}"
                    f"{item['discount']}%{'':<4}{item['total']:<10.2f}\n")

        f.write("-" * 80 + "\n")
        f.write("Total Amount = " + str(total_amount) + "\n")
        f.write("=" * 80 + "\n")
''
       
def print_restock_invoice(vendor, items, filename):
    print("================= RESTOCK INVOICE ==================")
    print("Date:\t", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Vendor:\t" + vendor + "\n")
    print("-"*80)
    print(f"{'Type':<15}{'Brand':<15}{'Qty':<5}{'Price':<10}{'Origin':<20}")
    print("-"*80)

    total_amount = 0
    for item in items:
        line_total = item['quantity'] * item['price']
        total_amount += line_total
        print(f"{item['type']:<15}{item['brand']:<15}{item['quantity']:<5}{item['price']:<10}{item['origin']:<20}")

    print("-"*80)
    print("Total Amount =", total_amount)
    print("="*80)

    # Save invoice to file
    with open(filename, "w") as f:
        f.write("\n================= RESTOCK INVOICE ==================\n")
        f.write("Date:\t" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        f.write("Vendor:" + vendor + "\n")
        f.write("-"*80 + "\n")
        f.write(f"{'Type':<15}{'Brand':<15}{'Qty':<5}{'Price':<10}{'Origin':<20}\n")
        f.write("-"*80 + "\n")
        for item in items:
            line_total = item['quantity'] * item['price']
            f.write(f"{item['type']:<15}{item['brand']:<15}{item['quantity']:<5}{item['price']:<10}{item['origin']:<20}\n")
        f.write("-"*80 + "\n")
        f.write("Total Amount = " + str(total_amount) + "\n")
        f.write("="*80 + "\n")
''

# ---------------- UPDATE STOCK FILE ----------------
def write_stock_file(filename, shoes):
    with open(filename, "w") as f:
        for shoe in shoes:
            f.write(f"{shoe['type']}\t{shoe['brand']}\t{shoe['quantity']}\t{shoe['price']}\t{shoe['origin']}\n")
   








