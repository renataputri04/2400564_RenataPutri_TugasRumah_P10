"""
Program untuk menghitung total nilai persediaan
berdasarkan jumlah unit dan harga satuan.
"""

HARGA_SATUAN_DEFAULT = 85000  # Rupiah per unit

jumlah_unit = int(input("Masukkan jumlah unit: "))
harga_satuan = int(input("Masukkan harga satuan (Rp): "))

total_nilai = jumlah_unit * harga_satuan

print(f"Total nilai persediaan: Rp {total_nilai:,}")
