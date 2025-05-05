keranjang = []

for i in range(5):
    keranjang.append(input("masukan keranjang: "))

print("daftar keranjang baru: ", keranjang)

menghapus = input("barang yang sudah ada di keranjang: ")
keranjang.remove(menghapus)

print("daftar keranjang sekarang", keranjang)