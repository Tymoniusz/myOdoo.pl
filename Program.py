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

def tylkocyfry(*a):
    global tx,pop_s
    s= tx.get()
    if s == "" or s.isdigit():
        pop_s = s
    else:
        tx.set(pop_s)

def start():
    global tx
    Ok = False
    wyjscie = tx.get()
    messagebox.showinfo("Sukces",wyjscie)

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
