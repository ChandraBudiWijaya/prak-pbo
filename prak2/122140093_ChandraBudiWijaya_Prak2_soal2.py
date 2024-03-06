def punya_motor(func):
    def wrapper(*args):
        print("Saya punya motor dengan spesifikasi sebagai berikut.")
        func(*args)

    return wrapper


class Motor:
    def __init__(self, merk, tipe_motor, tahun):
        self.merk = merk
        self.tipe_motor = tipe_motor
        self.tahun = tahun

    @punya_motor
    def ciri_motor(self):
        print(f"Merk: {self.merk} \nTipe: {self.tipe_motor} \nTahun: {self.tahun}")

    def __del__(self):
        print(f"Motor {self.tipe_motor} Telah Terjual")


motor1 = Motor("Honda", "CRF 250", 2020)
motor1.ciri_motor()

motor2 = Motor("Kawasaki", "KLX 150", 2021)
motor2.ciri_motor()

motor3 = Motor("Yamaha", "Xmax 250", 2024)
motor3.ciri_motor()