def baca_kata_dari_file(nama_file):
    try:
        with open(nama_file, "r") as f:
            isi = f.read()
            kata = isi.lower().split()
            return set(kata)
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")
        return None
    except:
        print(f"Gagal membaca file '{nama_file}'.")
        return None

file1 = input("Masukkan nama file pertama: ")
file2 = input("Masukkan nama file kedua: ")

kata_file1 = baca_kata_dari_file(file1)
kata_file2 = baca_kata_dari_file(file2)

if kata_file1 is not None and kata_file2 is not None:
    hasil = kata_file1 & kata_file2
    print("Kata-kata yang muncul di kedua file:")
    for kata in sorted(hasil):
        print(kata)
