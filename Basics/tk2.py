from tkinter import *

window = Tk()
window.geometry("500x300")
window.title("Transmit message")


def printt():
    print("send")


def exit1():
    exit()


fn = long()
Ln = IntVar()
st = long()
do = long()
at = long()
ha = long()
hi = long()
ho = long()
hp = long()
Vp = IntVar()

label1 = Label(window, text="ID:(hex)", font=("arial", 9, "bold"))
label1.grid(row=1, column=1)
label2 = Label(window, text="Lenght:", font=("arial", 9, "bold"))
label2.place(x=180, y=0)
label3 = Label(window, text="Data:(hex)", font=("arial", 9, "bold"))
label3.place(x=300, y=0)
label4 = Label(window, text="cycle time", font=("arial", 9, "bold"))
label4.place(x=0, y=40)
label5 = Label(window, text="send extended ", font=("arial", 9, "bold"))
label5.place(x=200, y=40)
label6 = Label(window, text="send ", font=("arial", 9, "bold"))
label6.place(x=200, y=60)

b1 = Button(window, text="send", width=12, bg='white', fg='black', command=printt())
b1.place(x=150, y=200)
b2 = Button(window, text="cancel", width=12, bg='white', fg='black', command=exit1())
b2.place(x=280, y=200)


entry_1 = Entry(textvar=fn, width=10)
entry_1.place(x=0, y=20)
entry_2 = Entry(textvar=Ln, width=9)
entry_2.place(x=180, y=20)
entry_3 = Entry(textvar=st, width=2)
entry_3.place(x=300, y=20)
entry_4 = Entry(textvar=do, width=2)
entry_4.place(x=320, y=20)
entry_5 = Entry(textvar=at, width=2)
entry_5.place(x=340, y=20)
entry_6 = Entry(textvar=ha, width=2)
entry_6.place(x=360, y=20)
entry_7 = Entry(textvar=hi, width=2)
entry_7.place(x=380, y=20)
entry_8 = Entry(textvar=ho, width=2)
entry_8.place(x=400, y=20)
entry_9 = Entry(textvar=hp, width=2)
entry_9.place(x=420, y=20)
entry_10 = Entry(textvar=Vp, width=2)
entry_10.place(x=440, y=20)
entry_11 = Entry(textvar=Vp, width=2)
entry_11.place(x=440, y=20)


window.mainloop()
