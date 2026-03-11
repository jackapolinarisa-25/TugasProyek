import matplotlib.pyplot as plt

nilai = []

for i in range(10):
    n = int(input("Masukkan nilai ke-" + str(i+1) + ": "))
    nilai.append(n)

tertinggi = max(nilai)
terendah = min(nilai)

lulus = 0
for n in nilai:
    if n >= 60:
        lulus += 1

tidak_lulus = 10 - lulus

# Grafik nilai tertinggi dan terendah
plt.bar(["Tertinggi","Terendah"], [tertinggi, terendah])
plt.title("Grafik Nilai")
plt.show()

# Grafik kelulusan
plt.bar(["Lulus","Tidak Lulus"], [lulus, tidak_lulus])
plt.title("Grafik Kelulusan")
plt.show()
