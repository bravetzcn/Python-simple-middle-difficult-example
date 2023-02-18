import tkinter as tk
from playsound import playsound

def donot(event=None):
    playsound('nota-do.wav',True)

def renot(event=None):
    playsound('nota-re.wav',True)

def minot(event=None):
    playsound('nota-mi.wav',True)
def fanot(event=None):
    playsound('nota-fa.wav',True )

def solnot(event=None):
    playsound('nota-sol.wav',True )

def lanot(event=None):
    playsound('nota-lya.wav',True)

def sinot(event=None):
    playsound('nota-si.wav', True)

def otonot(event=None):
    f= open('nota.txt')
    s=f.readline()
    def notlar(i):
        if i<len(s):
            satir=s[i].split()
            def nota (j):
                if satir[j].lower()=='do' :
                    donot()
                if satir[j].lower() == 're':
                    renot()

                if satir[j].lower() == 'mi':
                    minot()

                if satir[j].lower() == 'fa':
                    fanot()

                if satir[j].lower() == 'sol':
                    solnot()
                j=j+1
                pencere.after(200,lambda:nota(j))

        i = i+1
        pencere.after(200*len(satir)+1000,lambda: notlar(i))
    notlar(0)
pencere=tk.Tk()
pencere.title("piyona")
pencere.geometry('520x400')
b1=tk.Button(pencere,text="DO",font="Verdana 14 bold",bg="white",fg="black",width=3, height=10, command=donot)
b1.place(x=50,y=20)

b2=tk.Button(pencere,text="RE",font="Verdana 14 bold",bg="white",fg="black",width=3, height=10, command=renot)
b2.place(x=110,y=20)

b3=tk.Button(pencere,text="Mİ",font="Verdana 14 bold",bg="white",fg="black",width=3, height=10, command=minot)
b3.place(x=170,y=20)

b4=tk.Button(pencere,text="FA",font="Verdana 14 bold",bg="white",fg="black",width=3, height=10, command=fanot)
b4.place(x=230,y=20)

b5=tk.Button(pencere,text="SOL",font="Verdana 14 bold",bg="white",fg="black",width=3, height=10, command=solnot)
b5.place(x=290,y=20)

b6=tk.Button(pencere,text="LA",font="Verdana 14 bold",bg="white",fg="black",width=3, height=10, command=lanot)
b6.place(x=350,y=20)

b7=tk.Button(pencere,text="Sİ",font="Verdana 14 bold",bg="white",fg="black",width=3, height=10, command=sinot)
b7.place(x=410,y=20)

b7=tk.Button(pencere,text="OTOMATİK",font="Verdana 14 bold",bg="white",fg="black",width=10, height=1, command=otonot)
b7.place(x=200,y=300)

pencere.bind("<a>",donot)
pencere.bind("<s>",renot)
pencere.bind("<d>",minot)
pencere.bind("<f>",fanot)
pencere.bind("<g>",solnot)
pencere.bind("<h>",lanot)
pencere.bind("<j>",sinot)



pencere.mainloop()
