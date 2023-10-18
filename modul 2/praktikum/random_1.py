# Inisialisasi database buku yang tersedia
database_buku = []

# Inisialisasi database peminjaman buku
database_peminjaman = []

# Inisialisasi data admin
admin_username = "admin"
admin_password = "admin123"  # Ganti dengan password yang lebih aman

# Fungsi untuk menambahkan buku
def tambah_buku():
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan penulis buku: ")
    buku = {"ID": len(database_buku), "Judul": judul, "Penulis": penulis, "Status": "Tersedia"}
    database_buku.append(buku)
    print("Buku '{}' oleh {} telah ditambahkan.".format(judul, penulis))

# Fungsi untuk mencari buku berdasarkan ID
def cari_buku_by_id(id_buku):
    buku = next((buku for buku in database_buku if buku["ID"] == id_buku), None)
    return buku

# Fungsi untuk mengedit buku berdasarkan ID
def edit_buku_by_id(id_buku, judul_baru, penulis_baru):
    buku = cari_buku_by_id(id_buku)
    if buku:
        buku["Judul"] = judul_baru
        buku["Penulis"] = penulis_baru
        print("Data buku berhasil diperbarui.")
    else:
        print("Buku dengan ID {} tidak ditemukan.".format(id_buku))

# Fungsi untuk mencari buku berdasarkan judul atau penulis
def cari_buku():
    keyword = input("Masukkan kata kunci (judul/penulis): ").lower()
    found_books = [buku for buku in database_buku if keyword in buku["Judul"].lower() or keyword in buku["Penulis"].lower()]
    if found_books:
        print("\nHasil Pencarian:")
        for buku in found_books:
            print("ID: {}, Judul: {}, Penulis: {}".format(buku["ID"], buku["Judul"], buku["Penulis"]))
    else:
        print("Buku tidak ditemukan.")

# Fungsi untuk menampilkan buku yang tersedia
def tampilkan_buku_tersedia():
    print("\nBuku Tersedia:")
    available_books = [buku for buku in database_buku if buku["Status"] == "Tersedia"]
    for buku in available_books:
        print("ID: {}, Judul: {}, Penulis: {}".format(buku["ID"], buku["Judul"], buku["Penulis"]))

# Fungsi untuk pinjam buku
def pinjam_buku(id_buku, user_id):
    buku = next((buku for buku in database_buku if buku["ID"] == id_buku and buku["Status"] == "Tersedia"), None)
    if buku:
        buku["Status"] = "Dipinjam"
        peminjaman = {"ID": len(database_peminjaman), "ID Buku": id_buku, "ID User": user_id}
        database_peminjaman.append(peminjaman)
        print("Buku '{}' berhasil dipinjam.".format(buku["Judul"]))
    else:
        print("Buku tidak tersedia atau ID Buku tidak valid.")

# Fungsi untuk mengembalikan buku
def kembalikan_buku(id_buku, user_id):
    peminjaman = next((peminjaman for peminjaman in database_peminjaman if peminjaman["ID Buku"] == id_buku and peminjaman["ID User"] == user_id), None)
    if peminjaman:
        buku = next((buku for buku in database_buku if buku["ID"] == id_buku), None)
        if buku:
            buku["Status"] = "Tersedia"
            database_peminjaman.remove(peminjaman)
            print("Buku '{}' berhasil dikembalikan.".format(buku["Judul"]))
        else:
            print("Buku tidak ditemukan.")
    else:
        print("Buku tidak dipinjam oleh user dengan ID tersebut.")

# Program utama
while True:
    print("\nSelamat datang di Sistem Peminjaman Buku")
    print("1. Login sebagai Admin")
    print("2. Login sebagai User")
    print("3. Cari Buku")
    print("4. Keluar")

    pilihan = input("Pilih opsi: ")

    if pilihan == "1":
        print("\nLogin sebagai Admin")
        username = input("Username: ")
        password = input("Password: ")

        if username == admin_username and password == admin_password:
            while True:
                print("\nMenu Admin:")
                print("1. Tambah Buku")
                print("2. Lihat Buku Tersedia")
                print("3. Edit Buku")
                print("4. Keluar")

                admin_pilihan = input("Pilih opsi: ")

                if admin_pilihan == "1":
                    tambah_buku()
                elif admin_pilihan == "2":
                    tampilkan_buku_tersedia()
                elif admin_pilihan == "3":
                    tampilkan_buku_tersedia()
                    id_buku_edit = int(input("Masukkan ID Buku yang ingin diedit: "))
                    judul_baru = input("Masukkan judul baru: ")
                    penulis_baru = input("Masukkan penulis baru: ")
                    edit_buku_by_id(id_buku_edit, judul_baru, penulis_baru)
                elif admin_pilihan == "4":
                    break
                else:
                    print("Pilihan tidak valid.")
        else:
            print("Username atau password admin salah.")

    elif pilihan == "2":
        print("\nLogin sebagai User")
        user_id = input("Masukkan ID User: ")

        while True:
            print("\nMenu User:")
            print("1. Pinjam Buku")
            print("2. Kembalikan Buku")
            print("3. Keluar")

            user_pilihan = input("Pilih opsi: ")

            if user_pilihan == "1":
                tampilkan_buku_tersedia()
                id_buku_pinjam = int(input("Masukkan ID Buku yang ingin dipinjam: "))
                pinjam_buku(id_buku_pinjam, user_id)
            elif user_pilihan == "2":
                tampilkan_buku_tersedia()
                id_buku_kembali = int(input("Masukkan ID Buku yang ingin dikembalikan: "))
                kembalikan_buku(id_buku_kembali, user_id)
            elif user_pilihan == "3":
                break
            else:
                print("Pilihan tidak valid.")

    elif pilihan == "3":
        cari_buku()

    elif pilihan == "4":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")
