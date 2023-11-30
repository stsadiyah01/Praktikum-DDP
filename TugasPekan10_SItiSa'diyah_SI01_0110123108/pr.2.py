def duplikasi(listbuah):
    buah_terduplikasi=[]
    for buah in listbuah:
        buah_terduplikasi.append(buah)
        buah_terduplikasi.append(buah)
    return buah_terduplikasi
hasil = duplikasi(["Pepaya","Mangga","Pisang","Durian","Jambu"])  
print("Hasil duplikatnya",hasil)  
        
