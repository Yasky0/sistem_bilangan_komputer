import numpy as np
from PackageKonversiBilangan import konversi_desimal, konversi_biner, konversi_oktal, konversi_hexsadesimal

# Display

print('''
=============== KONVERSI SISTEM BILANGAN"===============
|                                                      |
| > Guide : Masukan angka yang ada di bawah atau tulis |
| nama sistem bilangan, selanjutnya masukan nilai      |
| bilangan sesuai tipenya, dan nanti otomatis konversi |
| ke tipe bilangan lainnya. :D                         |
|                                                      |
========================================================
| 1. Desimal --> Biner, Oktal, Hexadesimal             |
| 2. Biner --> Desimal, Oktal, Hexadesimal             |
| 3. Oktal --> Desimal, Biner, Hexadesimal             |
| 4. Hexadesimal --> Desimal, Biner, Oktal             |
========================================================
''')

# Sistem
tipe_bilangan = input("Masukan angka/nama tipe bilangan sesuai daftar di atas: ")
tipe_bilangan = tipe_bilangan.lower()
1
if tipe_bilangan == '1' or tipe_bilangan == 'desimal':
    print("DESIMAL --> BINER, OKTAL, HEXADESIMAL")
    input_desimal = int(input("Masukan nilai desimal: "))
    output_desimal1 = konversi_desimal.desimal_biner(input_desimal)
    output_oktal1 = konversi_desimal.desimal_oktal(input_desimal)
    output_hexadesimal1 = konversi_desimal.desimal_hexadesimal(input_desimal)
    print(f'Hasil konversi bilangan desimal ke biner = {input_desimal} ---> {output_desimal1}')
    print(f'Hasil konversi bilangan desimal ke oktal = {input_desimal} ---> {output_oktal1}')
    print(f'Hasil konversi bilangan desimal ke hexadesimal = {input_desimal} ---> {output_hexadesimal1}')
    
elif tipe_bilangan == '2' or tipe_bilangan == 'biner':
    print("BINER --> DESIMAL, OKTAL, HEXADESISMAL")
    input_biner = list(input("Masukan nilai biner: "))
    output_desimal2 = konversi_biner.biner_desimal(input_biner)
    output_oktal2 = konversi_biner.biner_oktal(input_biner)
    output_hexsadesimal2 = konversi_biner.biner_hexsadesimal(input_biner)
    print(f'Hasil konversi bilangan biner ke desimal = {input_biner} ---> {output_desimal2}')
    print(f'Hasil konversi bilangan biner ke oktal = {input_biner} ---> {output_oktal2}')
    print(f'Hasil konversi bilangan biner ke hexsadesimal = {input_biner} ---> {output_hexsadesimal2}')

elif tipe_bilangan == '3' or tipe_bilangan == 'oktal':
    print("OKTAL --> DESIMAL, BINER, HEXSADESIMAL")
    input_oktal = list(input("Masukan nilai oktal: "))
    output_desimal3 = konversi_oktal.oktal_desimal(input_oktal)
    output_biner3 = konversi_oktal.oktal_biner(input_oktal)
    output_hexsadesimal3 = konversi_oktal.oktal_hexsadesimal(input_oktal)
    print(f'Hasil konversi bilangan oktal ke desimal = {input_oktal} ---> {output_desimal3}')
    print(f'Hasil konversi bilangan oktal ke biner = {input_oktal} ---> {output_biner3}')
    print(f'Hasil konversi bilangan oktal ke hexsadesimal = {input_oktal} ---> {output_hexsadesimal3}')
    
elif tipe_bilangan == '4' or tipe_bilangan == 'hexadesimal':
    print("HEXSADESIMAL --> DESIMAL, BINER, BINER")
    input_hexsadesimal = list(input("Masukan nilai hexsadesimal: "))
    output_desimal4 = konversi_hexsadesimal.hexsadesimal_desimal(input_hexsadesimal)
    output_biner4 = konversi_hexsadesimal.hexsadesimal_biner(input_hexsadesimal)
    output_hexsadesimal4 = konversi_hexsadesimal.hexsadesimal_oktal(input_hexsadesimal)
    print(f'Hasil konversi bilangan hexsadesimal ke desimal = {input_hexsadesimal} ---> {output_desimal4}')
    print(f'Hasil konversi bilangan hexsadesimal ke biner = {input_hexsadesimal} ---> {output_biner4}')
    print(f'Hasil konversi bilangan hexsadesimal ke oktal = {input_hexsadesimal} ---> {output_hexsadesimal4}')

else:
    print("Masukan data dengan benarrrrrr!")