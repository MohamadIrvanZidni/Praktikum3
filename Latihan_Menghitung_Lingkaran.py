#memasukkan libraries math
import math

print("")
print("-------------------------------------------------")
print("Program Menghitung Luas dan Keliling Lingkaran")
print("---------------Mohamad Irvan Zidni---------------")
print("--------------------312210308--------------------")

#user memasukkan nilai jari-jari pada lingkaran
r = float(input("Masukkan Jari-jari : "))

#rumus perhitungan luas & keliling 
luas = math.pi*r*r
keliling = 2*math.pi*r

#mengeluarkan hasil dari proses ke layar
print("-------------------------------------------------")
print("Luas Lingkaran       : ", luas)
print("Keliling Lingkaran   : ", keliling)
print("-------------------------------------------------")
print("")