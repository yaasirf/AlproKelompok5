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
# mengambil nama dari nomor yang diinputkan
pilihan_menu = daftar_menu[menu]
pilihan_crust = daftar_crust[crust]
pilihan_ukuran = daftar_ukuran[ukuran]
# Menentukan harga jika memilih crust pan
if crust == 1:
    # harga awal jika memilih crust pan
    harga_pizza += 40909
    # Menentukan harga berdasarkan ukuran pizza
    if ukuran == 1:
        harga_pizza += 0
    elif ukuran == 2:
        # jika pelanggan memilih ukuran regular
        # harga pizza akan ditambah Rp.55.455
        harga_pizza += 55455
    else:
        # jika pelanggan memilih ukuran Large
        # harga pizza akan ditambah Rp.85.455
        harga_pizza += 85455    
# Menentukan harga jika pelanggan memilih crust stuffedcrust cheese
elif crust == 2:
    # harga awal jika memilih crust stuffedcrust cheese
    harga_pizza += 52727
    # Menentukan harga berdasarkan ukuran pizza
    if ukuran == 1:
        harga_pizza += 0
    elif ukuran == 2:
        # jika pelanggan memilih ukuran regular
        # harga pizza akan ditambah Rp.63.637
        harga_pizza += 63637
    else:
        # jika pelanggan memilih ukuran Large
        # harga pizza akan ditambah Rp.100.909
        harga_pizza += 100909
# menentukan harga jika pelanggan memilih crust stuffedcrust sausage        
elif crust == 3:
    # harga awal jika memilih crust stuffedcrust cheese
    harga_pizza += 50000
    # Menentukan harga berdasarkan ukuran pizza
    if ukuran == 1:
        harga_pizza += 0
    elif ukuran == 2:
        # jika pelanggan memilih ukuran regular
        # harga pizza akan ditambah Rp.62.727
        harga_pizza += 62727
    else:
        # jika pelanggan memilih ukuran Large
        # harga pizza akan ditambah Rp.99.091
        harga_pizza += 99091
        
