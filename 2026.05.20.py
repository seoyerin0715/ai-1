'''
from tkinter import *
from tkinter import messagebox


## 클래스 선언 부분 ##
class SeaWater:
    """UNESCO 1980 EOS-80 (압력 0 dbar) 기반 해수 밀도 계산기."""

    def __init__(self, T, S):
        if not (-2 <= T <= 40):
            raise ValueError
        if not (0 <= S <= 42):
            raise ValueError
        self.T = T
        self.S = S

    def density(self):
        """ρ(S,T,0) [kg/m^3] 반환"""
        T, S = self.T, self.S
        rho_w= 999.842594 + 6.793952e-2*T - 9.095290e-3*T**2+ 1.001685e-4*T**3 - 1.120083e-6*T**4 + 6.536336e-9*T**5
        A = 8.24493e-1 - 4.0899e-3*T + 7.6438e-5*T**2 - 8.2467e-7*T**3 + 5.3875e-9*T**4
        B = -5.72466e-3 + 1.0227e-4*T - 1.6546e-6*T**2
        C = 4.8314e-4
        rho=rho_w + A*S + B*S**1.5 + C*S*S
        return rho
        
    def sigma_t(self):
        """σ_t = ρ - 1000  [kg/m^3]"""
        return self.density() - 1000.0

    def __repr__(self):
        # 강의 12장 __repr__() 와 동일한 패턴
        return f"SeaWater(T={self.T:.2f}°C, S={self.S:.2f}PSU)"


## 함수 선언 부분 ##
def on_calc():
    try:
        T = float(entry_T.get())
        S = float(entry_S.get())
    except ValueError:
        messagebox.showerror("입력 오류", "T와 S는 숫자로 입력해 주세요.")
        return

    try:
        sw = SeaWater(T, S)
    except ValueError as e:
        messagebox.showerror("범위 오류", str(e))
        return

    rho = sw.density()
    sigma = sw.sigma_t()
    result.config(text=f"ρ   = {rho:9.4f} kg/m³\nσ_t = {sigma:9.4f} kg/m³")


## 메인 코드 부분 ##
window = Tk()
window.title("연습 5 - 해수 밀도 계산기 (EOS-80)")
window.geometry("380x230")

Label(window, text="수온 T [°C]:").grid(row=0, column=0, padx=10, pady=8, sticky="e")
entry_T = Entry(window, width=12);  entry_T.grid(row=0, column=1, padx=10, pady=8)
entry_T.insert(0, "15.0")

Label(window, text="염분 S [PSU]:").grid(row=1, column=0, padx=10, pady=8, sticky="e")
entry_S = Entry(window, width=12);  entry_S.grid(row=1, column=1, padx=10, pady=8)
entry_S.insert(0, "34.5")

Button(window, text="계산", width=12, command=on_calc).grid(row=2, column=0, columnspan=2, pady=10)

result = Label(window, text="", font=("Consolas", 12), justify=LEFT)
result.grid(row=3, column=0, columnspan=2)

window.mainloop()
'''

'''
from tkinter import *
from tkinter import messagebox


## 클래스 선언 부분 ##
class SeaWater:
    """UNESCO 1980 EOS-80 (압력 0 dbar) 해수 밀도 계산기"""

    T_MIN, T_MAX = -2.0, 40.0
    S_MIN, S_MAX =  0.0, 42.0

    def __init__(self, T, S):
        if not (self.T_MIN <= T <= self.T_MAX):
            raise ValueError(f"T 는 {self.T_MIN}~{self.T_MAX} °C 범위여야 합니다.")
        if not (self.S_MIN <= S <= self.S_MAX):
            raise ValueError(f"S 는 {self.S_MIN}~{self.S_MAX} PSU 범위여야 합니다.")
        self.T = T
        self.S = S

    def density(self):
        T, S = self.T, self.S

        # 순수 물 밀도 (S = 0)
        rho_w = (999.842594
                 + 6.793952e-2 * T
                 - 9.095290e-3 * T**2
                 + 1.001685e-4 * T**3
                 - 1.120083e-6 * T**4
                 + 6.536336e-9 * T**5)

        A = (8.24493e-1
             - 4.0899e-3 * T
             + 7.6438e-5 * T**2
             - 8.2467e-7 * T**3
             + 5.3875e-9 * T**4)

        B = (-5.72466e-3
             + 1.0227e-4 * T
             - 1.6546e-6 * T**2)

        C = 4.8314e-4

        rho = rho_w + A * S + B * S**1.5 + C * S * S
        return rho

    def sigma_t(self):
        return self.density() - 1000.0

    def __repr__(self):
        return f"SeaWater(T={self.T:.2f}°C, S={self.S:.2f}PSU)"


## 함수 선언 부분 ##
def on_calc():
    try:
        T = float(entry_T.get())
        S = float(entry_S.get())
    except ValueError:
        messagebox.showerror("입력 오류", "T와 S는 숫자로 입력해 주세요.")
        return

    try:
        sw = SeaWater(T, S)
    except ValueError as e:
        messagebox.showerror("범위 오류", str(e))
        return

    rho   = sw.density()
    sigma = sw.sigma_t()
    result.config(text=f"ρ   = {rho:9.4f} kg/m³\nσ_t = {sigma:9.4f} kg/m³")


## 메인 코드 부분 ##
window = Tk()
window.title("연습 5 - 해수 밀도 계산기 (EOS-80)")
window.geometry("380x230")

Label(window, text="수온 T [°C]:").grid(row=0, column=0, padx=10, pady=8, sticky="e")
entry_T = Entry(window, width=12);  entry_T.grid(row=0, column=1, padx=10, pady=8)
entry_T.insert(0, "15.0")

Label(window, text="염분 S [PSU]:").grid(row=1, column=0, padx=10, pady=8, sticky="e")
entry_S = Entry(window, width=12);  entry_S.grid(row=1, column=1, padx=10, pady=8)
entry_S.insert(0, "34.5")

Button(window, text="계산", width=12, command=on_calc).grid(row=2, column=0, columnspan=2, pady=10)

result = Label(window, text="", font=("Consolas", 12), justify=LEFT)
result.grid(row=3, column=0, columnspan=2)

window.mainloop()
'''

from tkinter import *
import math


## 클래스 선언 부분 ##
class Constituent:
    """단일 조화 분조 (M2, S2, K1, O1 등)"""
    def __init__(self, name, amplitude, period_hr, phase_deg=0.0):
        self.name = name
        self.A    = amplitude            # m
        self.T    = period_hr            # hr
        self.phi  = math.radians(phase_deg)
        self.enabled = True

    def eta(self, t):
        if not self.enabled:
            return 0.0
        return self.A * math.cos(2 * math.pi * t / self.T - self.phi)

    def __repr__(self):
        return f"{self.name}(A={self.A}, T={self.T})"


class Tide:
    """여러 분조의 합으로 조위 η(t) 를 계산"""
    def __init__(self, constituents):
        self.constituents = constituents

    def eta(self, t):
        return sum(c.eta(t) for c in self.constituents)

    def by_name(self, name):
        for c in self.constituents:
            if c.name == name:
                return c
        return None


## 함수 선언 부분 ##
def toggle(name):
    c = tide.by_name(name)
    if c is None:
        return
    c.enabled = bool(check_vars[name].get())


def step():
    """다음 프레임을 그린다 (애니메이션)"""
    global current_t
    current_t += 0.25
    draw()
    window.after(50, step)


def draw():
    canvas.delete("all")
    W = canvas.winfo_width()
    H = canvas.winfo_height()
    if W < 50 or H < 50:
        return

    t_left  = current_t - 24
    t_right = current_t + 12
    t_span  = t_right - t_left

    pad = 40
    y_mid = H / 2

    A_total = sum(c.A for c in tide.constituents if c.enabled) + 0.1
    y_scale = (H / 2 - pad) / A_total

    def to_px(t, eta):
        x = pad + (t - t_left) / t_span * (W - 2 * pad)
        y = y_mid - eta * y_scale
        return x, y

    # 0 m 기준선
    canvas.create_line(pad, y_mid, W - pad, y_mid, fill="#888888", dash=(2, 2))

    # 가로 시간축 눈금 (6시간 간격)
    t0 = math.floor(t_left / 6) * 6
    t  = t0
    while t <= t_right:
        x, _ = to_px(t, 0)
        canvas.create_line(x, y_mid - 4, x, y_mid + 4, fill="#888888")
        canvas.create_text(x, y_mid + 14, text=f"{t:.0f}h", fill="#666666",
                           font=("Consolas", 8))
        t += 6

    # 조위 곡선
    pts = []
    n = 400
    for i in range(n + 1):
        ti  = t_left + t_span * i / n
        pts.append(to_px(ti, tide.eta(ti)))
    for (x1, y1), (x2, y2) in zip(pts[:-1], pts[1:]):
        canvas.create_line(x1, y1, x2, y2, fill="navy", width=2)

    # 현재 시각 표시
    x_now, _ = to_px(current_t, 0)
    canvas.create_line(x_now, pad, x_now, H - pad, fill="red", width=1, dash=(4, 2))
    eta_now = tide.eta(current_t)
    canvas.create_text(x_now + 10, pad + 10,
                       text=f"t = {current_t:6.2f} h\nη = {eta_now:+.3f} m",
                       anchor="w", font=("Consolas", 10))


## 메인 코드 부분 ##
tide = Tide([
    Constituent("M2", 0.80, 12.4206,  0),
    Constituent("S2", 0.30, 12.0000, 30),
    Constituent("K1", 0.25, 23.9345, 60),
    Constituent("O1", 0.18, 25.8193, 90),
])

current_t = 0.0

window = Tk()
window.title("연습 7 - 조석 시뮬레이터")
window.geometry("640x460")

top = Frame(window)
top.pack(fill=X)
check_vars = {}
for c in tide.constituents:
    v = IntVar(value=1)
    check_vars[c.name] = v
    Checkbutton(top, text=f"{c.name}  A={c.A:.2f}m T={c.T:.2f}h",
                variable=v, command=lambda n=c.name: toggle(n)).pack(side=LEFT, padx=5)

canvas = Canvas(window, bg="white")
canvas.pack(fill=BOTH, expand=True, padx=10, pady=10)

step()
window.mainloop()

