#import modules
from tkinter import*
# from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import*

# buat objek root dari class Tk
root = ttk.Window(themename="vapor")

# Atur title
root.title("Aplikasi Tabel Perkalian")

# Atur Lebar dan Tinggi Tampilan
root.geometry('500x500')

# Buat judul
Button(root,text="Aplikasi Penampil Perkalian",font=("Times New Roman",25) ).pack(pady=10)
# buat teks inputan
Label(root,text="Masukkan Angka:", font=("Times New Roman",15)).pack(pady=10)
number = StringVar()
Entry(root,textvariable=number, width=10,font=("Times New Roman",15)).pack(pady=10)

# function untuk menampilkan
def table():
    n = number.get()
    stext.delete(1.0, END)
    for i in range(1,11):
        tab = int(n)*i 
        result = f"{n} x {i} = {tab}\n"
        stext.insert(END, result, "center")
    

# buat button tampilkan
Button(root,text="Tampilkan Perkalian", command=table,font=("Times New Roman",15),).pack(pady=10)
stext = Text(root,font=("Times New Roman",15))
stext.tag_configure("center", justify="center")

# Jalankan Aplikasi
stext.pack(side="top", fill="both", expand=True)
root.mainloop()