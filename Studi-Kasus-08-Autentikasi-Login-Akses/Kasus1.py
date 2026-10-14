login_lewat_google = False
login_lewat_email_manual = True

login_berhasil = login_lewat_google ^ login_lewat_email_manual

if login_berhasil:
    print("Proses login BERHASIL")
else:
    print("Proses login GAGAL")

#HASIL / OUPUT PROGRAM:
#Proses login BERHASIL
