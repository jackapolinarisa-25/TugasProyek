
#input nilai
nilai = []

for i in range(10):
    n = int(input("Masukkan nilai ke-" + str(i+1) + ": "))
    nilai.append(n)

# Nilai tertinggi dan terendah
tertinggi = max(nilai)
terendah = min(nilai)

# Rata-rata
rata = sum(nilai) / len(nilai)

# Jumlah lulus
lulus = 0
for n in nilai:
    if n >= 60:
        lulus += 1

print("Nilai tertinggi :", tertinggi)
print("Nilai terendah :", terendah)
print("Rata-rata :", rata)
print("Jumlah mahasiswa lulus :", lulus)
