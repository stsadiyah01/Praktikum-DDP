# Tugas 1 OOP
class Gempa :
    # Properti
    lokasi = ""
    skala = 0
    # Konstruktor
    def __init__(self, lokasi, skala):
       self.lokasi = lokasi
       self.skala = skala

    # Method
    def dampak(self):
        if self.skala < 2 :
            return("tidak berasa")
        elif self.skala  >=2 and self.skala <=4:
            return("bangunan retak-retak") 
        elif self.skala  >=4 and self.skala <=6: 
            return("bangunan roboh")  
        else:
            return("bangunan roboh dan berpotensi tsunami") 






