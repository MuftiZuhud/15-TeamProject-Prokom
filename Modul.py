import pandas as pd

def start():
    ### menginput nomor passport
    input("""
---------------------------------------------------------------------
|                         Konversi Mata Uang                        |
|                                                                   |
|                                                                   |
|                                                                   |
|                                                                   |
|                   Tekan apapun untuk melanjutkan                  |
|                                                                   |
---------------------------------------------------------------------
""")
    id = input("Masukkan No. Passport anda: ")
    return id

def checkpp(id):
    ### mengecek apakah nomor passport yang dimasukkan sesuai dengan yang ada di csv
    df = pd.read_csv("passpor.csv", delimiter=",")
    passpor = [list(row) for row in df.values]
    check = False
    if id.isnumeric():
        id = int(id)
        for row in passpor:
            if row[0] == id:
                check = True
                break
    return check

def menu():
    ### menentukan menu mana yang dipilih user
    print("""
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
    nomor_menu = input("Masukkan nomor menu yang diinginkan = ")
    return nomor_menu

def logout():
    ### keluar dari program
    print("Berhasil Log out")
    exit()