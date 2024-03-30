# Chandra Budi Wijaya
# 122140093
# Praktikum PBO RB

# Kategori: Polymorphism
""" Buatlah dua kelas Persegi dan Lingkaran dengan metode hitungLuas(). Gunakan konsep
polimorfisme agar kita dapat menghitung luas dari objek berbentuk persegi atau lingkaran
tanpa memeriksa jenis objek secara eksplisit. """

class Bentuk:
    def hitungLuas (self):
        pass

class Persegi (Bentuk):
    def __init__ (self, sisi):
        self.sisi = sisi
    
    def hitungLuas (self):
        return self.sisi * self.sisi

class Lingkaran (Bentuk):
    def __init__ (self, jari_jari):
        self.jari_jari = jari_jari
    
    def hitungLuas (self):
        return 3.14 * self.jari_jari * self.jari_jari

def printLuas (bentukbangunan):
    print (bentukbangunan.hitungLuas())

persegi = Persegi (5)
lingkaran = Lingkaran (3)

print ("Luas Persegi:", end= " ")
printLuas (persegi)

print ("Luas Lingkaran:", end= " ")
printLuas (lingkaran)