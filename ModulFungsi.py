import pandas as pd

def checkpp(id):
    ### mengecheck apakah nomor passporrt yang dimasukkan sama dengan yang ada di list
    check = False
    df = pd.read_csv("passpor.csv", delimiter=",")
    passpor = [list(row) for row in df.values]
    for i in range(len(passpor)):
        if passpor[i] == id:
            check = True
    return check

def menu():
    ### menentukkan menu mana yang dipilih user
    print(""""
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
|                           Konversi Mata Uang                          |
|                                                                       |
|   1. Daftar Kurs                                                      |
|   2. Konversi mata uang                                               |
|   3. Log out                                                          |
|                                                                       |
|                                                                       |
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
            """)
    nomor_menu = int(input("Masukkan nomor menu yang diinginkan = "))
    return nomor_menu

def logout():
    ### keluar dari program
    print("Berhasil Log out")
    exit()