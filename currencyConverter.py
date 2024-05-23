import os

def convert_currency(value, from_currency, to_currency):
    # Dictionary untuk menyimpan nilai tukar mata uang
    rates = {
        "USD": {"EUR": 0.85, "GBP": 0.75},
        "EUR": {"USD": 1.18, "GBP": 0.88},
        "GBP": {"USD": 1.33, "EUR": 1.14},
    }
    
    # Jika mata uang asal sama dengan mata uang tujuan, kembalikan nilai tanpa konversi
    if from_currency == to_currency:
        return value
    # Jika mata uang asal dan tujuan ada dalam rates, hitung nilai konversi
    if from_currency in rates and to_currency in rates[from_currency]:
        return value * rates[from_currency][to_currency]
    else:
        return "Invalid currency"

while True:
    # Membersihkan layar terminal (untuk Windows menggunakan 'cls', untuk MacOS/Linux menggunakan 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')
    print('|| KONVERSI MATA UANG ||\n')
    print('Mata Uang Anda:')
    print('|| 1. USD || 2. EUR || 3. GBP')

    while True:
        try:
            # Meminta pengguna untuk memilih mata uang asal
            currency_choice = int(input("Pilih (1/2/3): "))
            # Memeriksa apakah pilihan valid, jika tidak raise ValueError
            if currency_choice not in [1, 2, 3]:
                raise ValueError("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
            break
        except ValueError as e:
            # Menangkap dan menampilkan pesan error jika terjadi ValueError
            print(f"Error: {e}")
            input("Tekan Enter untuk melanjutkan...")
            continue

    # Menentukan mata uang asal berdasarkan pilihan pengguna
    if currency_choice == 1:
        from_currency = "USD"
    elif currency_choice == 2:
        from_currency = "EUR"
    elif currency_choice == 3:
        from_currency = "GBP"

    while True:
        try:
            # Meminta pengguna untuk memasukkan jumlah mata uang asal
            amount = float(input(f"Masukkan jumlah dalam {from_currency}: "))
            # Memeriksa apakah jumlah melebihi nilai batas, jika iya raise OverflowError
            if amount > 1000:
                raise OverflowError("Jumlah melebihi batas nilai batas yang dapat dihandle.")
            # Memeriksa apakah jumlah positif, jika tidak raise ValueError
            if amount < 0:
                raise ValueError("Jumlah tidak boleh negatif. Silakan masukkan angka positif.")
            break
        except ValueError as e:
            # Menangkap dan menampilkan pesan error jika terjadi ValueError
            print(f"Error: {e}")
            input("Tekan Enter untuk melanjutkan...")
            continue
        except OverflowError as e:
            # Menangkap dan menampilkan pesan error jika terjadi OverflowError
            print(f"Error: {e}")
            input("Tekan Enter untuk melanjutkan...")
            continue

    print('\nKonversi ke:')
    print('|| 1. USD || 2. EUR || 3. GBP')
    
    while True:
        try:
            # Meminta pengguna untuk memilih mata uang tujuan
            target_choice = int(input("Pilih (1/2/3): "))
            # Memeriksa apakah pilihan valid, jika tidak raise ValueError
            if target_choice not in [1, 2, 3]:
                raise ValueError("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
            break
        except ValueError as e:
            # Menangkap dan menampilkan pesan error jika terjadi ValueError
            print(f"Error: {e}")
            input("Tekan Enter untuk melanjutkan...")
            continue

    # Menentukan mata uang tujuan berdasarkan pilihan pengguna
    if target_choice == 1:
        to_currency = "USD"
    elif target_choice == 2:
        to_currency = "EUR"
    elif target_choice == 3:
        to_currency = "GBP"
    
    # Melakukan konversi mata uang
    result = convert_currency(amount, from_currency, to_currency)
    
    # Menampilkan hasil konversi atau pesan error jika terjadi kesalahan
    if isinstance(result, str):
        print(result)
    else:
        print(f"\n{amount} {from_currency} sama dengan {round(result, 2)} {to_currency}")

    # Meminta pengguna apakah ingin melakukan konversi lagi atau tidak
    loop = input("\nIngin melakukan konversi lagi? (y/n): ").lower()
    if loop != 'y':
        break

# Menampilkan pesan terima kasih setelah keluar dari loop
print("Terima kasih telah menggunakan aplikasi konversi mata uang!")
