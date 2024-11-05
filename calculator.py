def tambah(x, y):
    return x + y
def kurang(x, y):
    return x - y
# Menambahkan Fungsi untuk operasi perkalian
def kali(x, y):
    return x * y
# Update menambah Fungsi untuk operasi pembagian
def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Pembagi harus > 0!"

print("Pilih Salah satu oprasi:")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

pilihan = input("Masukkan IPilihan: ")

# Meminta input angka pertama dan kedua
angka1 = float(input("Masukkan angka: "))
angka2 = float(input("Masukkan angka kedua: "))

# Melakukan operasi berdasarkan pilihan
if pilihan == '1':
    print(f"{angka1} + {angka2} = {tambah(angka1, angka2)}")
elif pilihan == '2':
    print(f"{angka1} - {angka2} = {kurang(angka1, angka2)}")
elif pilihan == '3':
    print(f"{angka1} * {angka2} = {kali(angka1, angka2)}")
elif pilihan == '4':
    print(f"{angka1} / {angka2} = {bagi(angka1, angka2)}")
else:
    print("Pilihan tidak sesuai!")
