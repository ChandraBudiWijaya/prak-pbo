phi = 3.14

def luas_lingkaran (jari_jari):
    return phi* jari_jari**2

def keliling_Lingkaran (jari_jari):
    return 2 * phi * jari_jari

def main():
    jari_jari = float(input("Masukkan Ukuran Jari-jari Lingkaran: "))
    
    if (jari_jari < 0):
        print("Jari-jari lingkaran tidak boleh bernilai Negatif")
        return
    
    print("Jari-jari : ",jari_jari)
    print("Luas : ", round(luas_lingkaran(jari_jari),2))
    print("Keliling : ", round(keliling_Lingkaran(jari_jari),2))
    
if __name__ == "__main__":
    main()