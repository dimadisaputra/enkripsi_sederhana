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
