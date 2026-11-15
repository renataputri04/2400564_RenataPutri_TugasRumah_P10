jumlah_koli = int(input("Jumlah koli: "))
berat_per_koli = float(input("Berat per koli (kg): "))

total_berat = jumlah_koli * berat_per_koli

print(f"Total berat: {total_berat} kg")
# Catatan perbaikan:
# 1. SyntaxError: invalid syntax
# Penyebab: nama variabel menggunakan spasi.
# Perbaikan: mengganti total berat menjadi total_berat.

# 2. TypeError: can't multiply sequence by non-int of type 'str'
# Penyebab: input() menghasilkan data bertipe string.
# Perbaikan: menggunakan int() dan float().

# 3. TypeError: can only concatenate str (not "float") to str
# Penyebab: menggabungkan teks dengan angka secara langsung.
# Perbaikan: menggunakan f-string.