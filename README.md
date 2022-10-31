# Praktikum3

### Repository ini digunakan untuk memenuhi Tugas Bahasa Pemrograman Pertemuan-6

## Nama     : Mohamad Irvan Zidni

## NIM      : 312210308

## Kelas    : TI.22.A.3

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

2. Penggunaan Separator

![Penggunaan Separator](https://user-images.githubusercontent.com/115876072/198936507-2cffe74a-61cd-4f6b-a285-7f001162a0ab.png)

    #penggunaan separator
    w, x, y, z = 10, 15, 20, 25
    print(w, x, y, z)
    print(w, x, y, z, sep=',')
    print(w, x, y, z, sep='')
    print(w, x, y, z, sep=':')
    print(w, x, y, z, sep='-----')

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

# Program Menghitung Luas dan Keliling Lingkaran Menggunakan Python
-

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

========================================================================

# Flowchart Menghitung Luas dan Keliling Lingkaran
-

![Flowchart py](https://user-images.githubusercontent.com/115876072/198930934-65319087-aebf-4796-b65c-c4efab81fe7b.png)
