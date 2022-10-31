print("Latihan 2")

#input nilai variabel
a = input("Masukkan nilai a : ")
b = input("Masukkan nilai b : ")

#cetak nilai variabel
print("Variabel a : ", a)
print("Variabel b : ", b)

#cetak hasil operasi kedua variabel dengan String Format
print("Hasil Penggabungan {0}&{1}=%d".format(a,b)%int(a+b))

#konversi nilai variabel
a = int(a)
b = int(b)
print("Hasil Penjumlahan {0}+{1}=%d".format(a,b)%int(a+b))
print("Hasil Pembagian {0}/{1}=%d".format(a,b)%int(a/b))