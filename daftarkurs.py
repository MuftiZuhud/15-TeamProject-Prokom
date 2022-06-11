import pandas as pd

def daftar_kurs():
    df = pd.read_csv("kurs.csv", delimiter=",")
    kurs = [list(row) for row in df.values]
    print("=================================================")
    print("                   Daftar Kurs")
    print("   Mata Uang       Harga Jual       Harga Beli")
    print("=================================================")
    for i in range(1, len(kurs)+1):
        print("     ","{:12.2s}".format(kurs[i -1][0],), "{:.2f}".format(kurs[0][1]/kurs[i - 1][1]), "{:16.2f}".format(kurs[0][1]/kurs[i - 1][2]))
    print("=================================================")
    input("Tekan untuk melanjutkan ...")

#daftar_kurs()