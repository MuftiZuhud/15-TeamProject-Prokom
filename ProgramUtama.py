from Modul import start, checkpp, menu, logout
from konversi import konversi
from daftarkurs import daftar_kurs

bendera = True
while bendera:
    id = start()
    if checkpp(id):
        print("No. Passport terdaftar")
        nomor_menu = menu()
        while True:
            if nomor_menu == 1:
                daftar_kurs()
                nomor_menu = menu()
        
            elif nomor_menu == 2:
                sebelum, sesudah, dari, ke, flag = konversi()
                confirm = 0
                while confirm != "y" and confirm != "n":
                    if flag:
                        confirm = input(f"Konfirmasi konversi {sebelum:.2f} {dari} menjadi {sesudah:.2f} {ke}.(y/n) ")

                    else:
                        confirm = "n"

                    if confirm == "y":
                            teks = f"\nNomor Passport {id} berhasil melakukan konversi sejumlah {sebelum:.2f} {dari} menjadi {sesudah:.2f} {ke}."
                            file_log = open("log.txt","a")
                            file_log.write(teks)
                            file_log.close()
                            print("Terima kasih telah melakukan konversi.")
                            input("Tekan untuk melanjutkan ke menu utama ... ")
                            nomor_menu = menu()

                    elif confirm == "n":
                        choice = 0
                        while choice != "y" and choice != "n":
                            choice = input("Ingin mengulangi konversi?(y/n) ")
                        
                            if choice == "y":
                                nomor_menu = 2

                            elif choice == "n":
                                input("Tekan enter untuk kembali ke menu utama.")
                                nomor_menu = menu()
                            else:
                                print("Masukkan tidak dikenal.")

                    else:
                        print("Masukkan tidak dikenal.")

            elif nomor_menu == 3:
                logout()

            else:
                print("Nomor menu tidak dikenal.")
                input("Tekan untuk kembali ke menu utama ... ")
                nomor_menu = menu()

    else:
        print("Mohon periksa kembali No. Passport anda.")
        bendera = True