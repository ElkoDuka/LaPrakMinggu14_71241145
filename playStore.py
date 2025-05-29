from collections import defaultdict

# Data kategori dengan daftar aplikasinya
kategori = {
    "Game": {"Aplikasi1", "Aplikasi2", "Aplikasi3"},
    "Pendidikan": {"Aplikasi2", "Aplikasi4"},
    "Produktivitas": {"Aplikasi3", "Aplikasi5"},
}

# Membuat dictionary untuk menghitung jumlah kemunculan setiap aplikasi
jumlah_kemunculan = defaultdict(int)

for daftar_aplikasi in kategori.values():
    for aplikasi in daftar_aplikasi:
        jumlah_kemunculan[aplikasi] += 1

# Menampilkan aplikasi yang hanya muncul di satu kategori
hanya_satu_kategori = []
for aplikasi, jumlah in jumlah_kemunculan.items():
    if jumlah == 1:
        hanya_satu_kategori.append(aplikasi)

print("Aplikasi yang hanya muncul di satu kategori:")
print(hanya_satu_kategori)

# Jika jumlah kategori lebih dari 2, tampilkan aplikasi yang muncul tepat di dua kategori
if len(kategori) > 2:
    tepat_dua_kategori = []
    for aplikasi, jumlah in jumlah_kemunculan.items():
        if jumlah == 2:
            tepat_dua_kategori.append(aplikasi)

    print("Aplikasi yang muncul tepat di dua kategori:")
    print(tepat_dua_kategori)
