from tkinter import *

# 변수 선언
operator = ""

# 함수 정의


def btn_click(number):
    global operator
    operator = operator + str(number)
    e.delete(0, END)
    e.insert(0, operator)


def btn_clear():
    global operator
    operator = ""
    e.delete(0, END)


def btn_backspace():
    pass  # not working


def btn_plusminus():
    number = e.get()
    new_number = int(number)*-1
    e.delete(0, END)
    e.insert(0, new_number)


def btn_equal():
    global operator
    result = str(eval(operator))
    e.delete(0, END)
    e.insert(0, result)


# main
root = Tk()
root.title("My Calulator")
root.resizable(False, False)

# 디스플레이 화면
e = Entry(root, bg="lavender", font=15, width=30, justify="right")
e.grid(row=0, column=0, columnspan=4, padx=2, pady=2)

# 첫 번째 줄
btn_ce = Button(root, font=10, text="CE",
                width=6, height=2, command=btn_clear)
btn_c = Button(root, font=10, text="C",
               width=6, height=2, command=btn_clear)
btn_back = Button(root, font=10, text="<-",
                  width=6, height=2, command=btn_backspace)
btn_divide = Button(root, font=10,
                    text="%", width=6, height=2, command=lambda: btn_click("/"))

btn_ce.grid(row=1, column=0, padx=1, pady=1)
btn_c.grid(row=1, column=1, padx=1, pady=1)
btn_back.grid(row=1, column=2, padx=1, pady=1)
btn_divide.grid(row=1, column=3, padx=1, pady=1)

# 두 번째 줄
btn_7 = Button(root, font=10, text="7", width=6,
               height=2, command=lambda: btn_click(7))
btn_8 = Button(root, font=10, text="8", width=6,
               height=2, command=lambda: btn_click(8))
btn_9 = Button(root, font=10, text="9", width=6,
               height=2, command=lambda: btn_click(9))
btn_multiply = Button(root, font=10, text="x", width=6, height=2,
                      command=lambda: btn_click("*"))

btn_7.grid(row=2, column=0, padx=1, pady=1)
btn_8.grid(row=2, column=1, padx=1, pady=1)
btn_9.grid(row=2, column=2, padx=1, pady=1)
btn_multiply.grid(row=2, column=3, padx=1, pady=1)

# 세 번째 줄
btn_4 = Button(root, font=10, text="4", width=6,
               height=2, command=lambda: btn_click(4))
btn_5 = Button(root, font=10, text="5", width=6,
               height=2, command=lambda: btn_click(5))
btn_6 = Button(root, font=10, text="6", width=6,
               height=2, command=lambda: btn_click(6))
btn_subtract = Button(root, font=10, text="-", width=6, height=2,
                      command=lambda: btn_click("-"))

btn_4.grid(row=3, column=0, padx=1, pady=1)
btn_5.grid(row=3, column=1, padx=1, pady=1)
btn_6.grid(row=3, column=2, padx=1, pady=1)
btn_subtract.grid(row=3, column=3, padx=1, pady=1)

# 네 번째 줄
btn_1 = Button(root, font=10, text="1", width=6,
               height=2, command=lambda: btn_click(1))
btn_2 = Button(root, font=10, text="2", width=6,
               height=2, command=lambda: btn_click(2))
btn_3 = Button(root, font=10, text="3", width=6,
               height=2, command=lambda: btn_click(3))
btn_add = Button(root, font=10, text="+", width=6, height=2,
                 command=lambda: btn_click("+"))

btn_1.grid(row=4, column=0, padx=1, pady=1)
btn_2.grid(row=4, column=1, padx=1, pady=1)
btn_3.grid(row=4, column=2, padx=1, pady=1)
btn_add.grid(row=4, column=3, padx=1, pady=1)

# 네 번째 줄
btn_plusminus = Button(root, font=10, text="+/-", padx=16,
                       pady=10, command=btn_plusminus)
btn_0 = Button(root, font=10, text="0", width=6, height=2,
               command=lambda: btn_click(0))
btn_dot = Button(root, font=10, text=".", width=6, height=2,
                 command=lambda: btn_click(0))
btn_equal = Button(root, font=10, text="=", width=6, height=2,
                   command=btn_equal)

btn_plusminus.grid(row=5, column=0, padx=1, pady=1)
btn_0.grid(row=5, column=1, padx=1, pady=1)
btn_dot.grid(row=5, column=2, padx=1, pady=1)
btn_equal.grid(row=5, column=3, padx=1, pady=1)

root.mainloop()
