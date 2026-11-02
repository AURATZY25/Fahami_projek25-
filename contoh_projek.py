print("WARTEG BAHARI")
print("---------------------------------")
print("Kode  Jenis makanan  Harga")
print("---------------------------------")
print("A      Ayam               Rp. 10000")
print("TT     Teh Tawar          Rp. 5000")
print("TM     Teh manis          Rp. 6000")
print("---------------------------------\n")

banyak_jenis = int(input("Banyak Jenis : "))

kode_potong = []
banyak_beli = []
jenis_potong = []
harga_satuan = []
jumlah_harga = []

for i in range(banyak_jenis):
    print(f"Data Ke - {i+1}")
    kp = input("Kode Potong (A/TT/TM) : ").upper()
    bb = int(input("Banyak jenis         : "))
    
    if kp == "A":
        jenis = "Ayam"
        harga = 10000
    elif kp == "TT":
        jenis = "Teh Tawar"
        harga = 5000
    elif kp == "TM":
        jenis = "Teh manis"
        harga = 6000
    else:
        jenis = "Unknown"
        harga = 0
        
    kode_potong.append(kp)
    banyak_beli.append(bb)
    jenis_potong.append(jenis)
    harga_satuan.append(harga)
    jumlah_harga.append(harga * bb)
    print()

print("\n                    WARTEG BAHARI")
print("-------------------------------------------------------------------")
print("No.   Jenis         Harga          Banyak        Jumlah")
print("      Makanan        Satuan         Beli          Harga")
print("-------------------------------------------------------------------")

total_bayar = 0
for i in range(banyak_jenis):
    print(f"{i+1:<5} {jenis_potong[i]:<13} Rp. {harga_satuan[i]:<10} {banyak_beli[i]:<13} Rp. {jumlah_harga[i]}")
    total_bayar += jumlah_harga[i]

pajak = int(total_bayar * 0.1)
total_keseluruhan = total_bayar + pajak

print("-------------------------------------------------------------------")
print(f"                                   Jumlah Bayar  Rp. {total_bayar}")
print(f"                                   Pajak 10%     Rp. {pajak}")
print(f"                                   Total Bayar   Rp. {total_keseluruhan}")