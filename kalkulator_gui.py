import tkinter as tk
from tkinter import messagebox

def klik_tombol(angka):
    entri_layar.insert(tk.END, angka)

def hapus():
    entri_layar.delete(0, tk.END)

def hapus_satu():
    teks = entri_layar.get()
    entri_layar.delete(0, tk.END)
    entri_layar.insert(0, teks[:-1])

def hitung():
    try:
        hasil = eval(entri_layar.get())
        entri_layar.delete(0, tk.END)
        entri_layar.insert(tk.END, str(hasil))
    except Exception as e:
        messagebox.showerror("Error", "Input tidak valid")

# Membuat jendela utama
jendela = tk.Tk()
jendela.title("Kalkulator Sederhana")
jendela.geometry("350x500")
jendela.configure(bg="#2C3E50")

# Membuat layar entri
entri_layar = tk.Entry(jendela, font=("Arial", 24), bd=10, insertwidth=2, width=15, borderwidth=4, justify='right')
entri_layar.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Warna tombol
warna_tombol = {
    'angka': "#34495E",
    'operasi': "#E67E22",
    'hapus': "#E74C3C",
    'hitung': "#2ECC71"
}

# Membuat tombol angka dan operasi
angka = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3),
]

for (teks, baris, kolom) in angka:
    warna = warna_tombol['angka'] if teks not in ['C', '/', '*', '-', '+'] else warna_tombol['operasi']
    if teks == 'C':
        warna = warna_tombol['hapus']
    tk.Button(jendela, text=teks, padx=20, pady=20, font=("Arial", 16), bg=warna, fg="white", borderwidth=0, command=lambda t=teks: klik_tombol(t) if t != 'C' else hapus()).grid(row=baris, column=kolom, padx=5, pady=5, sticky="nsew")

# Tombol untuk menghapus satu karakter
tk.Button(jendela, text="⌫", padx=20, pady=20, font=("Arial", 16), bg="#E74C3C", fg="white", borderwidth=0, command=hapus_satu).grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

# Tombol untuk menghitung
tk.Button(jendela, text="=", padx=20, pady=20, font=("Arial", 16), bg=warna_tombol['hitung'], fg="white", borderwidth=0, command=hitung).grid(row=5, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

# Membuat grid responsif
for i in range(6):
    jendela.grid_rowconfigure(i, weight=1)
for i in range(4):
    jendela.grid_columnconfigure(i, weight=1)

# Menjalankan aplikasi
jendela.mainloop()
