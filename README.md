<p align="center">
  <img src="assets/logo.png" alt="LOCK_SMITH Logo" width="250"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue" />
  <img src="https://img.shields.io/github/v/release/KalloloCoder/LOCK_SMITH?color=blue&label=version" />
  <img src="https://img.shields.io/github/license/KalloloCoder/LOCK_SMITH" />
  <img src="https://img.shields.io/badge/Maintained-Yes-green" />
  <img src="https://img.shields.io/badge/Open%20Source-Yes-brightgreen" />
  <img src="https://img.shields.io/github/stars/KalloloCoder/LOCK_SMITH?style=social" />
  <img src="https://img.shields.io/github/forks/KalloloCoder/LOCK_SMITH?style=social" />
  <img src="https://img.shields.io/github/issues/KalloloCoder/LOCK_SMITH" />
  <a href="https://github.com/KalloloCoder">
    <img src="https://img.shields.io/badge/Author-KalloloCoder-blue" />
  </a>
</p>

# LOCK_SMITH
LOCK_SMITH adalah aplikasi Password Manager berbasis CLI (Command Line Interface) yang ditulis dengan Python.
Aplikasi ini membantu kamu menyimpan akun, mencari akun, serta membuat 100 password kuat otomatis dengan kombinasi acak.

---

## Fitur Utama

- Tambah akun baru (nama akun, username, password).

- Lihat semua akun yang tersimpan di database.

- Cari akun tertentu berdasarkan nama.

- Generate 100 password kuat berdasarkan kata kunci (keyword).

---

## Instalasi

### 1. Clone repositori ini:
```
git clone https://github.com/KalloloCoder/LOCK_SMITH.git
cd LOCK_SMITH
```

### 2. Buat virtual environment (opsional, tapi disarankan):
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install dependencies:
```
pip install colorama
(install juga Python ≥ 3.12)
```

---

## Cara Menjalankan

### 1. Jalankan script utama:
```
python locksmith.py
```

### 2. Akan muncul menu:

![Tampilan CLI](assets/picture.png)

---

## Struktur File
```
LOCK_SMITH/
└── .github/workflows/
   └── assets/
      ├── picture.png      #Gambar Screenshot
      ├── LICENSE          # Lisensi
      ├── README.md        # Dokumentasi
      ├── locksmith.py     # Main program
      └── passwords.json   # Database akun
```

---

## Author

Created by [KalloloCoder](https://github.com/KalloloCoder)
