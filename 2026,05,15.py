'''
from tkinter import *
root= Tk()
mainMenu= Menu(root)
root.config(menu=mainMenu)
fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label= '파일', menu=fileMenu)
fileMenu.add_command(label='열기')
fileMenu.add_separator()
fileMenu.add_command(label='종료')

root.mainloop()
'''
'''
from tkinter import *
from tkinter.filedialog import *
window=Tk()
window.geometry('400x100')
label1=Label(window, text='선택된 파일 이름')
label1.pack()

filename= askopenfilename(parent=window, filetypes=(('GIF파일', '*gif'),('모든 파일','*')))

label1.configure(text=str(filename))
window.mainloop()
'''
'''
import tkinter as tk

def say_hello():
    name=entry.get()
    label.config(text='Hello, {}'.format(name))
    
root= tk.Tk()

entry=tk.Entry(root)
entry.pack()

button= tk.Button(root, text='Click Me', command=say_hello)
button.pack()
label= tk.Label(root, text='No Input')
label.pack()
                

root.mainloop()
'''
'''
import tkinter as tk

def add():
    result=int(entry1.get())+int(entry2.get())
    label.config(text=f'Result:{result}')

root=tk.Tk()
entry1=tk.Entry(root)
entry1.pack()
entry2=tk.Entry(root)
entry2.pack()
button=tk.Button(root, text='Add', command=add)
button.pack()
label=tk.Label(root,text='')
label.pack()
root.mainloop()
'''
'''
import tkinter as tk
def show_fruit(event):
    selection=listbox.get(listbox.curselection())
    label.config(text=f'Selected:{selection}')

root=tk.Tk()
listbox=tk.Listbox(root)
for fruit in['Apple', 'Banana','Cherry']:
    listbox.insert(tk.END, fruit)
listbox.pack()
listbox.bind('<<ListboxSelect>>',show_fruit)
label= tk.Label(root,text='')
label.pack()
root.mainloop()
'''
'''
import tkinter as tk

def save_file():
    with open('note.txt','w')as f:
        f.write(text.get('1.0',tk.END))
        
root=tk.Tk()

text=tk.Text(root)
text.pack()

button=tk.Button(root, text='Save',command=save_file)
button.pack()

root.mainloop()
'''
'''
import tkinter as tk
import time

def update_time():
    current=time.strftime('%H:%M:%S')
    label.config(text=current)
    root.after(1000, update_time)

root=tk.Tk()
label=tk.Label(root, font=('Arial', 24))
label.pack()
update_time()

root.mainloop()
'''

class Counter:
    total_clicks=0

    def __init__(self, start=0):
        self.value=start

    def incrememt(self):
        self.value+=1
        
    def decrement(self):
        self.value-=1
        if(self.value<0):
            self.value=0
    def reset(self):
        self.value=1

def update_label():
    label.config(text=f'현재 값:{counter.value}')
    pass
def on_plus():
    cointer.increment()
    update_label()

def on_minus():
    counter.increment()
    update_label()

def on_reset():
    counter.reset()
    update_label()


counter = Counter(start=0)

window = Tk()
window.title("연습 1 - Counter 클래스 + GUI")
window.geometry("360x150")

label = Label(window, text="", font=("맑은 고딕", 14))
label.pack(pady=10)

btn_plus  = Button(window, text="+", width=6, command=on_plus)
btn_minus = Button(window, text="-", width=6, command=on_minus)
btn_reset = Button(window, text="Reset", width=8, command=on_reset)

btn_plus.pack(side=LEFT,  padx=10, pady=10)
btn_minus.pack(side=LEFT, padx=10, pady=10)
btn_reset.pack(side=LEFT, padx=10, pady=10)

update_label()
window.mainloop()



        
