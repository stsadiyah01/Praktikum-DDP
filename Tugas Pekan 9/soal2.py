# Buatlah fungsi untuk mencari kelulusan nilai dari ketentuan berikut:
# Jika nilai < 60 maka gagal
# Jika nilai = 61-70 maka baik
# Jika nilai = 71-80 maka sangat baik
# Jika nilai = 81-100 maka istimewa
def kelulusan(nilai):
    if nilai <= 60 :
        return "Gagal"
    elif nilai >=61 and nilai <=70 :
        return "Baik"  
    elif nilai >=71 and nilai <=80 :
        return "Sangat Baik" 
    elif nilai >=81 and nilai <=100:
        return "Istimewa" 
    else :
        return "Nilai yang anda masukan tidak valid"
print(kelulusan(60))      
 
