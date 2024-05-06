print("Nama = Nasywa Adila Rahma")
print("Nim = 2310433022")
print("SHIFT-2")
print("Data Nilai Ujian Mahasiswa Universitas Andalas")
print("<<<<<<<<<<>>>>>>>>>>")

data = [
    [80, 75, 90],
    [70, 85, 60],
    [95, 80, 92],
    [60, 70, 80]
]

print("Data Nilai Ujian:")
print("Nama", end=" ")
nama = ["Nanad", "Azlin", "Dea", "Aulia"]
mata_kuliah = ["  Kaldu", "ADP", "Matdis"]
for subject in mata_kuliah:
    print(f"{subject:>10}", end="")
print()
for i, grade in enumerate(data):
    print(f"{nama[i]:>5}", end="")
    for score in grade:
        print(f"{score:>10}", end="")
    print()


rata_rata = []
for i in range(len(data)):
    total_value = 0
    total_elements = 0
    for j in range(len(data[i])):
        total_value += data[i][j]
        total_elements += 1
    rata_rata.append(total_value / total_elements)
print("<<<<<<<<<<>>>>>>>>>>")
print("Rata-rata Nilai Ujian Mahasiswa:")
for i in range(len(nama)):
    print("{}: {}".format(nama[i], rata_rata[i]))
print("\n")
print("<<<<<<<<<<<>>>>>>>>>>")
print("\nNilai Tertinggi dan Terendah :")
for j, subject in enumerate(mata_kuliah):
    subject_grades = [grade[j] for grade in data]
    max_grade = max(subject_grades)
    min_grade = min(subject_grades)
    max_index = subject_grades.index(max_grade)
    min_index = subject_grades.index(min_grade)
    print(f"{subject:>10}:")
    print(f"  Nilai Tertinggi: {max_grade} (by {nama[max_index]})")
    print(f"  Nilai Terendah: {min_grade} (by {nama[min_index]})")