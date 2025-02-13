import numpy as np

def biner_desimal(biner):
    '''Fungsi unuk mengubah biner ke desimal'''
    
    pangkat = [] # Untuk menyimpan nilai pangkat
    # Membuat pangkat yang sesuai dengan biner untuk di operasikan
    for item in range(len(biner)):
        pangkat.append(item)
    
    pangkat.reverse() # Membalik data pangkat
    np_biner = np.array(biner, dtype=np.int64)*(2**np.array(pangkat)) # Mengoperasikan np_biner
    hasil = sum(np_biner) # Menjumlahkan semua hasil operasi
    
    return hasil
    
def biner_oktal(biner):
    '''Fungsi untuk mengubah biner ke oktal'''
    
    # While ini berfungsi untuk menambahkan string "0" di index=0 pada list np_biner
    while len(biner) % 3 == 2 or len(biner) % 3 == 1:
        biner.insert(0, '0')
    
    # Pangkat yang dibutuhkan untuk memangkatkan biner 2,1, dan 0
    pangkat = np.array([2,1,0], dtype=np.int64)
    
    list_biner = [] # untuk menyimpan data biner yang sudah disusun rapi
    
    # mengelompokan 3 nilai dalam 1 list contoh = [0,0,1],[1,1,0],dst
    # Item bernilai kelipatan 3 dari index contoh = 0,3,6,9,12,15,18,21,dst
    for item in range(0, len(biner), 3):
        step = biner[item:item + 3]
        list_biner.append(step) # Menampung data list 3 nilai dari variabel step

    hasil_biner = []
    np_array = np.array(list_biner, dtype=np.int64)*(2**pangkat) # Mengoperasikan np_biner
    
    # Memasukan data hasil operasi kedalam variabel 'hasil'
    for item in range(len(np_array)):
        hasil_biner.append(np.sum(np_array[item]))
        hasil = hasil_biner

    return hasil

def biner_hexsadesimal(biner):
    '''Fungsi ini untuk mengubah biner ke hexsadesimal'''
    
    # While ini berfungsi untuk menambahkan string "0" di index=0 pada list np_biner
    while len(biner) % 4 == 3 or len(biner) % 4 == 2 or len(biner) % 4 == 1:
        biner.insert(0, '0')
    
    # Pangkat yang dibutuhkan untuk memangkatkan biner 2,1, dan 0
    pangkat = np.array([3,2,1,0], dtype=np.int64)
    
    list_biner = [] # untuk menyimpan data biner yang sudah disusun rapi
    
    # mengelompokan 3 nilai dalam 1 list contoh = [0,0,1],[1,1,0],dst
    # Item bernilai kelipatan 3 dari index contoh = 0,3,6,9,12,15,18,21,dst
    for item in range(0, len(biner), 4):
        step = biner[item:item + 4]
        list_biner.append(step) # Menampung data list 3 nilai dari variabel step

    hasil_biner = []
    np_array = np.array(list_biner, dtype=np.int64)*(2**pangkat) # Mengoperasikan np_biner
    
    # Memasukan data hasil operasi kedalam variabel 'hasil'
    for item in range(len(np_array)):
        
        if np.sum(np_array[item]) == 10:
            hasil_biner.append('A')
        elif np.sum(np_array[item]) == 11:
            hasil_biner.append('B')
        elif np.sum(np_array[item]) == 12:
            hasil_biner.append('C')
        elif np.sum(np_array[item]) == 13:
            hasil_biner.append('D')
        elif np.sum(np_array[item]) == 14:
            hasil_biner.append('E')
        elif np.sum(np_array[item]) == 15:
            hasil_biner.append('F')
        else:
            hasil_biner.append(np.sum(np_array[item]))
            
        hasil = hasil_biner

    return hasil