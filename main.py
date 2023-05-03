#import fungsi enkripsi
import enkripsi

# inputan dari user
inputan_user = input("Masukkan inputan Anda: ")

# enkripsi inputan
hasil_enkripsi = enkripsi.fungsi_enkripsi(inputan_user)
hasil_dekripsi = enkripsi.fungsi_dekripsi(hasil_enkripsi)

# cetak inputan dan hasil enkripsi ke layar
print("Inputan Anda: ", inputan_user)
print("Hasil Enkripsi: ", hasil_enkripsi)
print("Hasil Dekripsi: ", hasil_dekripsi)