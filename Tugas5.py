phi = 3.14
jari_jari = float(input("Masukkan jari-jari tabung: "))
tinggi = float(input("Masukkan tinggi tabung: "))

luas_alas = phi * jari_jari * jari_jari
luas_selimut = 2 * phi * jari_jari * tinggi
luas_permukaan = 2 * luas_alas + luas_selimut
keliling_alas = 2 * phi * jari_jari

print("Luas alas tabung:", luas_alas)
print("Luas selimut tabung:", luas_selimut)
print("Luas permukaan tabung:", luas_permukaan)
print("Keliling alas tabung:", keliling_alas)