nota_ada = True
garansi_aktif = True
segel_utuh = True

garansi_valid = nota_ada and garansi_aktif and segel_utuh

if garansi_valid:
    print("Klaim garansi DITERIMA")
else:
    print("Klaim garansi DITOLAK")

#HASIL / OUTPUT PROGRAM:
#Klaim garansi DITERIMA
