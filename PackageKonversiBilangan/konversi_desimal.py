def desimal_biner(input_desimal):
    
    biner = []
    while True:
        sisa = input_desimal % 2
        input_desimal //= 2
        
        if sisa == 1:
            biner.append(1)
        elif sisa == 0:
            biner.append(0)

        if input_desimal == 0:
            break
    biner.reverse()
    return biner

def desimal_oktal(input_desimal):
    
    oktal = []
    while True:
        sisa = input_desimal % 8
        input_desimal //= 8
        
        if sisa < 8:
            oktal.append(sisa)
        elif sisa == 0:
            oktal.append(0)

        if input_desimal == 0:
            break
        
    oktal.reverse()
    return oktal

def desimal_hexadesimal(input_desimal):
    
    hexadesimal = []
    while True:
        sisa = input_desimal % 16
        input_desimal //= 16
        
        if sisa < 10:
            hexadesimal.append(sisa)
        elif sisa == 10:
            hexadesimal.append('A')
        elif sisa == 11:
            hexadesimal.append('B')
        elif sisa == 12:
            hexadesimal.append('C')
        elif sisa == 13:
            hexadesimal.append('D')
        elif sisa == 14:
            hexadesimal.append('E')            
        elif sisa == 15:
            hexadesimal.append('F')
        elif sisa == 0:
            hexadesimal.append(0)
            
        if input_desimal == 0:
            break
    
    hexadesimal.reverse()
    return hexadesimal