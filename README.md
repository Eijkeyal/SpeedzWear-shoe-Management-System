# 🥿 SpeedzWear Shoe Management System

A **Python-based console application** for managing wholesale shoe inventory, sales, and restocking.  
The system is designed for wholesalers to streamline operations by keeping track of stock, generating invoices, applying discounts, and recording transactions using file handling.

## 🚀 Features

- **Inventory Management** – View, add, and update shoe stock efficiently.  
- **Billing System** – Sell shoes and generate detailed invoices with cost breakdown.  
- **Discount Handling** – Automatic discounts based on purchase quantity or type.  
- **Stock Updates** – Inventory adjusts automatically after each transaction.  
- **File Handling** – Records sales and restocking in external text files for persistence.  
- **Interactive Console Menu** – Simple, text-based interface for easy navigation.  

## 📂 Folder Structure

```text
SpeedzWear-Shoes-System/
│
├── main.py               # Main program file
├── operation             # Stores current shoe stock
├── sales.txt             # Records sales transactions
├── Write_file            # Generates restock & sales invoices
├── Read_file             # Reads all text files
└── README.md             # Project documentation

```
## 📦 Installation & Usage
1. Clone the repository  
```bash
git clone https://github.com/eijkeyalpakhrin/SpeedzWear-Shoes-System.git
cd SpeedzWear-Shoes-System
2. Run the program  
 -python main.py
```

🛠️ **Built With**  
- Python 3.x – Core programming language  
- File Handling – Persistent storage of inventory & transactions  
- Modular Programming – Program structured using modules for better organization  
- Data Structures – Lists and dictionaries for stock management  

🧪 **Requirements**  
- Python 3.x  
- No external libraries required – Uses only built-in Python modules   

python main.py
📸 Example Output
1️⃣ Display Current Stock

```
--- Current Stock ---
Type                 Brand        Qty      Price      Origin      
----------------------------------------------------------------------
Loafer Light         GoldStar     965      1000.0     domestic
Inigo 732            Caliber      50       2800.0     domestic
Lite Racer           Adidas       60       7000.0     international
Air Max              Nike         80       8500.0     international
Classic Clog         Crocs        0        3200.0     international
...
======================================================================

2️⃣ Selling Shoes
============== Shoe Sales System =============
============ WELCOME TO SPEEDZWEAR SHOES ========
1. Sell Shoes
2. Restock Shoes
3. Display Stock
4. Exit
Enter your choice (1-4): 1

Customer name: Eijkeyal Pakhrin
Enter shoe type to sell (or 'done' to finish): Loafer Light

Enter quantity to sell for Loafer Light: 30

Applying 7% discount for 30 domestic Loafer Light
Item: Loafer Light, Qty: 30, Price: $1000.0, Discount: 7.0%, Total before: $30000.00, Total after: $27900.00

================== SALE INVOICE ==================
Date: 2025-09-13 14:00:55
Customer: Eijkeyal Pakhrin

Type           Brand          Qty  Price     Origin         Discount  Total     
Loafer Light   GoldStar       30   1000.00   domestic       7.0%    27900.00  
Lite Racer     Adidas         30   7000.00   international  5.0%    199500.00 
Air Max        Nike           80   8500.00   international  5.0%    646000.00 

Total Amount = 873400.0
Sale completed! Invoice saved as sale_invoice_EijkeyalPakhrin_20250913_140055.txt

3️⃣ Restocking Shoes
============== Shoe Sales System =============
Enter your choice (1-4): 2
Vendor name: Eijkeyal
Shoe type to restock (or 'done' to finish): loafer light
Quantity to add for Loafer Light: 300

Restocked 300 Loafer Light
Shoe type to restock (or 'done' to finish): lite racer
Quantity to add for Lite Racer: 300

Restocked 300 Lite Racer
Shoe type to restock (or 'done' to finish): done

================= RESTOCK INVOICE ==================
Date: 2025-09-13 14:01:38
Vendor: Eijkeyal

Type           Brand          Qty  Price     Origin              
Loafer Light   GoldStar       300  1000.0    domestic            
Lite Racer     Adidas         300  7000.0    international       

Total Amount = 2400000.0
Restock completed! Invoice saved as invoice_restock_Eijkeyal_20250913_140138.txt

4️⃣ Updated Stock After Transactions
--- Current Stock ---
Type                 Brand        Qty      Price      Origin      
----------------------------------------------------------------------
Loafer Light         GoldStar     1235     1000.0     domestic
Inigo 732            Caliber      50       2800.0     domestic
Lite Racer           Adidas       330      7000.0     international
Air Max              Nike         0        8500.0     international
Classic Clog         Crocs        0        3200.0     international
======================================================================

5️⃣ Exit Program
Enter your choice (1-4): 4
Exiting... Goodbye!

```
📌 **Future Enhancements**  
- Add a graphical user interface (GUI) for better user experience  
- Enable PDF invoice export for professional reporting  
- Integrate a database (MySQL/SQLite) instead of text files  
- Multi-user roles (admin, staff, customer)

## 📈 Project Status
✅ Completed – ready to use.  
🔧 Future improvements are possible, but no further updates are currently planned.
  
## 👤 Author  
**Eijkeyal Pakhrin**
– Developer & Maintainer

- GitHub: [@Eijkeyal](https://github.com/Eijkeyal)  
- LinkedIn: [Eijkeyal Pakhrin](https://www.linkedin.com/in/eijkeyalpakhrin)
- Credly: [Eijkeyal Pakhrin](https://credly.com/users/eijkeyal-pakhrin)
  

🤝 Contributing
Contributions, issues, and feature requests are welcome!  
If you want to contribute:  
1. Fork the repository  
2. Create a new branch (`git checkout -b feature-name`)  
3. Make your changes and commit (`git commit -m "Add feature"`)  
4. Push to the branch (`git push origin feature-name`)  
5. Open a Pull Request

🙌 Acknowledgements
-Inspired by real-world wholesale shoe management needs.
-Learned concepts of file handling and modular programming from Python documentation and online tutorials.
-Thanks to **Arayan Thapa** and **Pratik Panta** for guidance and support.
- Inspired by real-world wholesale shoe management needs.  
- Learned concepts of file handling and modular programming from Python documentation and online tutorials.  
- Thanks to **Arayan Thapa** and **Pratik Panta** for guidance and support.

⭐ *If you like this project, don’t forget to star the repo!* ⭐

