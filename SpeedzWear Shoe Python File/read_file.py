#Read_file

def read_shoes_file(filename):
    shoes = []
    try:
        with open(filename, "r") as file:
            for line in file:
                if line == "\n":
                    continue

                parts = line.split("\t")  
                if len(parts) != 5:
                    print("Skipping invalid line:", line)
                    continue

                shoe_type, brand, qty, price, origin = parts

                try:
                    shoes.append({
                        "type": shoe_type,
                        "brand": brand,
                        "quantity": int(qty),
                        "price": float(price),
                        "origin": origin
                    })
                except ValueError:
                    print("Skipping invalid line:", line)
    except FileNotFoundError:
        print("File not found:", filename)

    return shoes

