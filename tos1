import json
import os

FILE = "data_tugas.json"

def load_data():
    if not os.path.exists(FILE):
        return[]
    with open(FILE, "r") as file:
    return json.load(file)

def save_data(data):
    with open(FILE, "w") as file:
        jso.dump(data,file,indent=4)

def tambah_tugas(data):
    nama = imput("Nama Tugas:")


tugas = { "nama": nama,
         }

data.append(tugas)
save_data(data)
print("Tugas berhasil ditambahkan!")

def tampilkan_tugas(data):
    if not data:
        print("tidak ada tugas.")
        return
    
print("\Daftar Tugas:")
for i, t in enumerate(data,1):
    print(f"{i}. {t['nama']}")

def hapus_tugas(data):
    tampilkan_tugas(data)
    try:
        index = int(input("Pilih nomor tugas yang ingin dihapus:"))
        data.pop(index - 1)
        save_data(data)
        print("tugas dihapus!")
    except:
        print("input salah!")

def menu():
    data = load_data()

while True:
    print("\n=== SISTEM INFORMASI TUGAS MAHASISWA ===")
    print("1. Tambah tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugs")
    print("4. Keluar")

    pilih = input("Pilih menu:")

    if pilih == "1":
        tambah_tugas(data)
    elif pilih == "2":
        tampilkan_tugas(data)
    elif pilih == "3":
        hapus_tugas(data)
    elif pilih == "4":
        break
    else:
        print("Pilihan tidak valid!")

menu()
