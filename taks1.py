def main():
    # Membaca file indata.txt untuk dibaca
    with open('indata.txt', 'r') as file:
        # Membaca semua baris dari file
        lines = file.readlines()

    # variabel untuk menyimpan total jumlah
    total = 0

    # Iterasi melalui setiap baris dalam file
    for line in lines:
        # Konversi setiap baris menjadi bilangan bulat dan tambahkan ke total
        bilangan = int(line.strip())
        total += bilangan

    # Cetak jumlah dengan pemisah koma dan dua digit setelah titik desimal
    total_terformat = '{:.2f}'.format(total)
    print("Total dari bilangan-bilangan adalah:", total_terformat)

if __name__ == "__main__":
    main()
