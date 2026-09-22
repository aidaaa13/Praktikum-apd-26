komponen_1 = 120000 
komponen_2 = 135000 
komponen_3 = 150000
komponen_4 = 175000
komponen_5 = 200000
komponen_6 = 220000

komponen = [komponen_1, komponen_2, komponen_3, komponen_4, komponen_5, komponen_6]

total_biaya = komponen[0] + komponen[1] + komponen[2] + komponen[3] + komponen[4] + komponen[5] + 15000
rata_rata = total_biaya / len(komponen)
nim = 78
bolean = nim != rata_rata
    
poundsterling = total_biaya / 23.788
barang_1_sampai_4 = komponen[-6:-2]

print("Komponen 1 = ",komponen_1)
print("Komponen 2 = ",komponen_2)
print("Komponen 3 = ",komponen_3)
print("Komponen 4 = ",komponen_4)
print("Komponen 5 = ",komponen_5)
print("Komponen 6 = ",komponen_6)

print(komponen)
print("Total biaya adalah = ",total_biaya)
print("Rata rata adalah = ",rata_rata)
print("Nim = ",nim)
print(bolean)
print(f"Hasil konversi total biaya ke Poundsterling adalah = £{poundsterling:.2f}")
print(barang_1_sampai_4)