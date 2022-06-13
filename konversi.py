import pandas as pd

def konversi():
    ### melakukan konversi
    df = pd.read_csv("kurs.csv", delimiter=",")
    kurs = [list(row) for row in df.values]
    print("=================================================")
    print("        Daftar Mata Uang Yang Diterima")
    print("=================================================")
    for j in range(1, len(kurs)+1):
        print(j, ".", kurs[j-1][0])
    print("=================================================")
    kurs_awal = input("Masukkan nomor jenis mata uang yang ingin dikonversi : ")
    kurs_akhir = input("Masukkan nomor jenis mata uang tujuan konversi : ")
    nominal = input("Masukkan nominal uang yang ingin dikonversi : ")
    if kurs_awal.isnumeric() and kurs_akhir.isnumeric() and nominal.isnumeric():
        kurs_awal = int(kurs_awal)
        kurs_akhir = int(kurs_akhir)
        nominal = float(nominal)
        if 1 <= kurs_awal <= len(kurs) and 1 <= kurs_akhir <= len(kurs):
            hasil = nominal*(float(kurs[kurs_akhir-1][1]/kurs[kurs_awal-1][2]))
            flag = True
            return nominal, hasil, kurs[kurs_awal-1][0], kurs[kurs_akhir-1][0], flag
        else:
            print("Masukkan tidak dikenal kembali ke menu sebelumnya.")
            input("Tekan untuk melanjutkan ... ")
            flag = False
            return 0, 0, 0, 0, flag 
    else:
        print("Masukkan tidak dikenal kembali ke menu sebelumnya.")
        input("Tekan untuk melanjutkan ... ")
        flag = False
        return 0, 0, 0, 0, flag 