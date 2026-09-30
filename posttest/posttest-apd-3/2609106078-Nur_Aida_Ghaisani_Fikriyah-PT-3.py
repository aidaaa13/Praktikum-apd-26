nama = "aida"
NIM = 78

print("-------- Selamat Datang ----------")
data_login = input("Silahkan Masukkan Username: ")
nim = int(input("Silahkan Masukkan Password: "))
if data_login == nama or nim == NIM:
    print("\n-------- Selamat login berhasil --------")
    print("\n----------- Proses Top Up --------------")
    id_player_input = int(input("Masukkan id player anda: "))
    print("Id Player Terdeteksi")
    print("--------------------------------------------------------")
    print("pilihan game : Genshin Impact, Minecraft, Mobile Legends")
    nama_game = input("silahkan pilih game anda: ")

    if nama_game == "Genshin Impact":
            status = True
    elif nama_game == "Minecraft":
            status = True
    elif nama_game == "Mobile Legends":
            status = True
    else:
            print("Nama Game Tidak Valid")

    if status == True:  
        print("-------------------------------------------------")
        print("pilihan kategori top up: Kecil, Menengah, Besar")
        kategori_top_up = input("pilih kategori top up: ")
        if kategori_top_up == "Kecil":
            harga_dasar = 15000
            kategori_valid = True
        elif kategori_top_up == "Menengah":
            harga_dasar = 50000
            kategori_valid = True
        elif kategori_top_up == "Besar":
            harga_dasar = 150000
            kategori_valid = True
        else:
            harga_dasar = 0
            print("Kategori Top Up Tidak Valid")
        if kategori_valid == True:
            print("---------------------------------------------")
            print("pilihan metode pembayaran : Pulsa, E-wallet")
            metode_pembayaran = input("pilih metode pembayaran: ")
            biaya = 2500 if metode_pembayaran == "Pulsa" else (500 if metode_pembayaran == "E-wallet" else 0) 
            total_bayar = harga_dasar + biaya
            print("\nTotal Bayarnya Adalah: Rp",total_bayar)
            uang_dibayar = int(input("Masukkan Nominal Uang Yang Dibayarkan: "))
            if uang_dibayar < total_bayar:
                print("\nTransaksi Gagal Saldo Anda Tidak Mencukupi")
            else:
                print("Transaksinya Berhasil, Have Fun Yaa!")
            kembalian =  uang_dibayar - total_bayar

            print("\n=========== Struk Pembelian ============")
            print("Id Player               :",id_player_input)
            print("Nama Game               :",nama_game)
            print("Kategori Top Up         :",kategori_top_up)
            print("Metode Pembayaran       :",metode_pembayaran)
            print("Harga Dasar             :",harga_dasar)
            print("Biaya Admin             :",biaya)
            print("Total Bayar             :",total_bayar)
            print("------------------------------------------")
            print("Uang Tunai              :",uang_dibayar)
            print("Kembalian               :",kembalian)
else:   
    print("login gagal")