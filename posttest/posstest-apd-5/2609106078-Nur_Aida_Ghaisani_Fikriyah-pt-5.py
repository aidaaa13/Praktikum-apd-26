import os

data_akun = [
    ["admin", "admin123", "admin"],
    ["pembeli", "123", "user"]
]

data_booking = [
    ["Budi", "Lapangan A (Sintetis)", "2 Jam", "Rp 200.000"],
    ["Andi", "Lapangan B (Vinyil)", "1 Jam", "Rp 120.000"]
]

peran_login = ""
pengguna_aktif = ""

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 45)
    print("    SISTEM BOOKING LAPANGAN FUTSAL    ")
    print("=" * 45)
    print("1. Login")
    print("2. Register (Buat Akun Untuk User)")
    print("3. Keluar Program")
    print("=" * 45)
    
    pilihan_awal = input("Pilih menu (1-3): ")

    if pilihan_awal == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 45)
        print("              MENU LOGIN              ")
        print("=" * 45)
        username_input = input("Masukkan Username : ")
        password_input = input("Masukkan Password : ")

        berhasil_login = False
        for akun in data_akun:
            if akun[0] == username_input and akun[1] == password_input:
                berhasil_login = True
                pengguna_aktif = akun[0]
                peran_login = akun[2]
                break

        if berhasil_login:
            print(f"\nLogin Berhasil! Selamat datang, {pengguna_aktif}.")
            input("Tekan Enter untuk melanjutkan")

            if peran_login == "admin":
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=" * 45)
                    print("      MENU ADMIN      ")
                    print("=" * 45)
                    print("1. Lihat Semua Data Booking (Read)")
                    print("2. Tambah Data Booking (Create)")
                    print("3. Ubah Data Booking (Update)")
                    print("4. Hapus Data Booking (Delete)")
                    print("5. Logout")
                    print("=" * 45)
                    pilihan_admin = input("Pilih menu (1-5): ")

                    if pilihan_admin == "1":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=" * 60)
                        print("               DAFTAR BOOKING FUTSAL                ")
                        print("=" * 60)
                        if len(data_booking) == 0:
                            print("Belum ada data booking lapangan.")
                        else:
                            for id in range(len(data_booking)):
                                print(f"{id + 1}. Pemesan : {data_booking[id][0]}")
                                print(f"   Lapangan: {data_booking[id][1]}")
                                print(f"   Durasi  : {data_booking[id][2]}")
                                print(f"   Harga   : {data_booking[id][3]}")
                                print("-" * 60)
                        input("\nTekan Enter untuk kembali")

                    elif pilihan_admin == "2":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=" * 45)
                        print("         TAMBAH DATA BOOKING BARU          ")
                        print("=" * 45)
                        nama_pemesan = input("Masukkan Nama Pemesan : ")
                        
                        print("\nPilih Lapangan:")
                        print("1. Lapangan A (Sintetis) - Rp 100.000/jam")
                        print("2. Lapangan B (Vinyil)   - Rp 120.000/jam")
                        pilih_lap = input("Pilih (1/2): ")
                        
                        lapangan = ""
                        harga_per_jam = 0
                        if pilih_lap == "1":
                            lapangan = "Lapangan A (Sintetis)"
                            harga_per_jam = 100000
                        elif pilih_lap == "2":
                            lapangan = "Lapangan B (Vinyil)"
                            harga_per_jam = 120000
                        else:
                            print("Pilihan lapangan tidak valid!")
                            input("Tekan Enter untuk kembali")
                            continue

                        jam_input = input("Masukkan Durasi Main (Jam, angka saja): ")
                        if int(jam_input) > 0:
                            durasi = int(jam_input)
                            total_harga = durasi * harga_per_jam
                            
                            data_booking.append([nama_pemesan, lapangan, f"{durasi} Jam", f"Rp {total_harga:}"])
                            print("\nData Booking Berhasil Ditambahkan!")
                        else:
                            print("\nInput durasi jam harus berupa angka!")
                        input("Tekan Enter untuk kembali")

                    elif pilihan_admin == "3":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=" * 45)
                        print("            UBAH DATA BOOKING              ")
                        print("=" * 45)
                        if len(data_booking) == 0:
                            print("Tidak ada data untuk diubah.")
                        else:
                            for id in range(len(data_booking)):
                                print(f"{id + 1}. {data_booking[id][0]} - {data_booking[id][1]} - ({data_booking[id][2]})")
                            
                            pilih_id = input("\nMasukkan nomor data yang ingin diubah: ")
                            id_valid = True

                            if pilih_id == "":  
                                id_valid = False
                                print("\nInput tidak boleh kosong")
                            else:
                                for karakter in pilih_id:
                                    if karakter not in "0123456789":
                                        id_valid = False
                                        break  
                            if id_valid: 
                                nomor = int(pilih_id) - 1 
                                if 0 <= nomor < len(data_booking):
                                    print(f"\nMengubah Data Milik: {data_booking[nomor][0]}")
                                    nama_baru = input("Nama Pemesan Baru: ")
                                    
                                    print("\nPilih Lapangan Baru:")
                                    print("1. Lapangan A (Sintetis) - Rp 100.000/jam")
                                    print("2. Lapangan B (Vinyil)   - Rp 120.000/jam")
                                    pilih_lap = input("Pilih (1/2): ")
                                    
                                    if pilih_lap == "1":
                                        lap_baru = "Lapangan A (Sintetis)"
                                        harga_per_jam = 100000
                                    elif pilih_lap == "2":
                                        lap_baru = "Lapangan B (Vinyil)"
                                        harga_per_jam = 120000
                                    else:
                                        print("Pilihan lapangan tidak valid!")
                                        input("Tekan Enter")
                                        continue

                                    jam_baru = input("Durasi Baru (Jam, angka saja): ")
                                    jam_valid = True
                                    if jam_baru == "":  
                                        jam_valid = False
                                    else:
                                        for karakter in jam_baru:
                                            if karakter not in "0123456789":
                                                jam_valid = False
                                                break

                                    if jam_valid: 
                                        durasi = int(jam_baru)
                                        if durasi > 0:
                                            total = durasi * harga_per_jam

                                        data_booking[nomor][0] = nama_baru
                                        data_booking[nomor][1] = lap_baru
                                        data_booking[nomor][2] = f"{durasi} Jam"
                                        data_booking[nomor][3] = f"Rp {total: }"

                                        print("\nData berhasil diperbarui!")
                                    else:
                                        print("\nDurasi jam tidak valid, harus lebih dari 0!")
                                else:
                                    print("\nNomor data tidak ditemukan!")
                            else:
                                print("\nMasukkan nomor berupa angka!")
                        input("Tekan Enter untuk kembali")

                    elif pilihan_admin == "4":
                        os.system ('cls' if os.name == 'nt' else 'clear')
                        print("=" * 45)
                        print("            HAPUS DATA BOOKING             ")
                        print("=" * 45)
                        if len(data_booking) == 0:
                            print("Tidak ada data untuk dihapus.")
                        else:
                            for id in range(len(data_booking)):
                                print(f"{id + 1}. {data_booking[id][0]} - {data_booking[id][1]} - ({data_booking[id][2]})")
                            
                            pilih_id = input("\nMasukkan nomor data yang ingin dihapus: ")
                            id_valid = True

                            if pilih_id == "":  
                                id_valid = False
                                print("\nInput tidak boleh kosong")
                            else:
                                for karakter in pilih_id:
                                    if karakter not in "0123456789":
                                        id_valid = False
                                        break  
                            if id_valid: 
                                nomor = int(pilih_id) - 1
                                if 0 <= nomor < len(data_booking):
                                    data_dihapus = data_booking.pop(nomor)
                                    print(f"\nData booking atas nama '{data_dihapus[0]}' berhasil dihapus!")
                                else:
                                    print("\nNomor data tidak ditemukan!")
                            else:
                                print("\nMasukkan nomor berupa angka!")
                        input("Tekan Enter untuk kembali")

                    elif pilihan_admin == "5":
                        break
                    else:
                        print("Pilihan tidak valid!")
                        input("Tekan Enter")

            elif peran_login == "user":
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=" * 45)
                    print("       MENU USER        ")
                    print("=" * 45)
                    print("1. Lihat Jadwal Booking Futsal (Read)")
                    print("2. Lakukan Booking Lapangan (Create)")
                    print("3. Logout")
                    print("=" * 45)
                    pilihan_user = input("Pilih menu (1-3): ")

                    if pilihan_user == "1":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=" * 60)
                        print("               DAFTAR BOOKING FUTSAL                ")
                        print("=" * 60)
                        if len(data_booking) == 0:
                            print("Belum ada data booking lapangan.")
                        else:
                            for id in range(len(data_booking)):
                                print(f"{id + 1}. Pemesan : {data_booking[id][0]}")
                                print(f"   Lapangan: {data_booking[id][1]}")
                                print(f"   Durasi  : {data_booking[id][2]}")
                                print(f"   Harga   : {data_booking[id][3]}")
                                print("-" * 60)
                        input("\nTekan Enter untuk kembali")

                    elif pilihan_user == "2":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=" * 45)
                        print("            FORM BOOKING LAPANGAN          ")
                        print("=" * 45)
                        print(f"Nama Pemesan: {pengguna_aktif}")
                        
                        print("\nPilih Lapangan:")
                        print("1. Lapangan A (Sintetis) - Rp 100.000/jam")
                        print("2. Lapangan B (Vinyil)   - Rp 120.000/jam")
                        pilih_lap = input("Pilih (1/2): ")
                        
                        lapangan = ""
                        harga_per_jam = 0
                        if pilih_lap == "1":
                            lapangan = "Lapangan A (Sintetis)"
                            harga_per_jam = 100000
                        elif pilih_lap == "2":
                            lapangan = "Lapangan B (Vinyil)"
                            harga_per_jam = 120000
                        else:
                            print("Pilihan lapangan tidak valid!")
                            input("Tekan Enter untuk kembali")
                            continue

                        jam_input = input("Masukkan Durasi Main (Jam, angka saja): ")
                        if int(jam_input) > 0:
                            durasi = int(jam_input)
                            total_harga = durasi * harga_per_jam

                            data_booking.append([pengguna_aktif, lapangan, f"{durasi} Jam", f"Rp {total_harga:}"])
                            print("\nBooking Berhasil Dibuat!")
                        else:
                            print("\nInput durasi jam harus berupa angka!")
                        input("Tekan Enter untuk kembali")

                    elif pilihan_user == "3":
                        break
                    else:
                        print("Pilihan tidak valid!")
                        input("Tekan Enter")

        else:
            print("\nUsername atau Password salah!")
            input("Tekan Enter untuk mencoba lagi")

    elif pilihan_awal == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 45)
        print("              REGISTER USER              ")
        print("=" * 45)
        reg_user = input("Masukkan Username Baru : ")
        reg_pass = input("Masukkan Password Baru : ")

        sudah_ada = False
        for akun in data_akun:
            if akun[0] == reg_user:
                sudah_ada = True
                break

        if sudah_ada:
            print("\nUsername sudah digunakan! Silakan gunakan username lain.")
        elif reg_user == "" or reg_pass == "":
            print("\nUsername dan Password tidak boleh kosong!")
        else:
            data_akun.append([reg_user, reg_pass, "user"])
            print("\nRegistrasi berhasil! Silakan login.")
        input("Tekan Enter untuk kembali")

    elif pilihan_awal == "3":
        print("\nTerima kasih telah menggunakan sistem ini!")
        break
    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk mencoba lagi")