def konversi_suhu(suhu, satuan):
    celsius_to_fahrenheit = 9/5
    celsius_to_kelvin = 273.15
    celsius_to_reaumur = 4/5
    fahrenheit_to_celsius = 5/9
    kelvin_to_celsius = 1
    reaumur_to_celsius = 5/4

    if satuan == 'F':
        celsius = fahrenheit_to_celsius * (suhu - 32)
    elif satuan == 'R':
        celsius = reaumur_to_celsius * suhu
    elif satuan == 'K':
        celsius = kelvin_to_celsius + kelvin_to_celsius - celsius_to_kelvin
    else:
        celsius = suhu

    fahrenheit = celsius_to_fahrenheit * celsius + 32
    kelvin = celsius_to_kelvin + celsius
    reaumur = celsius_to_reaumur * celsius

    result = f"Suhu {suhu} {satuan} dapat di konversikan menjadi:\n" + \
             "| Satuan Suhu | Derajat Suhu |\n" + \
             "|-------------|-------------|\n" + \
             f"| Reaumur     | {reaumur:.2f}   |\n" + \
             f"| Fahrenheit  | {fahrenheit:.2f} |\n" + \
             f"| Kelvin     | {kelvin:.2f}   |\n"

    return result

print(konversi_suhu(32, 'C'))
print(konversi_suhu(20, 'F'))
print(konversi_suhu(15, 'R'))
print(konversi_suhu(22, 'K'))