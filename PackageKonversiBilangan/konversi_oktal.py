from PackageKonversiBilangan import konversi_biner
def oktal_biner(oktal):
    hasil_biner = []

    for item in oktal:
        input_desimal = int(item)
        biner = []
        
        while input_desimal > 0:
            sisa = input_desimal % 2
            biner.insert(0, sisa)  # Tambahkan bit di depan
            input_desimal //= 2
        
        # Pastikan panjang biner adalah 3 bit (sesuai representasi oktal ke biner)
        while len(biner) < 3:
            biner.insert(0, 0)
        
        hasil_biner.extend(biner)  # Gabungkan ke hasil akhir
    
    return hasil_biner

def oktal_desimal(oktal):
    pangkat = len(oktal) - 1
    hasil = 0
    for item in oktal: # Nilai pada data list oktal harus tipe str
        item = int(item)
        hasil += item*(8**pangkat)
        pangkat-=1
        
    return hasil

def oktal_hexsadesimal(oktal):
    
    nol = 0
    empat = 4
    hasil_hexsadesimal = []
    biner = oktal_biner(oktal)
    print(biner)
    while len(biner) % 4 != 0:
        biner.insert(0,0)
    
    while nol < len(biner):
        hasil = biner[nol:empat]
        nol += 4
        empat += 4
        hasil_hexsadesimal += konversi_biner.biner_hexsadesimal(hasil)
    
    while hasil_hexsadesimal[0] == 0:
        hasil_hexsadesimal.remove([0])
        
    return hasil_hexsadesimal