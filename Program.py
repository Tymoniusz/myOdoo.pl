## Program Brutton
## Autor : Tymoniusz

## Wytyczne: Aplikacja wpisuje u siebie kwote brutto, na kalkulator wynagrodzeń
## Zwraca kwote netto do programu
## (dodatkowe) Wykres zależności między brutto (oś x) a netto (oś y)

##a. kwoty brutto podawane są jako argumenty aplikacji. Użyj minimum 6 wartości brutto (pętle, użycie pakietu sys, listy).

##b. kwoty netto wylicz na podstawie witryny https://wynagrodzenia.pl/   (umiejętność korzystania z pakietów komunikujących się z serwerami www, obiektowość, obsługa błędów).

##c. stwórz wykres (obiektowość, podstawy pakietów do rysowania).

from tkinter import *
from tkinter import messagebox
import tkinter as tk

##import socket,sys To jest odpowiedź, ale jak? 


def tylkocyfry(*a):
    global tx,pop_s
    s= tx.get()
    if s == "" or s.isdigit():
        pop_s = s
    else:
        tx.set(pop_s)

def start():
    global tx
    wyjscie = tx.get()
    liczba = float(wyjscie)
    zmienna = 0.79889
    messagebox.showinfo("Sukces",liczba* zmienna)
    x = 360 * zmienna
    y = 360 - x

    ok = tk.Tk()
    ok.title("Wykres")
    c = Canvas(ok, width=400, height=400, bg='white')
    c.create_text(280,160,text=("Brutto "+ str(int(liczba-(liczba*zmienna)))+"zł"),font=("Arial","10","bold"),justify=CENTER,fill='grey')
    c.create_text(160,160,text=("Netto "+ str(int(liczba*zmienna))+"zł"),font=("Arial","10","bold"),justify=CENTER,fill='grey')
    c.create_arc(10,10,380,380,outline='black',width=5,style=PIESLICE,start=0,extent=y)
    c.create_arc(10,10,380,380,outline='red',width=5,style=ARC,start=0,extent=359)
    b = Button(ok, text="Zamknij", command=ok.destroy)
    c.grid(row=0)
    b.grid(row=1)
    ok.mainloop()

    

o = tk.Tk()
o.geometry("310x50")
o.title("Brutton")


tk.Label(o, text="Kwota brutto (zł):").grid(row=0, column=0)

tx = StringVar()
pop_s = "" #moduł do wpisania samych cyfr
tx.set(pop_s)
tx.trace("w", tylkocyfry)


tk.Entry(o,width=30, textvariable=tx).grid(row=0, column=1)
tk.Button(o, text="Ok", command=start).grid(row=0, column=2)

dana= ""


o.mainloop()
