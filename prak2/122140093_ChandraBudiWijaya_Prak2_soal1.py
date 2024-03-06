class Mahasiswa:
    def __init__(self,  nim, nama, angkatan, isMahasiswa = True):
        self.nim = nim
        self.nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa
        
    def set_nim(self, nim):
        self.nim = nim
        
    def get_nim(self):
        return self.nim
    
    def set_nama(self, nama):
        self.nama = nama
        
    def get_nama(self):
        return self.nama
    def method1 (self):
        return f"Nama Mahasiswa/i : {self.nama} \nNIM : {self.nim}"
    def method2 (self):
        return f"Mahasiswa/i {self.nama} dengan NIM {self.nim} merupakan mahasiswa/i Angkatan {self.angkatan}"
    def method3 (self):
        return f"{self.nama} {' merupakan seorang mahasiswa/i ITERA' if self.isMahasiswa else ' bukan mahasiswa/i ITERA'}"
    

mhs1 = Mahasiswa (122140093, "Chandra Budi Wijaya", 2022, True)

mhs2 = Mahasiswa (110140093, "Amir Cilok", 2022)

print (mhs1.method1())
print (mhs1.method2())
print (mhs1.method3())
print ("\n")
print (mhs2.method1())
print (mhs2.method2())
print (mhs2.method3())