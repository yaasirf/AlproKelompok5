# pesan selamat datang untuk pelanggan
print("Selamat datang di Pizza Hut Delivery!")
# Pseudocode
# Harga awal pizza
harga_pizza = 0
# Menammpilkan daftar menu
print("Menu:")
print("1.Frankfutter BBQ")
print("2.Meat Monsta")
print("3.American Favourite")
print("4.Meat Lovers")
print("5.Chicken Lovers")
print("6.Super Supreme")
print("7.Super Supreme Chicken")
print("8.Cheese Lovers")
#  pelanggan menginputkan menu pizza yang ingin dipesan
menu = int(input("Pilih pizza yang diinginkan: "))
# menampilkan crust pizza
print("==================================================")
print("Crust Pizza:")
print("1. Pan ")
print("2. Stuffedcrust Cheese")
print("3. Stuffedcrust Sausage")
print("4. Cheesy Bites")
# pelanggan menginputkan pilihan crust
crust = int(input("Pilih crust yang diinginkan: "))
# Menampilkan Ukuran pizza
print("==================================================")
print("Ukuran Pizza:")
print("1. Personal ")
print("2. Regular ")
print("3. Large ")
# pelanggan menginputkan pilihan ukuran
ukuran = int(input("Pilih ukuran pizza yang anda inginkan: "))
# dictionary daftar menu
daftar_menu = {
    1:"Frankfutter BBQ",
    2:"Meat Monsta",
    3:"American Favourite",
    4:"Meat Lovers",
    5:"Chicken Lovers",
    6:"Super Supreme",
    7:"Super Supreme Chicken",
    8:"Cheese Lovers"
}
# dictionary daftar crust
daftar_crust = {
    1:"Pan",
    2:"Stuffedcrust Cheese",
    3:"Stuffedcrust Sausage",
    4:"Cheesy Bites"
}
# dictionary daftar ukuran
daftar_ukuran = {
    1:"Personal",
    2:"Regular",
    3:"Large"
}
