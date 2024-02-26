def hitung_bilangan_ganjil(lower, upper):
    
    count = 0
    for num in range(lower, upper):
        if num % 2 != 0:
            count = count + num
            print(num)
    return count

def main():
    lower = int(input("Batas bawah: "))
    upper = int(input("Batas atas : "))

    if (lower < 0 or upper < 0):
        print("Batas bawah dan atas yang dimasukkan tidak boleh di bawah Nol")
        return

    if (lower <= upper):
        jumlah_ganjil = hitung_bilangan_ganjil(lower, upper)
        print("total:", jumlah_ganjil)
    else:
        print("Batas bawah harus kurang dari atau sama dengan batas atas.")
        return
    
if __name__ == "__main__":
    main()
