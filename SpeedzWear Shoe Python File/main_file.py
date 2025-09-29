#main_file
from operation import process_sale, process_restock
from read_file import read_shoes_file
from write_file import write_stock_file

def display_stock(shoes):
    if not shoes:
        print("\nNo shoes in stock.\n")
        return
    print("\n--- Current Stock ---")
    print("{:<20} {:<12} {:<8} {:<10} {:<12}".format("Type", "Brand", "Qty", "Price", "Origin"))
    print("-"*70)
    for shoe in shoes:
        print("{:<20} {:<12} {:<8} {:<10} {:<12}".format(
            shoe["type"], shoe["brand"], shoe["quantity"], shoe["price"], shoe["origin"]
        ))
    print("-"*70 + "\n")

def main():
    # Load stock from file
    shoes = read_shoes_file("shoes.txt")   

    # Display stock once at program start
    display_stock(shoes)

    while True:
        print("\n============== Shoe Sales System =============")
        print("============ WELCOME TO SPEEDZWEAR SHOES ========")
        print("1. Sell Shoes")
        print("2. Restock Shoes")
        print("3. Display Stock")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            process_sale(shoes)
            write_stock_file("shoes.txt", shoes)
        elif choice == "2":
            process_restock(shoes)
            write_stock_file("shoes.txt", shoes)   
        elif choice == "3":
            # Refresh stock from file and display
            shoes = read_shoes_file("shoes.txt")
            display_stock(shoes)
            input("Press Enter to return to the main menu...")
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
main()

