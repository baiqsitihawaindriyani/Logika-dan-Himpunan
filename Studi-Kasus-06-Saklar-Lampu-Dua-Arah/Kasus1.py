saklar_pintu = True
saklar_kasur = False

lampu_nyala = saklar_pintu ^ saklar_kasur

if lampu_nyala:
    print("Lampu Kamar MENYALA")
else:
    print("Lampu Kamar MATI")

#HASIL / OUTPUT PROGRAM:
#Lampu Kamar MENYALA
