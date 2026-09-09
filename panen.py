
def hitung_total(hasil_panen):
    return sum(hasil_panen)

def hitung_diskon(total, persen):
    return total - (total * persen / 100)

hasil = [100, 150, 200]

total = hitung_total(hasil)
total_setelah_diskon = hitung_diskon(total, 10)

print("Total hasil panen:", total)
print("Total setelah diskon:", total_setelah_diskon)
