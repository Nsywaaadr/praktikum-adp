print("Nama: Nasywa Adila Rahma")
print("Nim: 2310433022")
print("SHIFT 2")
print("-----------------------------------")
print("Bus PT. ANS lintas sumatera")
harga_tiket ={
    'Medan': 365000,
    'Padang': 250000,
    'Bengkulu': 285000,
    'Jambi': 265000,
    'Pekanbaru': 150000,
    'Lampung': 453000,
}
print(f"Harga Tiket {harga_tiket}")
tujuan_dipesan = input("Tujuan yang dipesan: ")
print('----------------------------------------------')
print("kelas (biaya tambahan)")
economi_class = 10000
bisnis_class = 20000
first_class = 30000
print(f"Economi Class: {economi_class}")
print(f'Bisnis Class: {bisnis_class}')
print(f'First Class: {first_class}')
kelas_dipesan = input("kelas yang diambil: ")
if kelas_dipesan == 'Ekonomi':
    harga_kelas = economi_class
elif kelas_dipesan == 'Bisnis':
    harga_kelas = bisnis_class
elif kelas_dipesan == "First":
    harga_kelas = first_class
else:
    print("kelas bus yang dipesan tidak valid")
    exit()
if tujuan_dipesan not in harga_tiket:
    print("Tujuan bus yang dipesan tidak valid.")
    exit()
jumlah_tiket = int(input(f"Masukkan jumlah tiket yang dipesan untuk tujuan {tujuan_dipesan}: "))
print('-------------------------------------------------------------------')
total_harga = jumlah_tiket * harga_tiket[tujuan_dipesan]
total_harga += jumlah_tiket * harga_kelas

if jumlah_tiket <5:
    diskon = harga_tiket[tujuan_dipesan] * 0.05
else: 
    if jumlah_tiket >5:
        diskon = harga_tiket[tujuan_dipesan] * 0.1
    else:
        diskon = 0

total_harga_setelah_diskon = total_harga - diskon
print(f'Tujuan: {tujuan_dipesan}')
print(f'Kelas: {kelas_dipesan}')
print(f'Jumlah tiket: {jumlah_tiket}')
print(f'Total harga tiket untuk {jumlah_tiket} tiket ke {tujuan_dipesan} dengan kelas {kelas_dipesan} adalah Rp. {total_harga}')
print(f'diskon yang diberikan adalah Rp. {diskon}')
print(f'total harga tiket setelah diskon adalah Rp. {total_harga_setelah_diskon}')