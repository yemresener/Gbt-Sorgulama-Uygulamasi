
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import messagebox
from tkinter import *
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from tkinter import ttk
import mysql.connector



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"image\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def login_msgbox(hata_kodu,mesaj_text,icon,pencere):
    mesaj = tk.Toplevel(pencere)

    mesaj.title(hata_kodu)
    mesaj.geometry("300x100")

    l1 = tk.Label(mesaj, image="::tk::icons::"+icon)
    l1.grid(row=0, column=0, pady=(7, 0), padx=(10, 30), sticky="e")
    l2 = tk.Label(mesaj, text=mesaj_text)
    l2.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")

    b1 = Button(mesaj, text="Tamam", command=mesaj.destroy, width=10)
    b1.grid(row=1, column=1, padx=(2, 35), sticky="e")


    mesaj.update_idletasks()
    x = pencere.winfo_rootx() + (pencere.winfo_width() - mesaj.winfo_width()) // 2
    y = pencere.winfo_rooty() + (pencere.winfo_height() - mesaj.winfo_height()) // 2
    mesaj.geometry(f"300x100+{x}+{y}")




window = Tk()

window.geometry("500x500")
window.configure(bg="#A0B2B0")
window.title("GBT")






class Uygulama():
    def __init__(self):
        self.giris_paneli()


        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python_araba"
    )

    def veritabani(self):

        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="python_gbt"
            )


##################################  GİRİŞ PENCERESİ ve FONKSİYONLARI  #####################################
    def giris_paneli(self):

        self.canvas = Canvas(
            window,
            bg="#011026",
            height=500,
            width=500,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)


        self.canvas.create_text(
            33.0,
            19.0,
            anchor="nw",
            text="   İSTANBUL EMNİYET MÜDÜRLÜĞÜ",
            fill="RED",
            font=("JetBrainsMonoRoman ExtraBold", 25 * -1)
        )

        self.tc_resim = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.tc_bg = self.canvas.create_image(
            130.0,
            135.5,
            image=self.tc_resim
        )
        self.tc = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.tc.place(
            x=49.0,
            y=119.0,
            width=162.0,
            height=33.0
        )

        self.sifre_resim = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.sifre_bg = self.canvas.create_image(
            130.0,
            207.5,
            image=self.sifre_resim
        )
        self.sifre = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.sifre.place(
            x=49.0,
            y=190.0,
            width=162.0,
            height=35.0
        )

        self.dogrulama_resim = PhotoImage(
            file=relative_to_assets("re.png"))
        self.dogrulama_bg = self.canvas.create_image(
            130.0,
            276.5,
            image=self.dogrulama_resim
        )
        self.dogrulama = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.dogrulama.place(
            x=49.0,
            y=261.0,
            width=162.0,
            height=35.0
        )
        self.email_text = self.canvas.create_text(
            33.0,
            93.0,
            anchor="nw",
            text="Kimlik numarası:",
            fill="#FFFFFF",
            font=("KumbhSans Bold", 15 * -1)
        )
        self.numara_text = self.canvas.create_text(
            33.0,
            165.0,
            anchor="nw",
            text="Şifre:",
            fill="#FFFFFF",
            font=("KumbhSans Bold", 15 * -1)
        )
        self.sifre_text = self.canvas.create_text(
            33.0,
            237.0,
            anchor="nw",
            text="Doğrulama:",
            fill="#FFFFFF",
            font=("KumbhSans Bold", 15 * -1)
        )
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.giris ,
            relief="flat"
        )
        self.button_2.place(
            x=33.0,
            y=330.0,
            width=77.643829345703125,
            height=34.0,

        )



        window.resizable(False, False)
        window.mainloop()


    def giris(self):
            self.veritabani()
            self.true_kullanici_adi = self.tc.get()
            self.true_sifre = self.sifre.get()
            self.true_dogrulama=self.dogrulama.get()

            self.sql_giris = "Select * FROM polisler where tc = '" + self.true_kullanici_adi + "'" + "and sifre = '" + self.true_sifre + "'" + "and dogrulama = '"+self.true_dogrulama + "'"
            self.mycursor = self.mydb.cursor()
            self.mycursor.execute(self.sql_giris)
            self.myresult = self.mycursor.fetchone()
            self.myresult2 = self.mycursor.fetchone()


            if self.myresult!=None:
                window.destroy()
                self.kullanici_pencere()


            else:
                login_msgbox("HATA!","HATALI GİRİŞ! ","warning",window)

##################################  ANA PENCERE ve FONKSİYONLARI  #####################################

    def veri_aktarimi(self):
        self.sql_veri_aktarimi=f"select * from suc"
        self.my_cursor = self.mydb.cursor()
        self.my_cursor.execute(self.sql_veri_aktarimi)
        self.rows=self.my_cursor.fetchall()
        if len(self.rows)!=0:
            self.halk_tablo1.delete(*self.halk_tablo1.get_children())
            for i in self.rows:
                self.halk_tablo1.insert("",END,values=i)
            self.mydb.commit()

    def veri_aktarimi1(self):
        self.veritabani()
        self.sql_veri_aktarimi1="select*from halk"
        self.my_cursor1 = self.mydb.cursor()
        self.my_cursor1.execute(self.sql_veri_aktarimi1)
        self.rows1=self.my_cursor1.fetchall()
        if len(self.rows1)!=0:
            self.halk_tablo.delete(*self.halk_tablo.get_children())
            for i in self.rows1:
                self.halk_tablo.insert("",END,values=i)
            self.mydb.commit()

    def kullanici_pencere(self):

        self.kullanici_window = Tk()

        self.kullanici_window.geometry("1100x800")
        self.kullanici_window.configure(bg="#FFFFFF")
        self.kullanici_window.title("İSTANBUL EMNİYET MÜDÜRLÜĞÜ")

        self.kullanici_window_canvas = Canvas(
            self.kullanici_window,
            bg="#FFFFFF",
            height=800,
            width=1100,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.kullanici_window_canvas.place(x=0, y=0)
        self.kullanici_photo = PhotoImage(
            file=relative_to_assets("gbt1.png"))
        self.kullanici_image_1 = self.kullanici_window_canvas.create_image(
                250.0,
                500.0,
                image=self.kullanici_photo
            )

        self.kullanici_window_canvas.create_text(
            182.0,
            5.0,
            anchor="nw",
            text="               GBT SORGULAMA SİSTEMİ",
            fill="RED",
            font=("KumarOne Regular", 30 * -1)
        )




        self.table_frame1 = Frame(self.kullanici_window, bd=10, relief=RIDGE, bg="Green")
        self.table_frame1.place(x=550, y=40, width=550, height=380)

        self.scroll_x1 = ttk.Scrollbar(self.table_frame1, orient=HORIZONTAL)
        self.scroll_y1 = ttk.Scrollbar(self.table_frame1, orient=VERTICAL)
        self.halk_tablo = ttk.Treeview(self.table_frame1, columns=("tc", "isim", "tarih", "yer",
                                                                  "ana", "baba"),
                                       xscrollcommand=self.scroll_x1.set, yscrollcommand=self.scroll_y1.set)

        self.scroll_x1.pack(side=BOTTOM, fill=X)
        self.scroll_y1.pack(side=RIGHT, fill=Y)

        self.scroll_x1.config(command=self.halk_tablo.xview)
        self.scroll_y1.config(command=self.halk_tablo.yview)

        self.halk_tablo.heading("tc", text="T.C", anchor=W)
        self.halk_tablo.heading("isim", text="AD-SOYAD", anchor=W)
        self.halk_tablo.heading("tarih", text="D.Tarihi", anchor=W)
        self.halk_tablo.heading("yer", text="D.Yeri", anchor=W)
        self.halk_tablo.heading("ana", text="Anne adı", anchor=W)
        self.halk_tablo.heading("baba", text="Baba adı", anchor=W)

        self.halk_tablo.column("tc", width=75)
        self.halk_tablo.column("isim", width=75)
        self.halk_tablo.column("tarih", width=65)
        self.halk_tablo.column("yer", width=60)
        self.halk_tablo.column("ana", width=80)
        self.halk_tablo.column("baba", width=90)

        self.veri_aktarimi1()

        self.halk_tablo["show"] = "headings"
        self.halk_tablo.pack(fill=BOTH, expand=1)

############           SUÇ TABLOSU


        self.table_frame2 = Frame(self.kullanici_window, bd=10, relief=RIDGE, bg="green")
        self.table_frame2.place(x=550, y=410, width=550, height=380)

        self.scroll_x2 = ttk.Scrollbar(self.table_frame2, orient=HORIZONTAL)
        self.scroll_y2 = ttk.Scrollbar(self.table_frame2, orient=VERTICAL)
        self.halk_tablo1 = ttk.Treeview(self.table_frame2, columns=("tc", "suc", "suc yeri", "tarih",
                                                                  "ceza", "arama"),
                                       xscrollcommand=self.scroll_x2.set, yscrollcommand=self.scroll_y2.set)

        self.scroll_x2.pack(side=BOTTOM, fill=X)
        self.scroll_y2.pack(side=RIGHT, fill=Y)

        self.scroll_x2.config(command=self.halk_tablo1.xview)
        self.scroll_y2.config(command=self.halk_tablo1.yview)

        self.halk_tablo1.heading("tc", text="T.C", anchor=W)
        self.halk_tablo1.heading("suc", text="SUÇU", anchor=W)
        self.halk_tablo1.heading("suc yeri", text="SUÇ YERİ", anchor=W)
        self.halk_tablo1.heading("tarih", text="SUÇ TARİH", anchor=W)
        self.halk_tablo1.heading("ceza", text="CEZA", anchor=W)
        self.halk_tablo1.heading("arama", text="ARANMA", anchor=W)

        self.halk_tablo1.column("tc", width=75)
        self.halk_tablo1.column("suc", width=85)
        self.halk_tablo1.column("suc yeri", width=95)
        self.halk_tablo1.column("tarih", width=70)
        self.halk_tablo1.column("ceza", width=80)
        self.halk_tablo1.column("arama", width=90)

        self.veri_aktarimi()

        self.halk_tablo1["show"] = "headings"
        self.halk_tablo1.pack(fill=BOTH, expand=1)


########### TABLODA ARAMA ENTRY'Sİ


        self.arama_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.arama_entry.place(
            x=49.0,
            y=190.0,
            width=162.0,
            height=35.0
        )



        self.kirala_buton_image = PhotoImage(
            file=relative_to_assets("kirala.png"))
        self.kirala_buton = Button(
            image=self.kirala_buton_image,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command = self.kayit_bilgi
        )
        self.kirala_buton.place(
            x=248.0,
            y=280.0,
            width=98.0,
            height=44.0
        )


        self.kullanici_window.resizable(False, False)
        self.kullanici_window.mainloop()


    def kayit_bilgi(self):
########### KAYIT BİLGİLERİNİ TABLOYA GETİRTME ###########
        self.halk_tablo.delete(*self.halk_tablo.get_children())

        self.halk_tablo1.delete(*self.halk_tablo1.get_children())

        self.arama=self.arama_entry.get()

        self.veritabani()
        # Veriyi güncel Treeview'a aktar
        self.kayit_sql_sorgu = f"SELECT*from halk where tc={self.arama}"
        self.kayit_sql_sorgu1 = f"SELECT*from suc where tc={self.arama}"

        self.my_cursor1 = self.mydb.cursor()
        self.my_cursor1.execute(self.kayit_sql_sorgu)
        self.rows1 = self.my_cursor1.fetchall()

        self.my_cursor2 = self.mydb.cursor()
        self.my_cursor2.execute(self.kayit_sql_sorgu1)
        self.rows2 = self.my_cursor2.fetchall()


        if len(self.rows1) != 0 and len(self.rows2)!=0:
            self.halk_tablo.delete(*self.halk_tablo.get_children())
            for i in self.rows1:
                self.halk_tablo.insert("", END, values=i)
            self.mydb.commit()

            self.halk_tablo1.delete(*self.halk_tablo1.get_children())
            for i in self.rows2:
                self.halk_tablo1.insert("", END, values=i)
            self.mydb.commit()








app=Uygulama()