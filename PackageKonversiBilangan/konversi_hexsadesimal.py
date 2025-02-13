from PackageKonversiBilangan import konversi_desimal, konversi_biner
def hexsadesimal_desimal(hexsadesimal):
    
    pangkat = len(hexsadesimal)-1
    hasil = 0
    for item in hexsadesimal:
        if item == 'A':
            item = 10
        elif item == 'B':
            item = 11
        elif item == 'C':
            item = 12
        elif item == 'D':
            item = 13
        elif item == 'E':
            item = 14
        elif item == 'F':
            item = 15           

        hasil += int(item)*(16**pangkat)
        pangkat -= 1
    
    return hasil

def hexsadesimal_biner(hexsadesimal):
    
    hasil = []
    for item in hexsadesimal:
        biner = []
        if item == 'A':
            item = 10
        elif item == 'B':
            item = 11
        elif item == 'C':
            item = 12
        elif item == 'D':
            item = 13
        elif item == 'E':
            item = 14
        elif item == 'F':
            item = 15

        
        item = int(item)
        biner.extend(konversi_desimal.desimal_biner(item))
        while len(biner) % 4 != 0:
            biner.insert(0,0)
        hasil.extend(biner)

    return hasil
    

def hexsadesimal_oktal(hexsadesimal):
    
    biner = hexsadesimal_biner(hexsadesimal)
    print(biner)
    nol = 0
    tiga = 3
    hasil = []
    while nol < len(biner):
        biner_tiga = biner[nol:tiga]
        hasil.extend(konversi_biner.biner_oktal(biner_tiga))
        nol += 3
        tiga += 3
    
    return hasil
