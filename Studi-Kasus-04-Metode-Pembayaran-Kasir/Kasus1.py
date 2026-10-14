bayar_tunai = False
bayar_qris = True
bayar_kartu_kredit = False

pembayaran_valid = bayar_tunai or bayar_qris or bayar_kartu_kredit

if pembayaran_valid:
    print("Pembayaran DITERIMA")
else:
    print("Metode pembayaran TIDAK VALID")

#HASIL / OUTPUT PROGRAM:
#Pembayaran DITERIMA
