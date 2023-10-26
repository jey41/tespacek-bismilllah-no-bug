import json
import pwinput
import os
from prettytable import PrettyTable 
os.system("cls")


# dictionary
akun_admin = {"Username" : ["admin1"],
            "Password" : ["123"]} #aku admin supermarket AHA

# prettytable
etalase_produk = PrettyTable()      #untuk memanggil prettytable menampilkan daftar produk
etalase_produk.field_names = ["ID Produk","Nama Produk","Harga Produk", "Stok Produk"]

# json login
json_path_login = "C:\\Users\\Hisyam\\OneDrive\\Desktop\\Kuliah\\Semester 1\\lry and eror\\pa alisa\\data_user.json"
jsonlogin = json_path_login
with open(jsonlogin, "r") as read_user:
    user = json.load(read_user)

def tambah_user(datauser):
    with open(jsonlogin, "w") as add_user:
        json.dump(datauser, add_user, indent=4)

nm = user.get("Usernames")
pw = user.get("Passwords")

# json produk
json_path_produk = "C:\\Users\\Hisyam\\OneDrive\\Desktop\\Kuliah\\Semester 1\\lry and eror\\pa alisa\\produk.json"
jsonproduk = json_path_produk   #untuk membuka file json yang menyimpan
with open(jsonproduk, "r") as baca_produk:
    produk = json.load(baca_produk)

def penyimpanan():
    with open("produk.json", "w") as sn:
        json.dump(produk, sn)

ip = produk.get("ID Produk")
np = produk.get("Nama Produk")
hp = produk.get("Harga Produk")
sp = produk.get("Stok Produk")

# function login admin
def login_admin():
    print("""
    ==============================
    |        LOGIN ADMIN         |
    ==============================
        """)

    while True : 
        try :
            input_username = input("Masukkan username : ")
            input_password = pwinput.pwinput("Masukkan Password : ")

            user_admin = akun_admin.get("Username").index(input_username)
            password_admin = akun_admin.get("Password").index(input_password)

            if input_username == akun_admin.get("Username")[user_admin] and input_password == akun_admin.get("Password")[password_admin]:
                print("")
                print("        --- LOGIN BERHASIL ---\n")
                print("Selamat datang,", input_username)
                menuHomeAdmin()
                break  # Hanya berhenti jika login berhasil
            else:
                print("\n> USERNAME ATAU PASSWORD SALAH")
                print("> SILAHKAN COBA LAGI\n")
        except ValueError:
            print("\n> TERJADI KESALAHAN")
            print("> SILAHKAN COBA LAGI\n")

# function registrasi akun baru
def regis():
    print("""
    ==============================
    |    REGISTRASI AKUN BARU    |
    ==============================
        """)
    while True:
        try :
            uname = input("Masukkan username: ")
            if all(x.isspace () for x in uname):
                print("> INPUT TIDAK BOLEH KOSONG")
                print("> Coba lagi\n")
                
            elif all(x.isalpha() for x in uname):
                if uname in user["Usernames"]:
                    print("> USERNAME TELAH TERDAFTAR\n")
                    while True :
                        login_pembeli()
                        break
                else:
                    password = pwinput.pwinput("Masukkan password: ")
                    if all(x.isspace () for x in password):
                        print("> INPUT TIDAK BOLEH KOSONG, COBA ULANG\n")
                        
                    elif all(x.isnumeric() for x in password):
                        nm.append(uname)
                        pw.append(password)
                        tambah_user(user)
                        
                        os.system('cls')
                        print("\n---- AKUN BERHASIL DIBUAT ----")
                        menu_pembeli()
                        break
                    else :
                        print("> PASSWORD HARUS BERNILAI ANGKA")
            else:
                print("> USERNAME YANG DIMASUKAN HARUS ALPHABET")
        except ValueError:
            print("> INVALID INPUT\n")

def menuHomeAdmin ():
    while True :
        try :
            tampilan_admin ()
            pilihan = input("Masukkan pilihan (1/2/3/4/5) : ")

            if pilihan == "1":
                os.system("cls")
                while True:
                    create()
                    while True:
                        lanjut = input("Mau nambah data lagi? (y/t): ")
                        tambah_lagi = lanjut.lower()
                        if tambah_lagi == "y":
                            create()
                        elif tambah_lagi == "t":
                            os.system('cls')
                            menuHomeAdmin()
                        else :
                            print("> INPUT HARUS BERUPA (y/t)")
            elif pilihan == "2":
                os.system("cls")
                while True :
                    read()
                    while True:
                        
                        lanjut = input("Mau kembali ke menu? (y/t): ")
                        tambah_lagi = lanjut.lower()
                        if tambah_lagi == "y":
                            os.system('cls')
                            menuHomeAdmin()
                        elif tambah_lagi == "t":
                            break
                        else :
                            print("> INPUT HARUS BERUPA (y/t)")
            elif pilihan == "3":
                os.system("cls")
                while True:
                    update()
                    while True:
                        lanjut = input("Mau nambah data lagi? (y/t)")
                        tambah_lagi = lanjut.lower()
                        if tambah_lagi == "y":
                            create()
                        elif tambah_lagi == "t":
                            os.system('cls')
                            menuHomeAdmin()
                        else :
                            print("> INPUT HARUS BERUPA (y/t)")
                            
            elif pilihan == "4":
                os.system("cls")
                while True:
                    delete()
                    while True:
                        lanjut = input("Mau nambah data lagi? (y/t)")
                        tambah_lagi = lanjut.lower()
                        if tambah_lagi == "y":
                            create()
                        elif tambah_lagi == "t":
                            os.system('cls')
                            menuHomeAdmin()
                        else :
                            print("> INPUT HARUS BERUPA (y/t)")
                
            elif pilihan == "5":
                os.system("cls")    
                break
            
            else:
                print("> PILIHAN HARUS DARI 1-5, COBA LAGI")
                menuHomeAdmin()

        except Exception as e:
            print(f"> TERJADI KESALAHAN: {str(e)}")


def login_pembeli ():
    print("""
    ==============================
    |        LOGIN PEMBELI       |
    ==============================
        """)

    while True :
        uname = input("Masukkan username: ")
        password = pwinput.pwinput("Masukkan password: ")
        uname_user = nm.index(uname)

        if uname == nm[uname_user] and password == pw[uname_user]:
            print("                      ---LOGIN BERHASIL---\n")
            print("Selamat Datang", uname)
            menuHomepembeli()
            break
            

def tampilan_awal():
    print("""
    -----------------------------
    |        LOGIN SEBAGAI      |
    -----------------------------
    |1.|         ADMIN          |
    |2.|        PEMBELI         |
    |3.|        KELUAR          |
    -----------------------------
        """)
    
def tampilan_pembeli() :
    print("""
    ------------------------------
    |         OPSI LOGIN         |
    ------------------------------
    |1.|     REGISTRASI AKUN     |
    |2.|      LOGIN AKUN         |
    |3.|        KELUAR           |
    ------------------------------
    """)

def tampilan_admin():
    print("""
    ------------------------------
    |         MENU ADMIN         |
    ------------------------------
    |1.|     TAMBAH BARANG       |
    |2.|    TAMPILKAN BARANG     |
    |3.|      UBAH BARANG        |
    |4.|     HAPUS BARANG        |
    |5.|        KELUAR           |
    ------------------------------
        """)
    
def menu_belanja_pembeli():
        print("""
    ------------------------------
    |        MENU PEMBELI        |
    ------------------------------
    |1.|      BELI BARANG        |
    |2.|   CEK SALDO E-MONEY     |
    |3.|    TOP UP E-MONEY       |
    |4.|        KELUAR           |
    ------------------------------
        """)


def menuHomepembeli():
    while True:
        menu_belanja_pembeli()
        pilihan = int(input("Masukkan nomor metode yang Anda inginkan: "))

        if pilihan == 1:
            tampilkan_barang()
            beli_barang()
        elif pilihan == 2:
            cek_saldo()
        elif pilihan == 3:
            top_up_saldo()
        elif pilihan == 4:
            print("Terima Kasih Telah Berbelanja Di SuperMarket AHA")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih metode yang tersedia.")


#function menu pembeli
def menu_pembeli() :
    tampilan_pembeli()
    while True :
        awal = input("Pilih opsi (1/2/3): ")
        if awal == "1":
            os.system('cls')
            regis()
        elif awal == "2":
            os.system('cls')
            login_pembeli()
        elif awal == "3":
            break
        else:
            print("Invalid")

def create():
    read()
    print("\n+--------TAMBAHKAN PRODUK BARU--------+")
    while True:
        try:
            id_produk = int(input("Masukan ID Produk : "))
            id_produk_str = str(id_produk)

            if id_produk == 0:
                print("> INPUT HARUS LEBIH DARI 0")
            elif id_produk in produk["ID Produk"]:
                print("> ID PRODUK SUDAH ADA, MASUKIN LAINNYA")
            elif id_produk_str.isspace():
                print("> INPUT TIDAK BOLEH KOSONG")
            elif len(id_produk_str) > 3:
                print("> ID PRODUK TIDAK BOLEH LEBIH DARI 3 ANGKA\n")
            else:
                break
                
        except ValueError:
            print("> PERHATIKAN INPUT")


    while True:
        try :
            nama = str(input("Masukan Nama Produk : "))
            if nama in produk["Nama Produk"]:
                cari_produk = produk.get("Nama Produk").index(nama)
                produk["Stok Produk"][cari_produk] = produk.get("Stok Produk")[cari_produk] +1
                read()
                while True :
                    balik = input("Apakah anda ingin ke menu home? (y/t) : ")
                    if balik == "y":
                        tampilan_admin()
                        break
                    elif balik == "t":
                        create()
                    else :
                        print("[] PILIHAN TIDAK TERSEDIA")
            elif all(x.isspace () for x in nama):
                print("> INPUT TIDAK BOLEH KOSONG")
            elif all(x.isalpha() for x in nama) and len(nama) <= 20:
                break
            elif len(nama) > 20:
                print("> NAMA PRODUK TIDAK BOLEH LEBIH DARI 20\n")
            elif all(x.isnumeric() for x in nama):
                print("> INPUT TIDAK BOLEH ANGKA\n")
            else:
                print("> INPUT YANG DIMASUKAN TIDAK SESUAI")
                print("> SILAHKAN COBA LAGI\n")
        except :
            print("[] PERHATIKAN INPUT")
            
    while True:
        try:
            harga = int(input("Masukan Harga Produk : Rp "))

            if harga < 0:
                print("HARGA TIDAK BOLEH KURANG DARI 0")
            elif harga == 0:
                print("HARGA HARUS LEBIH DARI 0")
            elif harga < 100000000 :
                break
            elif harga > 100000000 :
                print("[] Harga Produk tidak boleh lebih dari 100000000\n")
            else:
                print("[] TOLONG MASUKAN INPUT YANG BENAR")
                print("[] SILAHKAN COBA LAGI\n")
        except ValueError:
            print("[] MASUKAN ANGKA")

    while True:
        try:
            stok = int(input("Masukan Stok Produk : "))
            if stok < 0:
                print("> STOK PRODUK TIDAK BOLEH KURANG DARI 0 0")
            elif stok > 0 and stok <= 1000 :
                break
            elif stok > 1000 :
                print("> STOK PRODUK TIDAK BOLEH MELEBIHI 1000 PRODUK\n")
            else :
                print("> INPUT YANG DIMASUKAN SALAH, COBA LAGI")
        except ValueError:
            print("[] MASUKAN ANGKA")
        
    ip.append(id_produk)
    np.append(nama)
    hp.append(harga)
    sp.append(stok)
    penyimpanan()
    
    print("--- PRODUK BERHASIL DITAMBAHKAN ---\n")
    read()
    

def read():
    
    etalase_produk.clear_rows()
    for i in range(len(produk["ID Produk"])):
        etalase_produk.add_row([
            produk["ID Produk"][i],
            produk["Nama Produk"][i],
            "Rp." + str(produk["Harga Produk"][i]),
            produk["Stok Produk"][i]
        ])
    
    print(etalase_produk)

def update():
    read()
    print("\n+--------UBAH PRODUK--------+")
    while True:
        try :
            nama_produk = int(input("Masukkan ID Produk yang ingin diubah: "))
            pilih_update = produk.get("nama produk").index(nama_produk)
            break
        except : 
            print("NAMA PRODUK TIDAK DITEMUKAN")
            print("SILAHKAN COBA LAGI")

    while True :
        pilih= input("\n>> Apakah anda ingin mengubah nama produk? (y/t) : ")
        if pilih == "y":
            nama_produk_baru= input("~ Masukan nama produk baru : ")
            if nama_produk_baru in produk["Nama Produk"] :
                print("> NAMA YG DIMASUKAN SUDAH ADA")
                print("> MASUKAN NAMA PRODUK YG BERBEDA\n")
            elif all(x.isalpha() for x in nama_produk_baru) and len(nama_produk_baru) <= 20:
                produk.get("Nama Produk")[pilih_update] = nama_produk_baru
                print("--- Nama Produk berhasil diubah ---\n")
                break
            else :
                print("> NAMA PRODUK HANYA BOLEH ALPHABET")
                print("> NAMA TIDAK BOLEH LEBIH DARI 20 HURUF")

        elif pilih == "t":
            break
        else :
            print("> PILIHAN TIDAK TERSEDIA")

    while True:
        pilih1 = input("\n>> Apakah anda ingin mengubah harga produk? (y/t) : ")
        if pilih1 == "y":
            while True :
                try :
                    harga_produk_baru = int(input("~ Masukkan harga produk baru : Rp. "))
                    if harga_produk_baru < 0:
                        print("HARGA TIDAK BOLEH KURANG DARI 0")
                    elif harga_produk_baru == 0:
                        print("HARGA HARUS LEBIH DARI 0")
                    elif harga_produk_baru > 0 and harga_produk_baru < 100000000:
                        produk.get("Harga Produk")[pilih_update] = harga_produk_baru
                        print("--- Harga Produk berhasil diubah ---\n")
                        break
                    else :
                        print("HARGA PRODUK TIDAK BISA LEBIH DARI 100000000")
                except :
                    print("PERHATIKAN INPUTAN")
            break
        elif pilih1 == "t":
            break
        else :
            print("PILIHAN TIDAK TERSEDIA")

def delete():
        hapus = input("Masukkan kode produk yang ingin dihapus: ")
        hapus = int(hapus)
        if hapus == "":
            print("Input tidak boleh kosong")
        elif hapus in etalase_produk:
            nama_menu_hapus = etalase_produk[hapus]['nama']
            del etalase_produk[hapus]
            print(f"Produk {nama_menu_hapus} telah dihapus dari menu.")
        elif hapus not in etalase_produk:
            print("Produk tidak ditemukan")
        else:
            print("Kode produk tidak valid.")

def menuadmin():
    print("Menu admin")

def hitung_total_barang(pembelian_barang):
    total = 0
    for item in pembelian_barang:
        total += produk[item]["harga"]
    return total

def tampilkan_barang():
    tabel_barang = PrettyTable()
    tabel_barang.field_names = ["ID Produk", "Nama Produk", "Harga Produk", "Stok Produk"]
    for no, value in produk.items():
        if value["harga"] > 0:
            tabel_barang.add_row([no, value["nama"], value["harga"], value["stok"]])
    print("===============================")
    print("Barang yang tersedia di Supermarket AHA")
    print("===============================")
    print(tabel_barang)
    print("|-----------------------------|")

def beli_barang():
    global saldo
    pembelian_barang = []
    while True:
        try:
            nomor_produk = int(input("Pilih nomor produk (0 untuk selesai): "))
            if nomor_produk == 0:
                break
            if nomor_produk in produk and produk[nomor_produk]["stok"] > 0:
                if produk[nomor_produk]["harga"] <= saldo:
                    pembelian_barang.append(nomor_produk)
                    produk[nomor_produk]["stok"] -= 1
                    saldo -= produk[nomor_produk]["harga"]
                    print(f"{produk[nomor_produk]['nama']} berhasil ditambahkan ke keranjang.")
                else:
                    print("Saldo Anda tidak mencukupi untuk membeli produk ini.")
            else:
                print("Produk tidak tersedia atau stok habis.")
        except ValueError:
            print("Masukan tidak valid. Silakan masukkan nomor produk.")
    total_harga = hitung_total_barang(pembelian_barang)
    print(f"Total Harga: {total_harga}")

def cek_saldo():
    print(f"Sisa saldo Anda adalah: {saldo}")

def top_up_saldo():
    global saldo
    top_up = int(input("Masukkan jumlah saldo yang ingin Anda top up: "))
    saldo += top_up
    print(f"Saldo Anda sekarang adalah: {saldo}")

    
#main program
while True:
    try :
        print("""
=====================================
          SELAMAT DATANG DI 
              AHA MART
=====================================""")
        tampilan_awal()
        pilihan = input("Masukkan pilihan (1/2/3): ")
        os.system("cls")
        
        if pilihan == "1":
            login_admin()
        elif pilihan == "2" :
            menu_pembeli()
        elif pilihan == "3":
            
            print("""
=======================================
        PROGRAM TELAH SELESAI
Terima kasih! dan sampai jumpa :)
=======================================
    """)
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")
    except ValueError :
            print("Input harus berupa angka\n")
