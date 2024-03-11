print("# Menghitung IP Semester 1 #")
print("Nama: Nasywa Adila Rahma ")
print("Nim: 2310433022")
print("SHIFT-2")
print()

nilai_matkul =[]
Jumlah_Matkul = int(input ("Jumlah Matkul: "))

for i in range (1,Jumlah_Matkul+1) :
    print("----------------------------------")
    print(f'Data Matkul ke-{i}')
    
    Nama= input('Nama Matkul:')
    SKS= float(input('banyak SKS:'))   
    Tugas= float(input('Nilai Tugas:'))
    Kuis= float(input('Nilai Kuis:'))
    UTS= float(input('Nilai UTS:'))
    UAS= float(input('Nilai UAS:'))
    Keaktifan= float(input('Nilai Keaktifan:'))
    
    R_Tugas = Tugas * 0.10
    R_Kuis = Kuis * 0.20
    R_UTS = UTS * 0.30
    R_UAS = UAS * 0.30
    R_Keaktifan = Keaktifan * 0.10
     
    rata_rata= R_Tugas + R_Kuis + R_UTS + R_UAS + R_Keaktifan
    if (rata_rata >= 90) and (rata_rata <= 100):
        grade = 'A+'
    elif (rata_rata >= 85) and (rata_rata <= 90):
        grade = 'A'
    elif (rata_rata >= 80) and (rata_rata <= 85):
        grade = "A-"
    elif (rata_rata >= 75) and (rata_rata <= 80):
        grade = 'B+'
    elif (rata_rata >= 70) and (rata_rata <= 75):
        grade = 'B'
    elif (rata_rata >= 65) and (rata_rata <= 70):
        grade = 'B-'
    elif (rata_rata >= 50) and (rata_rata <= 65):
        grade = 'C'
    elif (rata_rata >= 40) and (rata_rata <= 50):
        grade = 'D'
    else :
        grade = 'E'
    print("\nNilai Grade Mahasiswa = %s"%grade)
    print(f'Rata-rata Mata Kuliah ke-{i}:{rata_rata: .2f}')
print('-----------------------------------------------------------')
Jumlah_SKS= int(input("Jumlah SKS: "))
total_nilai = rata_rata * Jumlah_SKS
print(f'Total nilai: {total_nilai:.2f}')
ipk_semester = total_nilai / Jumlah_SKS
print(f'\nIndeks Prestasi Semester (IPS): {ipk_semester:.2f}')
