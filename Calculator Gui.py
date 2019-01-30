from tkinter import *

def clean():
    txt.delete(0,END)

def insert1():
    txt.insert(END,1)
def insert2():
    txt.insert(END,2)
def insert3():
    txt.insert(END,3)
def insert4():
    txt.insert(END,4)
def insert5():
    txt.insert(END,5)
def insert6():
    txt.insert(END,6)
def insert7():
    txt.insert(END,7)
def insert8():
    txt.insert(END,8)
def insert9():
    txt.insert(END,9)
def insert0():
    txt.insert(END,0)

def insertplus():
    txt.insert(END,'+')
def insertminus():
    txt.insert(END,'-')
def insertdiv():
    txt.insert(END,'/')
def insertmult():
    txt.insert(END,'*')
def insertpar1():
    txt.insert(END,'(')
def insertpar2():
    txt.insert(END,')')
def insertdot():
    txt.insert(END,'.')

def commands():
    a=txt.get()
    b=str(eval(a))
    txt.delete(0,END)
    txt.insert(END,b)

def back():
    x=txt.get()
    y=x/10
    
    
    
#Main window
window=Tk()
window.geometry('530x500')
window.title('Calculator')
window.configure(bg='red')

#Display box
txt=Entry(window,width=18,font='Helvetica 40')
txt.place(x=0,y=0)

#Reset Button
reset=Button(window,text='C',height=3,width=10,command=clean)
reset.place(x=390,y=100)

#Number buttons
b1=Button(window,text='1',height=3,width=10,command=insert1)
b1.place(x=20,y=100)

b2=Button(window,text='2',height=3,width=10,command=insert2)
b2.place(x=120,y=100)

b3=Button(window,text='3',height=3,width=10,command=insert3)
b3.place(x=220,y=100)

b4=Button(window,text='4',height=3,width=10,command=insert4)
b4.place(x=20,y=170)

b5=Button(window,text='5',height=3,width=10,command=insert5)
b5.place(x=120,y=170)

b6=Button(window,text='6',height=3,width=10,command=insert6)
b6.place(x=220,y=170)

b7=Button(window,text='7',height=3,width=10,command=insert7)
b7.place(x=20,y=240)

b8=Button(window,text='8',height=3,width=10,command=insert8)
b8.place(x=120,y=240)

b9=Button(window,text='9',height=3,width=10,command=insert9)
b9.place(x=220,y=240)

b0=Button(window,text='0',height=3,width=10,command=insert0)
b0.place(x=20,y=310)

#Operators button
plus=Button(window,text='+',height=2,width=8,font='30',command=insertplus)
plus.place(x=390,y=170)

minus=Button(window,text='-',height=2,width=8,font='30',command=insertminus)
minus.place(x=390,y=240)

mult=Button(window,text='*',height=2,width=8,font='30',command=insertmult)
mult.place(x=390,y=310)

div=Button(window,text='/',height=2,width=8,font='30',command=insertdiv)
div.place(x=390,y=380)

par1=Button(window,text='(',height=2,width=8,font='30',command=insertpar1)
par1.place(x=20,y=400)

par2=Button(window,text=')',height=2,width=8,font='30',command=insertpar2)
par2.place(x=120,y=400)

dot=Button(window,text='.',height=2,width=8,font='30',command=insertdot)
dot.place(x=220,y=400)


#Equal to button
eq=Button(window,text='=',height=3,width=8,font='30',command=commands)
eq.place(x=220,y=310)
