print("Nama: Nasywa Adila Rahma")
print("Nim: 2310433022")
print("SHIFT-2")
print("-----------------------------")

x = []
f = []
g = []
h = []

while True:
    x_val = float(input("Nilai untuk x: "))
    f_val = float(input("Nilai untuk f(x): "))
    g_val = float(input("Nilai untuk g(x): "))
    h_val = float(input("Nilai untuk h(x): "))

    x.append(x_val)
    f.append(f_val)
    g.append(g_val)
    h.append(h_val)

    choice = input("Input nilai x ? (Y/N): ")
    if choice.lower() == 'n':
        break
print("-------------------------------------")
print("x: ", x)
print("f(x): ", f)
print("g(x): ", g)
print("h(x): ", h)
