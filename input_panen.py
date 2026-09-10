def input_hasil_panen():
    hasil = []

    jumlah_data = int(input("Masukkan jumlah data hasil panen: "))

    for i in range(jumlah_data):
        nilai = float(input(f"Masukkan hasil panen ke-{i+1}: "))
        hasil.append(nilai)

    return hasil
