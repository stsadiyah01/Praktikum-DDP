# Persegi
def persegi(sisi):
    luas = sisi*sisi
    keliling = 4*sisi
    print("Luas Persegi:",luas)
    print("Keliling Persegi:", keliling)

# Persegi Panjang
def persegi_panjang(panjang,lebar):
    luas = panjang*lebar
    keliling = 2 * (panjang + lebar)
    print("Luas Persegi Panjang:",luas)
    print("Keliling Persegi panjang:",keliling)

# Segitiga sama sisi
def segitiga_sama_sisi(alas,tinggi):
    luas = 0.5 * alas * tinggi
    keliling = 3 * alas
    print("Luas Segitiga Sama Sisi:",luas)
    print("Keliling Segitiga Sama Sisi:", keliling)

# Jajargenjang
def jajargenjang(alas,tinggi,sisi_miring):
    luas = alas * tinggi
    keliling = (2 * alas) + (2 * sisi_miring)
    print("Luas Jajar Genjang:",luas)
    print("Keliling Jajar Genjang:", keliling)

# Trapesium
def lingkaran(jari2):
    phi = 3.14
    luas = phi * jari2 ** 2
    keliling = 2 * jari2 * phi
    print("Luas Lingkaran:",luas)
    print("Keliling Lingkaran:", keliling)

# Belah Ketupat
def belah_ketupat(diagonal1,diagonal2,sisi):
    luas = 0.5 * diagonal1 * diagonal2
    keliling = 4 * sisi
    print("Luas Belah Ketupat:",luas)
    print("Keliling Belah Ketupat:", keliling)

# Layang-layang
def Layang_layang(diagonal1,diagonal2,sisiatas,sisibawah):
    luas = 0.5 * diagonal1 * diagonal2
    keliling = (2 * sisiatas) + (2 * sisibawah)
    print("Luas Layang-layang:",luas)
    print("Keliling Layang-layang:", keliling)
