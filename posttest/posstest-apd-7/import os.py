import os
import time

data_akun = {
    "admin": {
        "password": "admin123",
        "peran": "admin"
    },
    "pembeli": {
        "password": "123",
        "peran": "user"
    }
}

data_booking = {
    1: {
        "nama": "Budi",
        "lapangan": "Lapangan A (Sintetis)",
        "durasi": 2,
        "total": 200000
    },
    2: {
        "nama": "Andi",
        "lapangan": "Lapangan B (Vinyil)",
        "durasi": 1,
        "total": 120000
    }
}

nomor_booking_berikutnya = 3
peran_login = ""
pengguna_aktif = ""

def tampilkan_judul(judul):
    print("=" * 45)
    print(judul.center(45))
    print("=" * 45)

def input_angka(pesan):
    while True:
        try:
            angka = int(input(pesan))
            return angka
        except ValueError:
            print("Input harus berupa angka!")

def tampilkan_semua_booking():
    tampilkan_judul("DATA BOOKING LAPANGAN FUTSAL")

    if not data_booking:
        print("Belum ada data booking.")
    else:
        for nomor in data_booking:
            print(f"\nNomor Booking : {nomor}")
            print(f"Nama          : {data_booking[nomor]['nama']}")
            print(f"Lapangan      : {data_booking[nomor]['lapangan']}")
            print(f"Durasi        : {data_booking[nomor]['durasi']} jam")
            print(f"Total         : Rp{data_booking[nomor]['total']:,}")

def pilih_lapangan():
    print("\nPilihan Lapangan:")
    print("1. Lapangan A (Sintetis) - Rp100.000/jam")
    print("2. Lapangan B (Vinyil) - Rp120.000/jam")

    pilihan_lapangan = input("Pilih lapangan (1-2): ")

    if pilihan_lapangan == "1":
        lapangan = "Lapangan A (Sintetis)"
        harga = 100000
    elif pilihan_lapangan == "2":
        lapangan = "Lapangan B (Vinyil)"
        harga = 120000
    else:
        print("Pilihan lapangan tidak valid!")
        return pilih_lapangan()

    return lapangan, harga

def input_menu_awal():
    pilihan = input("\nPilih menu (1-3): ")

    if pilihan == "1" or pilihan == "2" or pilihan == "3":
        return pilihan
    else:
        os.system("cls" if os.name == "nt" else "clear")
        tampilkan_judul("SISTEM BOOKING LAPANGAN FUTSAL")
        print("1. Login")
        print("2. Registrasi (Buat Akun Untuk User)")
        print("3. Keluar")
        print("\nPilihan tidak valid.")
        input("Enter untuk kembali...")
        return input_menu_awal()

def input_menu_admin():
    pilihan = input("Pilih menu (1-5): ")

    if (pilihan == "1" or pilihan == "2" or
        pilihan == "3" or pilihan == "4" or
        pilihan == "5"):
        return pilihan
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("Pilihan tidak valid!")
        return input_menu_admin()

def input_menu_user():
    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1" or pilihan == "2" or pilihan == "3":
        return pilihan
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("Pilihan tidak valid!")
        return input_menu_user()

def login():
    global peran_login, pengguna_aktif

    tampilkan_judul("LOGIN")

    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in data_akun:
        if data_akun[username]["password"] == password:
            pengguna_aktif = username
            peran_login = data_akun[username]["peran"]
            print("Login berhasil!")
            return True
        else:
            print("Password salah!")
            input("Enter untuk kembali...")
    else:
        print("Username tidak ditemukan!")
        input("Enter untuk kembali...")
    return False

def registrasi():
    tampilkan_judul("REGISTRASI")

    username = input("Buat username: ")

    if username in data_akun:
        print("Username sudah digunakan!")
    else:
        password = input("Buat password: ")

        data_akun[username] = {
            "password": password,
            "peran": "user"
        }
        print("Registrasi berhasil!")

def tambah_booking():
    global nomor_booking_berikutnya

    tampilkan_judul("TAMBAH DATA BOOKING")

    nama = input("Masukkan nama penyewa: ")
    if nama == "":
        print("Nama penyewa tidak boleh kosong")
        return
    lapangan, harga = pilih_lapangan()

    durasi = input_angka("Masukkan durasi sewa (jam): ")

    if durasi <= 0:
        print("Durasi harus lebih dari 0 jam!")
    else:
        total = harga * durasi

        data_booking[nomor_booking_berikutnya] = {
            "nama": nama,
            "lapangan": lapangan,
            "durasi": durasi,
            "total": total
        }

        print(f"\nBooking berhasil ditambahkan!")
        print(f"Nomor Booking: {nomor_booking_berikutnya}")
        print(f"Total biaya: Rp{total:,}")

        nomor_booking_berikutnya += 1

def ubah_booking():
    tampilkan_judul("UBAH DATA BOOKING")

    if not data_booking:
        print("Tidak ada data untuk diubah.")
    else:
        tampilkan_semua_booking()

        nomor = input_angka("\nMasukkan nomor booking yang ingin diubah: ")

        if nomor in data_booking:
            print("\nMasukkan data booking yang baru.")

            nama = input("Nama penyewa baru: ")
            lapangan, harga = pilih_lapangan()
            durasi = input_angka("Durasi sewa baru (jam): ")

            if durasi <= 0:
                print("Durasi harus lebih dari 0 jam!")
            else:
                data_booking[nomor]["nama"] = nama
                data_booking[nomor]["lapangan"] = lapangan
                data_booking[nomor]["durasi"] = durasi
                data_booking[nomor]["total"] = harga * durasi

                print("Data booking berhasil diubah!")
        else:
            print("Nomor booking tidak ditemukan.")

def hapus_booking():
    tampilkan_judul("HAPUS DATA BOOKING")

    if not data_booking:
        print("Tidak ada data untuk dihapus.")
    else:
        tampilkan_semua_booking()

        nomor = input_angka("\nMasukkan nomor booking yang ingin dihapus: ")

        if nomor in data_booking:
            del data_booking[nomor]
            print("Data booking berhasil dihapus!")
        else:
            print("Nomor booking tidak ditemukan.")

def menu_admin():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        tampilkan_judul("MENU ADMIN")
        print("1. Lihat Data Booking")
        print("2. Tambah Booking")
        print("3. Ubah Data Booking")
        print("4. Hapus Data Booking")
        print("5. Logout")

        pilihan_admin = input_menu_admin()

        if pilihan_admin == "1":
            os.system("cls" if os.name == "nt" else "clear")
            tampilkan_semua_booking()
            input("\nTekan Enter untuk kembali...")

        elif pilihan_admin == "2":
            os.system("cls" if os.name == "nt" else "clear")
            tambah_booking()
            input("\nTekan Enter untuk kembali...")

        elif pilihan_admin == "3":
            os.system("cls" if os.name == "nt" else "clear")
            ubah_booking()
            input("\nTekan Enter untuk kembali...")

        elif pilihan_admin == "4":
            os.system("cls" if os.name == "nt" else "clear")
            hapus_booking()
            input("\nTekan Enter untuk kembali...")

        elif pilihan_admin == "5":
            print("Logout berhasil!")
            time.sleep(3)
            break

def menu_user():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        tampilkan_judul("MENU PENGGUNA")
        print("1. Lihat Data Booking")
        print("2. Booking Lapangan")
        print("3. Logout")

        pilihan_user = input_menu_user()

        if pilihan_user == "1":
            os.system("cls" if os.name == "nt" else "clear")
            tampilkan_semua_booking()
            input("\nTekan Enter untuk kembali...")

        elif pilihan_user == "2":
            os.system("cls" if os.name == "nt" else "clear")
            tambah_booking()
            input("\nTekan Enter untuk kembali...")

        elif pilihan_user == "3":
            print("Logout berhasil!")
            time.sleep(1)
            break

while True:
    os.system("cls" if os.name == "nt" else "clear")
    tampilkan_judul("SISTEM BOOKING LAPANGAN FUTSAL")
    print("1. Login")
    print("2. Registrasi")
    print("3. Keluar")

    pilihan_awal = input_menu_awal()

    if pilihan_awal == "1":
        os.system("cls" if os.name == "nt" else "clear")
        if login():
            if peran_login == "admin":
                menu_admin()
            elif peran_login == "user":
                menu_user()

            pengguna_aktif = ""
            peran_login = ""

    elif pilihan_awal == "2":
        os.system("cls" if os.name == "nt" else "clear")
        registrasi()
        input("\nTekan Enter untuk kembali...")

    elif pilihan_awal == "3":
        print("Terima kasih telah menggunakan program!")
        break