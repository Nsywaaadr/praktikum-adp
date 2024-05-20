def baca_data():
    try:
        with open("buku.txt", "r") as file:
            data = file.readlines()
            buku = {}
            for line in data:
                judul, penulis, penerbit, tahun = line.strip().split(",")
                buku[judul] = {"penulis": penulis, "penerbit": penerbit, "tahun": tahun}
            return buku
    except FileNotFoundError:
        return {}

# Menyimpan data buku ke file
def simpan_data(buku):
    with open("buku.txt", "w") as file:
        for judul, data in buku.items():
            file.write(f"{judul},{data['penulis']},{data['penerbit']},{data['tahun']}\n")
def tampilkan_data(buku):
    print("Data Buku Favorit:")
    for judul, data in buku.items():
        print(f"Judul: {judul}")
        print(f"Penulis: {data['penulis']}")
        print(f"Penerbit: {data['penerbit']}")
        print(f"Tahun Terbit: {data['tahun']}")
        print()

# Menghapus data buku
def hapus_data(buku, judul):
    if judul in buku:
        del buku[judul]
        print(f"Data buku '{judul}' telah dihapus.")
    else:
        print(f"Data buku '{judul}' tidak ditemukan.")

def menu():
    buku = baca_data()
    while True:
        print("Menu:")
        print("1. Tambah Buku")
        print("2. Hapus Buku")
        print("3. Tampilkan Buku")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            judul = input("Masukkan judul buku: ")
            penulis = input("Masukkan nama penulis: ")
            penerbit = input("Masukkan nama penerbit: ")
            tahun = input("Masukkan tahun terbit: ")
            buku[judul] = {"penulis": penulis, "penerbit": penerbit, "tahun": tahun}
            simpan_data(buku)
        elif pilihan == "2":
            judul = input("Masukkan judul buku yang ingin dihapus: ")
            hapus_data(buku, judul)
            simpan_data(buku)
        elif pilihan == "3":
            tampilkan_data(buku)
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan program
menu()