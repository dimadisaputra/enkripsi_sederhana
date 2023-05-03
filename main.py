#import fungsi enkripsi
import enkripsi

# inputan dari user
inputan_user = input("Masukkan inputan Anda: ")

# enkripsi inputan
hasil_enkripsi = enkripsi.fungsi_enkripsi(inputan_user)

# cetak inputan dan hasil enkripsi ke layar
print("Inputan Anda: ", inputan_user)
print("Hasil Enkripsi: ", hasil_enkripsi)