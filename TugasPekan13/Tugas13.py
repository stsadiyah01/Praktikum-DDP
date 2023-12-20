class Animal :
    # Properti
    nama = ""
    makanan = ""
    habitat = ""
    berkembang_biak = ""

    #Konstruktor
    def __init__(self, nama, makanan, habitat, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.habitat = habitat
        self.berkembang_biak = berkembang_biak

    #Method
    def cetak(self):
        print("="*50)
        print("Nama Hewan\t:",self.nama)
        print("Makanan\t\t:",self.makanan)
        print("Habitat\t\t:",self.habitat)
        print("Cara Berkembang Biak \t:",self.berkembang_biak)
        

class Badak(Animal) :
    # Properti
    jenis_kelamin = ""
    berat_badan = ""

    # Konstruktor
    def __init__(self, nama, makanan, habitat, berkembang_biak,jenis_kelamin,berat_badan):
        super().__init__(nama, makanan, habitat, berkembang_biak)
        self.jenis_kelamin = jenis_kelamin
        self.berat_badan = berat_badan

    # Method
    def cetak(self):
        super().cetak()
        print("Jenis Kelamin\t\t:", self.jenis_kelamin)
        print("Berat Badan\t\t:", self.berat_badan)

    def klasifikasi(self):
        print("Badak termasuk hewan Mamalia")
        print("="*50)

class Ikan(Animal) :
    # Properti
    spesies = ""
    tawar_laut = ""

    # Konstruktor
    def __init__(self,nama,makanan,habitat,berkembang_biak,spesies,tawar_laut):
        super().__init__ (nama,makanan,habitat,berkembang_biak)
        self.spesies = spesies
        self.tawar_laut = tawar_laut

    # Method
    def cetak(self):
        super().cetak()
        print("Nama Jenis Ikan\t:",self.spesies)
        print("Hidup di Air\t:",self.tawar_laut)

    def klasifikasi(self):
        print("Ikan dalam klasifikasi binatang termasuk ke dalam pisces")
        print("="*50)

class Ular(Animal) :
    # Properti
    jenis_ular = ""
    ukuran= ""

    # Konstruktor
    def __init__(self,nama,makanan,habitat,berkembang_biak,jenis_ular,ukuran):
        super().__init__ (nama,makanan,habitat,berkembang_biak)
        self.jenis_ular = jenis_ular
        self.ukuran = ukuran

    # Method
    def cetak(self):
        super().cetak()
        print("Nama Jenis Ular\t:",self.jenis_ular)
        print("Ukuran\t:",self.ukuran)

    def klasifikasi(self):
        print("Ular termasuk reptil")
        print("="*50)



# Objek Badak
x = Badak("Badak","Tumbuhan","Hidup di Hutan (Daratan)","Vivipar(melahirkan)","Jantan","650 Kg")
x.cetak()
x.klasifikasi()

# Objek Ikan
y = Ikan("Ikan","plankton,cacing,pelet,dan organisme lainnya yang lebih kecil darinya","Hidup di Air","Ovivar(Bertelur)","Ikan Mas","Air Tawar")
y.cetak()
y.klasifikasi()

# Objek Ular
z = Ular("Ular","Daging atau hewan lainnya","Hidup di Daratan","Ovivar(bertelur)","Piton","5 Meter")
z.cetak()
z.klasifikasi()
        






