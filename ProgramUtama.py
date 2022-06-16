#Program Utama Konversi Mata Uang
#Kelompok 15 Praktikum Programa Komputer Teknik Industri 2021

from Modul import start, checkpp, menu, logout
from konversi import konversi
from daftarkurs import daftar_kurs
import time

bendera = True
while bendera:
    ### memasukan nomor passport
    id = start()
    ### mengecek nomor passport
    if checkpp(id):
        print("No. Passport terdaftar")

        ### menampilkan menu
        nomor_menu = menu()
        while True:
            ### menampilkan daftar kurs
            if nomor_menu == "1":
                daftar_kurs()
                nomor_menu = menu()

            ### melakukan konversi
            elif nomor_menu == "2":
                sebelum, sesudah, dari, ke, flag = konversi()
                ### konfirmasi melakukan konversi
                confirm = 0
                while confirm != "y" and confirm != "n":
                    if flag:
                        confirm = input(f"Konfirmasi konversi {sebelum:.2f} {dari} menjadi {sesudah:.2f} {ke}.(y/n) ")

                    else:
                        confirm = "n"

                    ### melanjutkan melakukan konversi dan menulis log
                    if confirm == "y":
                        ambilwaktu = time.localtime() ### mengambil waktu saat melakukan konversi
                        waktu = time.strftime("[%m/%d/%Y, %H:%M:%S]", ambilwaktu)
                        teks = f"\n{waktu} Nomor Passport {id} berhasil melakukan konversi sejumlah {sebelum:.2f} {dari} menjadi {sesudah:.2f} {ke}."
                        file_log = open("log.txt","a")
                        file_log.write(teks)
                        file_log.close()
                        print("Terima kasih telah melakukan konversi.")
                        input("Tekan untuk melanjutkan ke menu utama ... ")
                        nomor_menu = menu()

                    ### pilihan mengulang konversi
                    elif confirm == "n":
                        choice = 0
                        while choice != "y" and choice != "n":
                            choice = input("Ingin mengulangi konversi?(y/n) ")

                            if choice == "y":
                                nomor_menu = "2"     

                            elif choice == "n":
                                input("Tekan untuk kembali ke menu utama ... ")
                                nomor_menu = menu()  
                            else:
                                print("Masukkan tidak dikenal.")

                    else:
                        print("Masukkan tidak dikenal.")

            ### melakukan logout
            elif nomor_menu == "3":
                logout()

            else:
                print("Nomor menu tidak dikenal.")
                input("Tekan untuk kembali ke menu utama ... ")
                nomor_menu = menu()

    ### nomor passport tidak sesuai
    else:
        print("Mohon periksa kembali No. Passport anda.")
        bendera = True