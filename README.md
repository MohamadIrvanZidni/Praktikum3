# Praktikum3

Repository ini digunakan untuk memenuhi Tugas Bahasa Pemrograman Pertemuan-6

Nama     : Mohamad Irvan Zidni

NIM      : 312210308

Kelas    : TI.22.A.3

| No | Daftar Isi | Link |
| -- | ---------- | ---- |
| 1  | Latihan 1 | [Click Here](https://github.com/MohamadIrvanZidni/Praktikum3#latihan-1) |
| 2  | Latihan 2 | [Click Here](https://github.com/MohamadIrvanZidni/Praktikum3#latihan-2) |
| 3  | Latihan 3 | [Click Here](https://github.com/MohamadIrvanZidni/Praktikum3#latihan-3) |
| 4  | Latihan Menghitung Lingkaran | [Click Here](https://github.com/MohamadIrvanZidni/Praktikum3#program-menghitung-luas-dan-keliling-lingkaran-menggunakan-python) |

# Latihan 1

1. Penggunaan End

![Code](Foto/Penggunaan%20End.png)

    #penggunaan end
    print('A', end='')
    print('B', end='')
    print('C', end='')
    print()
    print('X')
    print('Y')
    print('Z')

Output :

![Output](Foto/Output%20Penggunaan%20End.png)

2. Penggunaan Separator

![Code](Foto/Penggunaan%20Separator.png)

    #penggunaan separator
    w, x, y, z = 10, 15, 20, 25
    print(w, x, y, z)
    print(w, x, y, z, sep=',')
    print(w, x, y, z, sep='')
    print(w, x, y, z, sep=':')
    print(w, x, y, z, sep='-----')

Output :

![Output](Foto/Output%20Penggunaan%20Separator.png)

3. Penggunaan String -1

![Code](Foto/String%20Format.png)

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

![Output](Foto/Output%20String%20Format.png)

4. Penggunaan String -2

![Code](Foto/String%20Format1.png)

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

![Output](Foto/Output%20String%20Format1.png)

# Latihan 2

Program :

![Code](Foto/Code%20Latihan.png)

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

![Output](Foto/Output%20Code.png)

# Latihan 3

Program :

![Code](Foto/Code%20Belah%20Ketupat.png)

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

![Output](Foto/Output%20Belah%20Ketupat.png)

# Program Menghitung Luas dan Keliling Lingkaran Menggunakan Python

1. Buat File Menghitung Luas Lingkaran

![File](Foto/Buat%20File.png)

2. Memasukkan library math pada awal program (otomatisasi rumus phi tanpa mendekalarasikan)

![Import](Foto/Import%20math.png)

    #memasukkan libraries math
    import math

3. Membuat judul awal program

![Judul](Foto/Judul%20Program.png)

    print("")
    print("-------------------------------------------------")
    print("Program Menghitung Luas dan Keliling Lingkaran")
    print("---------------Mohamad Irvan Zidni---------------")
    print("--------------------312210308--------------------")

4. Membuat proses inputan jari-jari oleh user

![Input](Foto/Proses%20Input.png)

    #user memasukkan nilai jari-jari pada lingkaran
    r = float(input("Masukkan Jari-jari : "))

5. Membuat proses perhitungan luas dan keliling

![Hitung](Foto/Proses%20Hitung.png)

    #rumus perhitungan luas & keliling 
    luas = math.pi*r*r
    keliling = 2*math.pi*r

6. Run program yang sudah dibuat

![Run](Foto/Run%20Program.png)

7. Tampilan hasil ke layar

![Output](Foto/Output%20Program.png)

# Flowchart Menghitung Luas dan Keliling Lingkaran

![Flowchart py](https://user-images.githubusercontent.com/115876072/198930934-65319087-aebf-4796-b65c-c4efab81fe7b.png)
