def entrans(p, k):  
    c = ''  # Membuat variabel c untuk menyimpan ciphertext.
    b = len(p)  # Menghitung panjang plaintext dan menyimpannya dalam variabel b.
    while b % k > 0:  # Memastikan panjang plaintext adalah kelipatan dari kunci.
        p = p + 'x'  # Jika tidak, tambahkan karakter 'x' untuk membuatnya habis dibagi kunci.
        b = len(p)  # Hitung ulang panjang plaintext yang telah dimodifikasi.
    n = b // k  # Menghitung berapa kali plaintext akan dibagi menjadi blok dengan panjang kunci.
    for i in range(k):  # Loop untuk iterasi sebanyak kunci (blok).
        for j in range(n):  # Loop untuk iterasi sebanyak n (banyaknya blok yang akan dibuat).
            c = c + p[i + j * k]  # Menggabungkan karakter plaintext sesuai indeks dan tambahkan ke ciphertext.
    return c  # Mengembalikan ciphertext yang dihasilkan.

def detrans(c, k):
    b = len(c)  # Menghitung panjang ciphertext.
    k = b // k  # Menghitung berapa kali ciphertext akan dibagi menjadi blok dengan panjang kunci.
    p = ''  # Membuat variabel p untuk menyimpan plaintext hasil dekripsi.
    n = b // k  # Banyaknya blok yang akan dibaca.
    for i in range(k):  # Loop untuk iterasi sebanyak kunci (blok).
        for j in range(n):  # Loop untuk iterasi sebanyak n (banyaknya blok ciphertext yang akan dibaca).
            p = p + c[i + j * k]  # Menggabungkan karakter ciphertext sesuai indeks dan tambahkan ke plaintext.
    return p  # Mengembalikan plaintext hasil dekripsi.

if __name__ == "__main__":
    choice = input("Pilih operasi (1 untuk enkripsi, 2 untuk dekripsi): ")  # Meminta pengguna memilih operasi.
    if choice == '1':  # Jika pengguna memilih enkripsi:
        plaintext = input("Masukkan teks untuk enkripsi: ")  # Meminta input plaintext.
        key = int(input("Masukkan kunci: "))  # Meminta input kunci.
        ciphertext = entrans(plaintext, key)  # Panggil fungsi entrans untuk enkripsi.
        print("Chiper text:", ciphertext)  # Cetak ciphertext.
    elif choice == '2':  # Jika pengguna memilih dekripsi:
        ciphertext = input("Masukkan teks untuk dekripsi: ")  # Meminta input ciphertext.
        key = int(input("Masukkan kunci: "))  # Meminta input kunci.
        plaintext = detrans(ciphertext, key)  # Panggil fungsi detrans untuk dekripsi.
        print("Plain text:", plaintext)  # Cetak plaintext.
    else:
        print("Pilihan tidak valid.")  # Cetak pesan jika pilihan tidak valid.
