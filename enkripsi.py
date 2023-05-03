def fungsi_enkripsi(inputan):
    # konversi inputan ke string dan ambil setiap karakternya
    inputan_str = str(inputan)
    karakter = list(inputan_str)

    # enkripsi setiap karakter
    enkripsi_karakter = []
    for kar in karakter:
        enkripsi_karakter.append(str(ord(kar) * 69))

    # gabungkan hasil enkripsi ke dalam string
    enkripsi_str = "".join(enkripsi_karakter)

    return enkripsi_str

def fungsi_dekripsi(inputan):
    # konversi inputan ke string dan ambil setiap karakternya
    inputan_str = str(inputan)
    
    # split hasil enkripsi ke dalam list dengan panjang 4 digit
    karakter = [inputan_str[i:i+4] for i in range(0, len(inputan_str), 4)]
    
    # dekripsi setiap karakter
    dekripsi_karakter = []
    for kar in karakter:
        dekripsi_karakter.append(chr(int(kar) // 69))

    # gabungkan hasil dekripsi ke dalam string
    dekripsi_str = "".join(dekripsi_karakter)

    return dekripsi_str