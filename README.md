# Praktikum3

Repository ini digunakan untuk memenuhi Tugas Bahasa Pemrograman Pertemuan-6

Nama     : Mohamad Irvan Zidni

NIM      : 312210308

Kelas    : TI.22.A.3

# Latihan 1

1. Penggunaan End

![Penggunaan End](https://user-images.githubusercontent.com/115876072/198936483-6197b578-4851-45fb-933e-3e568f279c22.png)

    #penggunaan end
    print('A', end='')
    print('B', end='')
    print('C', end='')
    print()
    print('X')
    print('Y')
    print('Z')

Output :

![Output Penggunaan End](https://user-images.githubusercontent.com/115876072/198937626-719738ac-f234-4bc1-8f08-8d2a5e20729f.png)

2. Penggunaan Separator

![Penggunaan Separator](https://user-images.githubusercontent.com/115876072/198936507-2cffe74a-61cd-4f6b-a285-7f001162a0ab.png)

    #penggunaan separator
    w, x, y, z = 10, 15, 20, 25
    print(w, x, y, z)
    print(w, x, y, z, sep=',')
    print(w, x, y, z, sep='')
    print(w, x, y, z, sep=':')
    print(w, x, y, z, sep='-----')

Output :

![Output Penggunaan Separator](https://user-images.githubusercontent.com/115876072/198937656-dfb2c31e-58e7-4be9-ad14-5d4816ffa8a1.png)

3. Penggunaan String -1

![String Format](https://user-images.githubusercontent.com/115876072/198936522-dd5fff18-13b7-4ba5-967c-1fa63bba0942.png)

    #string format
    print(0, 10**0)
    print(1, 10**1)
    print(2, 10**2)
    print(3, 10**3)
    print(4, 10**4)
    print(5, 10**5)
    print(6, 10**6)
    print(7, 10**7)
    print(8, 10**8)
    print(9, 10**9)
    print(10, 10**10)

Output :

![Output String Format](https://user-images.githubusercontent.com/115876072/198937677-e3f351b1-2407-4583-903a-c6369af24cf4.png)

4. Penggunaan String -2

![String Format1](https://user-images.githubusercontent.com/115876072/198936539-90dd5beb-a76c-48ea-ae0b-ba06c10e9bba.png)

    #string format
    print('{0:>3} {1:>16}'. format(0, 10**0))
    print('{0:>3} {1:>16}'. format(1, 10**1))
    print('{0:>3} {1:>16}'. format(2, 10**2))
    print('{0:>3} {1:>16}'. format(3, 10**3))
    print('{0:>3} {1:>16}'. format(4, 10**4))
    print('{0:>3} {1:>16}'. format(5, 10**5))
    print('{0:>3} {1:>16}'. format(6, 10**6))
    print('{0:>3} {1:>16}'. format(7, 10**7))
    print('{0:>3} {1:>16}'. format(8, 10**8))
    print('{0:>3} {1:>16}'. format(9, 10**9))
    print('{0:>3} {1:>16}'. format(10, 10**10))

Output :

![Output String Format1](https://user-images.githubusercontent.com/115876072/198937713-6f50629c-aa5b-4294-87a8-f20283569d7b.png)

# Latihan 2

Program :

![Code Latihan](https://user-images.githubusercontent.com/115876072/198938694-5247c0a7-17ec-42ef-b6b7-438908b3688e.png)

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

Output :

![Output Code](https://user-images.githubusercontent.com/115876072/198938777-1063af70-d79d-4837-a63a-fa05743ab254.png)

# Latihan 3

Program :

![Code Belah Ketupat](https://user-images.githubusercontent.com/115876072/198939273-657992bf-a70f-4cc2-bc28-a8e97fd304b5.png)

    #Belah Ketupat
    print('{0:>16}'.format("*"))
    print('{0:>17}'.format("***"))
    print('{0:>18}'.format("*****"))
    print('{0:>19}'.format("*******"))
    print('{0:>20}'.format("*********"))
    print('{0:>19}'.format("*******"))
    print('{0:>18}'.format("*****"))
    print('{0:>17}'.format("***"))
    print('{0:>16}'.format("*"))

Output :

![Output Belah Ketupat](https://user-images.githubusercontent.com/115876072/198939299-dae12019-8a69-40ef-88ad-9257ab227f0b.png)

# Program Menghitung Luas dan Keliling Lingkaran Menggunakan Python

1. Buat File Menghitung Luas Lingkaran

![Buat File](https://user-images.githubusercontent.com/115876072/197689567-e8184849-7cf2-4406-811c-43eee4f47e2b.png)

2. Memasukkan library math pada awal program (otomatisasi rumus phi tanpa mendekalarasikan)

![Import math](https://user-images.githubusercontent.com/115876072/197689771-c38394ab-a15b-4f47-9316-bb50ef5c799a.png)

    #memasukkan libraries math
    import math

3. Membuat judul awal program

![Judul Program](https://user-images.githubusercontent.com/115876072/197689910-51e6a3e3-0654-4daf-a3da-e6607ff5aab4.png)

    print("")
    print("-------------------------------------------------")
    print("Program Menghitung Luas dan Keliling Lingkaran")
    print("---------------Mohamad Irvan Zidni---------------")
    print("--------------------312210308--------------------")

4. Membuat proses inputan jari-jari oleh user

![Proses Input](https://user-images.githubusercontent.com/115876072/197690059-abd571ee-272e-455a-934e-8c32ae27ff6c.png)

    #user memasukkan nilai jari-jari pada lingkaran
    r = float(input("Masukkan Jari-jari : "))

5. Membuat proses perhitungan luas dan keliling

![Proses Hitung](https://user-images.githubusercontent.com/115876072/197690184-1b13e41b-dbdb-4576-9ac3-5704b66c20c6.png)

    #rumus perhitungan luas & keliling 
    luas = math.pi*r*r
    keliling = 2*math.pi*r

6. Run program yang sudah dibuat

![Run Program](https://user-images.githubusercontent.com/115876072/197690342-57c90e0a-e74b-46d2-a7c0-b4808018eaa2.png)

7. Tampilan hasil ke layar

![Output Program](https://user-images.githubusercontent.com/115876072/197690508-f0b837e8-3241-4c60-84f8-5a0fc7f229f9.png)



# Flowchart Menghitung Luas dan Keliling Lingkaran

![Flowchart py](https://user-images.githubusercontent.com/115876072/198930934-65319087-aebf-4796-b65c-c4efab81fe7b.png)
