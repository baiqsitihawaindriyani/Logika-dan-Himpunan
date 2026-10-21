login_lewat_google = True
login_lewat_email_manual = False

login_berhasil = login_lewat_google ^ login_lewat_email_manual

if login_berhasil:
    print("Proses login BERHASIL")
else:
    print("Proses login GAGAL")

#HASIL / OUTPUT PROGRAM:
Proses login BERHASIL
