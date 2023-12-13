from Gempa import *
# Lokasi dan Skala
Banten  = Gempa("Banten", 1.2)
Palu = Gempa("Palu", 6.1)
Cianjur = Gempa("Cianjur", 5.6)
Jayapura = Gempa("Jayapura", 3.3)
Garut = Gempa ("Garut", 4.0)

# Dampak Gempa
print("Gempa di Banten dengan skala 1.2 berdampak",Banten.dampak())
print("Gempa di Palu dengan skala 6.1 berdampak",Palu.dampak())
print("Gempa di Cianjur dengan skala 5.6 berdampak",Cianjur.dampak())
print("Gempa di Jayapura dengan skala 3.3 berdampak",Jayapura.dampak())
print("Gempa di Garut dengan skala 4.0 berdampak",Garut.dampak())
