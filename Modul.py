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
    id = int(input("Masukkan No. Passport anda: "))
    return id

def checkpp(id):
    ### mengecheck apakah nomor passporrt yang dimasukkan sama dengan yang ada di list
    df = pd.read_csv("passpor.csv", delimiter=",")
    passpor = [list(row) for row in df.values]
    check = False
    for row in passpor:
        if row[0] == id:
            check = True
            break
    return check

def menu():
    ### menentukkan menu mana yang dipilih user
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
    nomor_menu = int(input("Masukkan nomor menu yang diinginkan = "))
    return nomor_menu

def logout():
    ### keluar dari program
    print("Berhasil Log out")
    exit()