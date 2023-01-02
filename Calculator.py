import tkinter as tk
import ttkbootstrap as ttk



def row1_buttons():
    row1_frame = tk.Frame(app)
    button7 = ttk.Button(row1_frame, text = "7", bootstyle = "danger-outline")
    button8 = ttk.Button(row1_frame, text = "8", bootstyle = "danger-outline")
    button9 = ttk.Button(row1_frame, text = "9", bootstyle = "danger-outline")
    button_mul = ttk.Button(row1_frame, text = "*", bootstyle = "danger-outline")

    button7.pack(side = "left")
    button8.pack(side = "left", padx = 12)
    button9.pack(side = "left")
    button_mul.pack(side = "left", padx = 10)
    row1_frame.pack()


def row2_buttons():
    row2_frame = tk.Frame(app)
    button4 = ttk.Button(row2_frame, text = "4", bootstyle = "danger-outline")
    button5 = ttk.Button(row2_frame, text = "5", bootstyle = "danger-outline")
    button6 = ttk.Button(row2_frame, text = "6", bootstyle = "danger-outline")
    button_div = ttk.Button(row2_frame, text = "/", bootstyle = "danger-outline")

    button4.pack(side = "left")
    button5.pack(side = "left", padx = 12)
    button6.pack(side = "left")
    button_div.pack(side = "left", padx = 10)
    row2_frame.pack(pady = 15)


def row3_buttons():
    row3_frame = tk.Frame(app)
    button1 = ttk.Button(row3_frame, text = "1", bootstyle = "danger-outline")
    button2 = ttk.Button(row3_frame, text = "2", bootstyle = "danger-outline")
    button3 = ttk.Button(row3_frame, text = "3", bootstyle = "danger-outline")
    button_plu = ttk.Button(row3_frame, text = "+", bootstyle = "danger-outline")

    button1.pack(side = "left")
    button2.pack(side = "left", padx = 12)
    button3.pack(side = "left")
    button_plu.pack(side = "left", padx = 10)
    row3_frame.pack()


def row4_buttons():
    row4_frame = tk.Frame(app)
    button0 = ttk.Button(row4_frame, text = "0", bootstyle = "danger-outline")
    button_dot = ttk.Button(row4_frame, text = ".", bootstyle = "danger-outline")
    button_equ = ttk.Button(row4_frame, text = "=", bootstyle = "danger-outline")
    button_min = ttk.Button(row4_frame, text = "-", bootstyle = "danger-outline")

    button0.pack(side = "left")
    button_dot.pack(side = "left", padx = 12)
    button_equ.pack(side = "left")
    button_min.pack(side = "left", padx = 10)
    row4_frame.pack(pady = 15)


app = ttk.Window(themename = "darkly")
app.title("Calculator")

label = ttk.Label(app, text = "Calculator", font = 'Calibri 30 bold')
label.pack()

calculation_frame = tk.Frame(app)
event = ttk.Entry(calculation_frame, width = 32)
button = ttk.Button(calculation_frame, text = "Calculate", bootstyle = "danger-outline")

event.pack(side = "left",padx = 3)
button.pack(side = "left", padx = 10)
calculation_frame.pack(pady = 20)

row1_buttons()

row2_buttons()

row3_buttons()

row4_buttons()

app.geometry("350x350")
app.mainloop()