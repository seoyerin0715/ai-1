'''
from tkinter import *
window=Tk()
window.mainloop()
#GUI 코딩에 반드시 필요한 3줄. 기말시험예상
'''
'''
from tkinter import *
window=Tk()
window.title('윈도창 연습')
window.geometry('400x100')
window.resizable(width = FALSE, height = FALSE)
window.mainloop()
'''
'''
from tkinter import *
window=Tk()

label1= Label(window, text = 'COOKBOOK~~ Python을')
label2= Label(window, text = '열심히', font =  ('궁서체',30), fg = 'blue')
label3= Label(window, text = '공부 중입니다,', bg = 'magenta', width=20, height=5, anchor= SE)
label1.pack()
label2.pack()
label3.pack()
window.mainloop()
'''
'''
from tkinter import *
window=Tk()
photo1= PhotoImage(file='dailyfina-bouquet-26261.gif')
photo2= PhotoImage(file='mxjfiles-sky-26732.gif')
label1=Label(window, imag=photo1)
label2=Label(window, imag=photo2)
label1.pack(side=LEFT)
label2.pack(side=RIGHT)
window.mainloop()
'''
'''
from tkinter import *
window=Tk()
photo1= PhotoImage(file='dailyfina-bouquet-26261.gif')
button1= Button(window, imag=photo1, command=quit)
button1.pack()
window.mainloop()
'''
'''
from tkinter import *
from tkinter import messagebox

def myFunc():
    messagebox.showinfo('꽃다발 버튼', '꽃다발 보소')
    
window=Tk()

photo=PhotoImage(file='dailyfina-bouquet-26261.gif')
button1=Button(window, imag=photo, command=myFunc)

button1.pack()
window.mainloop()
'''
'''
from tkinter import *
from tkinter import messagebox
window=Tk()

def myFunc():
    if chk.get()==0:
        messagebox.showinfo("","체크버튼이 꺼졌어요.")
    else:
        messagebox.showinfo("","체크버튼이 켜졌어요.")

chk=IntVar()
cb1=Checkbutton(window, text='클릭하세요',variable=chk, command= myFunc)
cb1.pack()

window.mainloop()
'''
'''
from tkinter import *
window=Tk()

def myFunc():
    if var.get()==1:
        label1.configure(text='파이썬')
    elif var.get()==2:
        label1.configure(text='C++')
    else:
        label1.configure(text='Java')

var=IntVar()
rb1=Radiobutton(window, text='파이썬',variable=var, value=1, command= myFunc)
rb2=Radiobutton(window, text='C++',variable=var, value=2, command= myFunc)
rb3=Radiobutton(window, text='Java',variable=var, value=3, command= myFunc)

label1= Label(window, text='선택한 언어:', fg='red')

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()
window.mainloop()
'''
'''
from tkinter import *

btnList=[None]*9
photoList=[None]*9
i,k=0,0
xPos, yPos=0,0
num=0

window=Tk()
window.geometry('210x210')

for i in range(0,9):
    photoList[i]=PhotoImage(file='dailyfina-bouquet-26261.gif')
    btnList[i]=Button(window, imag=photoList[i])

for i in range(0,3):
    for k in range(0,3):
        btnList[num].place(x=xPos, y=yPos)
        num += 1
        xPos += 70

    xPos = 0
    yPos += 70
    
window.mainloop()
'''

from tkinter import *
from tkinter import messagebox

def clickLeft(event):
    messagebox.showinfo('마우스','마우스 왼쪽 버튼이 클릭됨')

window=Tk()

window.bind('<Button-1>', clickLeft)

window.mainloop()
