print("# Program Menghitung Luas dan Volume Limas")
print("Nama: Nasywa Adila Rahma")
print("Nim: 2310433022")
print("SHIFT-2")
print()

import math 
def hitung_limas(sisi_alas,tinggi_limas):
    luas_alas = sisi_alas ** 2
    luas_permukaan = luas_alas + 4 * sisi_alas * tinggi_segitiga / 2
    volume = (luas_alas * tinggi_limas) / 3
    return luas_permukaan, volume
sisi_alas = float(input("Panjang Sisi alas: "))
tinggi_limas = float(input("tinggi limas: "))
tinggi_segitiga = float(input("tinggi segitiga: "))
luas_permukaan, volume = hitung_limas(sisi_alas,tinggi_limas)
print("Luas Permukaan Limas segi Empat:", luas_permukaan)
print("Volume Limas segi Empat:", volume)
