import json
import os
import random
import string
import time
import sys
from colorama import init, Fore, Style

init(autoreset=True)

DB_FILE = "passwords.json"

def loading(pesan="Loading"):
    for i in range(3):
        sys.stdout.write(f"\r{Fore.YELLOW}{pesan}{'.' * (i+1)}")
        sys.stdout.flush()
        time.sleep(0.5)
    print()

def load_data():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {} 
    return {}

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def tambah_akun(data):
    loading("Menyimpan akun")
    akun = input(Fore.YELLOW + "Masukkan nama akun (misal: Gmail, IG, dll): ")
    username = input(Fore.YELLOW + "Masukkan username: ")
    password = input(Fore.YELLOW + "Masukkan password: ")

    data[akun] = {"username": username, "password": password}
    save_data(data)
    print(Fore.GREEN + f"Akun '{akun}' berhasil disimpan!\n")

def lihat_semua(data):
    loading("Mengambil data akun")
    if not data:
        print(Fore.RED + "Belum ada akun tersimpan.\n")
    else:
        print(Fore.GREEN + "\n=== Daftar Akun Tersimpan ===")
        for akun, info in data.items():
            print(Fore.YELLOW + f"{akun} -> Username: {info['username']} | Password: {info['password']}")
        print()

def cari_akun(data):
    target = input(Fore.YELLOW + "Masukkan nama akun yang dicari: ")
    loading("Mencari akun")
    if target in data:
        info = data[target]
        print(Fore.GREEN + f"\n{target} -> Username: {info['username']} | Password: {info['password']}\n")
    else:
        print(Fore.RED + "Akun tidak ditemukan.\n")

def generate_passwords(keyword, jumlah=100, panjang=12):
    saran = []
    karakter = string.ascii_letters + string.digits + string.punctuation
    for _ in range(jumlah):
        tambahan = "".join(random.choice(karakter) for _ in range(max(1, panjang - len(keyword))))
        password = list(keyword + tambahan)
        random.shuffle(password)
        saran.append("".join(password))
    return saran

def fitur_generate():
    keyword = input(Fore.YELLOW + "Masukkan kata kunci: ")
    loading("Membuat 100 password kuat")
    print(Fore.GREEN + "\n=== 100 Saran Password Kuat ===")
    passwords = generate_passwords(keyword)
    for i, pwd in enumerate(passwords, start=1):
        print(Fore.YELLOW + f"{i}. {pwd}")
    print()

def main():
    data = load_data()

    while True:
        print(Fore.GREEN + "===================================")
        print(Fore.YELLOW + "          LOCK SMITH CLI          ")
        print(Fore.GREEN + "   Made by: KalloloCoder  -  v1.0  ")
        print(Fore.GREEN + "===================================")
        print(Fore.YELLOW + "1. Tambah akun baru")
        print(Fore.YELLOW + "2. Lihat semua akun")
        print(Fore.YELLOW + "3. Cari akun")
        print(Fore.YELLOW + "4. Generate password kuat")
        print(Fore.YELLOW + "5. Keluar")
        print(Fore.GREEN + "===================================")

        pilihan = input(Fore.CYAN + "Pilih menu (1/2/3/4/5): ")

        if pilihan == "1":
            tambah_akun(data)
        elif pilihan == "2":
            lihat_semua(data)
        elif pilihan == "3":
            cari_akun(data)
        elif pilihan == "4":
            fitur_generate()
        elif pilihan == "5":
            loading("Menyimpan dan keluar")
            print(Fore.GREEN + "Keluar... data aman tersimpan (⁠◔⁠‿⁠◔⁠)")
            break
        else:
            print(Fore.RED + "Pilihan tidak valid!\n")

if __name__ == "__main__":
    main()
