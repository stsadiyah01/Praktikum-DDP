# Tugas 2 Menghitung Luas Bangun Datar
print("========================================================")
print("Program Penghitung Luas Bangun Datar")
print(''' 
Pilih salah satu bangun datar :
 1 = Luas Persegi
 2 = Luas Lingkaran
 3 = Luas Segitiga           
''')
print("========================================================")

Pilihan= int(input ("Masukan Pilihan:"))
match Pilihan:
    case 1 :
        sisi = int(input ("Masukan sisi:"))
        luas =  sisi * sisi
        print("Luas persegi dengan sisi",sisi, "adalah", luas)
    case 2 :
        jari = int(input("Masukan jari-jari:"))
        phi = 3.14
        luas= phi * jari ** 2
        print("Luas lingkaran dengan jari-jari",jari,"adalah",luas)
    case 3 :
        alas = int(input("Masukan alas:")) 
        tinggi = int(input("Masukan tinggi:")) 
        luas = 0.5 * alas * tinggi
        print("Luas segitiga dengan alas",alas,"dan tinggi",tinggi, "adalah",luas)
    case _ :
        print("Pilihan anda salah")    

        
        

    
