num_items = int(input("Enter the number of items: "))
total_harga = 0
for i in range(num_items):
    price = int(input("Enter the price of item " + str(i+1) + ": "))
    total_harga += price

print("total barang: Rp", total_harga)
