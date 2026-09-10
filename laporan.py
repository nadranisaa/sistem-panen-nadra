def buat_laporan(hasil_panen):
    total = sum(hasil_panen)
    rata_rata = total / len(hasil_panen)

    print("Laporan Hasil Panen")
    print("Total hasil panen:", total)
    print("Rata-rata hasil panen:", rata_rata)

hasil = [100, 150, 200]

buat_laporan(hasil)
