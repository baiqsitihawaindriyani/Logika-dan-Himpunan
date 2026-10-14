pilih_work_from_home = True
pilih_work_from_office = False

pilihan_valid = pilih_work_from_home ^ pilih_work_from_office

if pilihan_valid:
    print("Pilihan mode kerja VALID")
else:
    print("Pilihan mode kerja TIDAK VALID (Harus pilih salah satu)")

#HASIL / OUTPUT PROGRAM:
#Pilihan mode kerja VALID
