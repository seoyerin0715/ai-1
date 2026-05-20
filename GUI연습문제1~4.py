'''
from tkinter import *
class Counter:
    total_clicks=0

    def __init__(self, start=0):
        self.value= start

    def increment(self):
        self.value += 1
        Counter.total_clicks += 1

    def decrement(self):
        self.value -= 1
        Counter.total_clicks += 1

    def reset(self):
        self.value=0

def update_label():
    label.config(text=f"현재값:{counter.value}/총 클릭수:{Counter.total_clicks}")

def on_plus():
    counter.increment()
    update_label()

def on_minus():
    counter.decrement()
    update_label()

def on_reset():
    counter.reset()
    update_label()

counter= Counter(start=0)

window=Tk()
window.title("연습 1 - Counter 클래스 + GUI")
window.geometry("360x150")

label=Label(window,text="", font=("맑은 고딕",14))
label.pack(pady=10)

btn_plus  = Button(window, text="+", width=6, command=on_plus)
btn_minus = Button(window, text="-", width=6, command=on_minus)
btn_reset = Button(window, text="Reset", width=8, command=on_reset)

btn_plus.pack(side=LEFT,  padx=10, pady=10)
btn_minus.pack(side=LEFT, padx=10, pady=10)
btn_reset.pack(side=LEFT, padx=10, pady=10)

update_label()
window.mainloop()
'''
'''
from tkinter import *
from tkinter import messagebox

class BankAccount:
    num_accounts=0

    def __init__(self, owner, balance=0):
        self.owner=owner
        self.balance=balance
        BankAccount.num_accounts += 1

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("입금액은 양수여야 합니다")
        self.balance += amount
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("출금액은 양수여야 합니다")
        if amount > self.balance:
            raise ValueError(f"잔액 부족: 현재 {self.balance:,}원")
        self.balance -= amount

    def get_balance(self):
        return self.balance

def parse_amount():
    text= entry.get().strip()
    try:
        return int(text)
    except ValueError:
        messagebox.showerror("입력 오류", "금액은 정수로 입력해 주세요.")
        return None
    
 
def update_label():
    label.config(
        text=f"소유주: {account.owner}\n잔액: {account.get_balance():,} 원"
        f"\n생성된 계좌 수: {BankAccount.num_accounts}")


def on_deposit():
    amount = parse_amount()
    if amount is None:
        return
    try:
        account.deposit(amount)
    except ValueError as e:
        messagebox.showerror("입금 오류", str(e))
        return
    update_label()

def on_withdraw():
    amount = parse_amount()
    if amount is None:
        return
    try:
        account.withdraw(amount)
    except ValueError as e:
        messagebox.showerror("출금 오류", str(e))
        return
    update_label()

account = BankAccount("홍길동", balance=10000)

window = Tk()
window.title("연습 2 - BankAccount + GUI")
window.geometry("360x220")

label = Label(window, text="", font=("맑은 고딕", 12), justify=LEFT)
label.pack(pady=10)

entry = Entry(window, width=15, justify="right")
entry.pack(pady=5)

frm = Frame(window)
frm.pack(pady=5)
Button(frm, text="입금", width=8, command=on_deposit).pack(side=LEFT, padx=5)
Button(frm, text="출금", width=8, command=on_withdraw).pack(side=LEFT, padx=5)

update_label()
window.mainloop()
'''
'''
from tkinter import *
import random

def random_color():
    return "#%02x%02x%02x" % (random.randint(0, 255),
                              random.randint(0, 255),
                              random.randint(0, 255))


class Shape:
    def __init__(self, canvas, x, y, color=None):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color if color is not None else random_color()

    def draw(self):
        raise NotImplementedError("Shape.draw() 를 override 하세요.")


class Circle(Shape):
    def __init__(self, canvas, x, y, r=30, color=None):
        super().__init__(canvas, x, y, color)
        self.r = r

    def draw(self):
        x, y, r = self.x, self.y, self.r
        self.canvas.create_oval(x - r, y - r, x + r, y + r,
                                fill=self.color, outline="")


class Rectangle(Shape):
    def __init__(self, canvas, x, y, w=60, h=40, color=None):
        super().__init__(canvas, x, y, color)
        self.w = w
        self.h = h

    def draw(self):
        x, y, w, h = self.x, self.y, self.w, self.h
        self.canvas.create_rectangle(x - w / 2, y - h / 2,
                                     x + w / 2, y + h / 2,
                                     fill=self.color, outline="")


class Triangle(Shape):
    def __init__(self, canvas, x, y, size=40, color=None):
        super().__init__(canvas, x, y, color)
        self.size = size

    def draw(self):
        x, y, s = self.x, self.y, self.size
        p1 = (x, y - s)
        p2 = (x - s, y + s * 0.7)
        p3 = (x + s, y + s * 0.7)
        self.canvas.create_polygon(p1, p2, p3,
                                   fill=self.color, outline="")


def on_canvas_click(event):
    kind = shape_var.get()
    if kind == 1:
        shape = Circle(canvas, event.x, event.y)
    elif kind == 2:
        shape = Rectangle(canvas, event.x, event.y)
    else:
        shape = Triangle(canvas, event.x, event.y)
    shape.draw()


def on_clear():
    canvas.delete("all")


window = Tk()
window.title("연습 3 - Shape 상속 + Canvas")
window.geometry("520x460")

shape_var = IntVar(value=1)

frm_top = Frame(window)
frm_top.pack(side=TOP, fill=X)

Radiobutton(frm_top, text="원",     variable=shape_var, value=1).pack(side=LEFT, padx=5, pady=5)
Radiobutton(frm_top, text="사각형", variable=shape_var, value=2).pack(side=LEFT, padx=5, pady=5)
Radiobutton(frm_top, text="삼각형", variable=shape_var, value=3).pack(side=LEFT, padx=5, pady=5)
Button(frm_top, text="지우기", command=on_clear).pack(side=RIGHT, padx=5, pady=5)

canvas = Canvas(window, bg="white")
canvas.pack(fill=BOTH, expand=True)
canvas.bind("<Button-1>", on_canvas_click)

window.mainloop()
'''

from tkinter import *
import time


class StopWatch:
    def __init__(self):
        self.start_time = None
        self.elapsed = 0.0
        self.running = False

    def start(self):
        if self.running:
            return
        self.start_time = time.time()
        self.running = True

    def stop(self):
        if not self.running:
            return
        self.elapsed += time.time() - self.start_time
        self.running = False

    def reset(self):
        self.running = False
        self.elapsed = 0.0

    def current(self):
        if self.running:
            return self.elapsed + (time.time() - self.start_time)
        return self.elapsed


def update():
    label.config(text=f"{sw.current():7.2f} 초")
    window.after(100, update)   


def on_start():
    sw.start()


def on_stop():
    sw.stop()


def on_reset():
    sw.reset()
    label.config(text=f"{sw.current():7.2f} 초")


sw = StopWatch()

window = Tk()
window.title("연습 4 - StopWatch")
window.geometry("320x150")

label = Label(window, text="  0.00 초", font=("Consolas", 28))
label.pack(pady=10)

frm = Frame(window)
frm.pack()
Button(frm, text="시작", width=7, command=on_start).pack(side=LEFT, padx=5)
Button(frm, text="정지", width=7, command=on_stop).pack(side=LEFT, padx=5)
Button(frm, text="리셋", width=7, command=on_reset).pack(side=LEFT, padx=5)

update()
window.mainloop()












        
