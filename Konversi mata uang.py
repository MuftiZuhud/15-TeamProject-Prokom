#Currency Corverter
#Program yang menstimulasikan bagaimana sebuah Currency Converter

no_passport = [3256758, 2341567, 6789543, 5432678, 9075432, 7865456, 6875430, 4563219, 8765432, 8790654, 6786908, 7654890]

kurs = [# Dalam IDR
        [['IDR', '1000'], ['USD', '0.068'], ['SGD', '0.09'], ['EUR', '0.064'], ['AUD', '0.096'], ['GBP', '0.054'], ['JPY', '8.72'], ['KRW', '86.9'], ['HKD', '0.53'], ['CNY', '0.45'], ['SAR', '0.25'], ['MYR', '0.3']],
        # Dalam USD
        [['IDR', '14662.60'], ['USD', '1'], ['SGD', '1.38'], ['EUR', '0.94'], ['AUD', '1.41'], ['GBP', '0.80'], ['JPY', '127.78'], ['KRW', '1261.99'], ['HKD', '7.85'], ['CNY', '6.66'], ['SAR', '3.75'], ['MYR', '4.39']],
        # Dalam SGD
        [['IDR', '10663.08'], ['USD', '0.73'], ['SGD', '1'], ['EUR', '0.69'], ['AUD', '1.02'], ['GBP', '0.58'], ['JPY', '92.89'], ['KRW', '917.79'], ['HKD', '5.71'], ['CNY', '4.84'], ['SAR', '2.73'], ['MYR', '3.19']],
        # Dalam EUR
        [['IDR', '15552.61'], ['USD', '1.06'], ['SGD', '1.46'], ['EUR', '1'], ['AUD', '1.49'], ['GBP', '0.84'], ['JPY', '135.52'], ['KRW', '1339.42'], ['HKD', '8.33'], ['CNY', '7.06'], ['SAR', '3.98'], ['MYR', '4.65']],
        # Dalam AUD
        [['IDR', '10405.03'], ['USD', '00.71'], ['SGD', '0.97'], ['EUR', '0.66'], ['AUD', '1'], ['GBP', '0.56'], ['JPY', '90'], ['KRW', '896'], ['HKD', '5.57'], ['CNY', '4.72'], ['SAR', '2.66'], ['MYR', '3.11']],
        # Dalam GBP
        [['IDR', '18401.48'], ['USD', '1.25'], ['SGD', '1.72'], ['EUR', '1.17'], ['AUD', '1.76'], ['GBP', '1'], ['JPY', '160'], ['KRW', '1585'], ['HKD', '9.86'], ['CNY', '8.36'], ['SAR', '4.71'], ['MYR', '5.51']],
        # Dalam JPY
        [['IDR', '114.62'], ['USD', '0.0078'], ['SGD', '0.01'], ['EUR', '0.0073'], ['AUD', '0.01'], ['GBP', '0.0062'], ['JPY', '1'], ['KRW',' 9'], ['HKD', '0.06'], ['CNY', '0.05'], ['SAR', '0.02'], ['MYR', '0.03']],
        # Dalam KRW
        [['IDR', '11.62'], ['USD', '0.00079'], ['SGD', '0.0011'], ['EUR', '0.00074'], ['AUD', '0.0011'], ['GBP', '0.00063'], ['JPY', '0.10'], ['KRW', '1'], ['HKD', '0.0062'], ['CNY', '0.053'], ['SAR', '0.0030'], ['MYR', '0.0035']],
        # Dalam HKD
        [['IDR', '1868.84'], ['USD', '0.13'], ['SGD', '0.17'], ['EUR', '0.12'], ['AUD', '0.18'], ['GBP', '0.10'], ['JPY', '16.25'], ['KRW', '160.78'], ['HKD', '1'], ['CNY', '0.85'], ['SAR', '0.48'], ['MYR', '0.56']],
        # Dalam CNY
        [['IDR', '2203.86'], ['USD', '0.15'], ['SGD', '0.21'], ['EUR', '0.14'], ['AUD', '0.21'], ['GBP', '0.12'], ['JPY', '19.16'], ['KRW', '189.60'], ['HKD', '1.18'], ['CNY', '1'], ['SAR', '0.56'], ['MYR', '0.66']],
        # Dalam SAR
        [['IDR', '3910.41'], ['USD', '0.226'], ['SGD', '0.367'], ['EUR', '0.252'], ['AUD', '0.378'], ['GBP', '0.213'], ['JPY', '34.11'], ['KRW', '339.739'], ['HKD', '2.092'], ['CNY', '1.78'], ['SAR', '1'], ['MYR', '1.17']],
        # Dalam MYR
        [['IDR', '3340.56'], ['USD', '0.227'], ['SGD', '0.314'], ['EUR', '0.215'], ['AUD', '0.323'], ['GBP', '0.182'], ['JPY', '29.139'], ['KRW', '290.23'], ['HKD', '1.787'], ['CNY', '1.5424'], ['SAR', '0.854'], ['MYR', '1']]]


def checkpp(id):
    ### mengecheck apakah nomor passporrt yang dimasukkan sama dengan yang ada di list
    check = False
    for i in range(len(no_passport)):
        if no_passport[i] == id:
            check = True
    return check


def menu():
    ### menentukkan menu mana yang dipilih user
    print(""""
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
|                           Currency Converter                          |
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


def daftar_kurs():
    nomor_pilihan = int(input('''
---------------------------------------------------------------------
|                          Daftar kurs                              |
|                                                                   |
|    1. Tekan 1 untuk melihat daftar kurs dalam IDR                 |
|    2. Tekan 2 untuk melihat daftar kurs dalam USD                 |
|    3. Tekan 3 untuk melihat daftar kurs dalam SGD                 |
|    4. Tekan 4 untuk melihat daftar kurs dalam EUR                 |
|    5. Tekan 5 untuk melihat daftar kurs dalam AUD                 |
|    6. Tekan 6 untuk melihat daftar kurs dalam GBP                 |
|    7. Tekan 7 untuk melihat daftar kurs dalam JPY                 |
|    8. Tekan 8 untuk melihat daftar kurs dalam KRW                 |
|    9. Tekan 9 untuk melihat daftar kurs dalam HKD                 |
|    10. Tekan 10 untuk melihat daftar kurs dalam CNY               |
|    11. Tekan 11 untuk melihat daftar kurs dalam SAR               |
|    12. Tekan 12 untuk melihat daftar kurs dalam MYR               |
|                                                                   |
|    Tekan 0 untuk kembali ke menu utama                            |
---------------------------------------------------------------------
Pilihan anda : '''))
    print("---------------------------------------------------------------------")
    if 1 <= nomor_pilihan <= 10 :
        if nomor_pilihan == 1:
            a = "1000 IDR"
        elif nomor_pilihan == 2:
            a = "1 USD"
        elif nomor_pilihan == 3:
            a = "1 SGD" 
        elif nomor_pilihan == 4:
            a = "1 EUR"
        elif nomor_pilihan == 5:
            a = "1 AUD"
        elif nomor_pilihan == 6:
            a = "1 GBP"
        elif nomor_pilihan == 7:
            a = "1 JPY"
        elif nomor_pilihan == 8:
            a = "1 KRW"
        elif nomor_pilihan == 9:
            a = "1 HKD"
        elif nomor_pilihan == 10:
            a = "1 CNY"
        elif nomor_pilihan == 11:
            a = "1 SAR"
        elif nomor_pilihan == 12:
            a = "1 MYR"
        print(f'                   Daftar kurs dalam {a}')
        for i in range(1,13):
            print(i, '.', kurs[nomor_pilihan - 1][i -1][0], '=', kurs[nomor_pilihan - 1][i - 1][1])
        print("---------------------------------------------------------------------")
    elif nomor_pilihan == 0:
        nomor_pilihan = menu()
        return nomor_pilihan
    else:
        print("Masukkan tidak dikenal kembali ke menu sebelumnya.")
        input("Tekan untuk melanjutkan ... ")
        nomor_pilihan = menu()
        return nomor_pilihan
    input("Tekan untuk melanjutkan ... ")
    nomor_pilihan = menu()
    return nomor_pilihan