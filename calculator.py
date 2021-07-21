from tkinter import * 


def press(event):
    global scvalue
    text = event.widget.cget("text")
    
    if text == " = ":
        if scvalue.get().isdigit():
            value = int(scvalue.get())

        else:
            try:
                value = eval(scvalue.get())

            except Exception as e:
                scvalue.set("Undefined")
                screen.update()

        scvalue.set(value)
        screen.update()

    elif text == " C ":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()

root.geometry("302x438")
root.minsize(302, 438)
root.maxsize(302, 438)
root.title("BASIC CALCULATOR")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="Stylus 30 bold").pack(pady=12, ipady=8, padx=8)

f1 = Frame(root, borderwidth=4, bg="Teal")
f1.pack(side=LEFT, anchor="nw", padx=0)
b1 = Button(f1, fg="Dark orange", text=" C ",  font="Stylus 22 bold", bg="Gold", relief=RAISED, borderwidth=2.75)
b1.pack(pady=2.5, padx=1.75)
b1.bind("<Button-1>", press)
 
b2 = Button(f1, fg="orange", text="7", padx=10, font="Stylus 22 bold", bg="BlanchedAlmond" ,relief=RAISED, borderwidth=2.75)
b2.pack(pady=3, padx=2)
b2.bind("<Button-1>", press)

b3 = Button(f1, fg="orange", text="4", padx=10,  font="Stylus 22 bold", bg="BlanchedAlmond" ,relief=RAISED, borderwidth=2.75)
b3.pack(pady=3, padx=2)
b3.bind("<Button-1>", press)

b4 = Button(f1, fg="orange", text="1",padx=10,   font="Stylus 22 bold", bg="BlanchedAlmond", relief=RAISED, borderwidth=2.75)
b4.pack(pady=3, padx=2)
b4.bind("<Button-1>", press)

b5 = Button(f1, fg="orange", text="0", padx=10,  font="Stylus 22 bold", bg="BlanchedAlmond", relief=RAISED, borderwidth=2.75)
b5.pack(pady=3, padx=2)
b5.bind("<Button-1>", press)

f2 = Frame(root, borderwidth=4, bg="Teal")
f2.pack(side=LEFT, anchor="nw")
b1= Button(f2, fg="Dark orange", text="%", padx=7,  font="Stylus 22 bold", bg="Gold", relief=RAISED, borderwidth=2.75)
b1.pack(pady=2.5, padx=1.75)
b1.bind("<Button-1>", press)

b2 = Button(f2, fg="orange", text="8",padx=10,   font="Stylus 22 bold", bg="BlanchedAlmond" ,relief=RAISED, borderwidth=2.75)
b2.pack(pady=3, padx=2)
b2.bind("<Button-1>", press)

b3 = Button(f2, fg="orange", text="5",padx=10,   font="Stylus 22 bold", bg="BlanchedAlmond" ,relief=RAISED, borderwidth=2.75)
b3.pack(pady=3, padx=2)
b3.bind("<Button-1>", press)

b4 = Button(f2, fg="orange", text="2",padx=10,   font="Stylus 22 bold", bg="BlanchedAlmond" ,relief=RAISED, borderwidth=2.75)
b4.pack(pady=3, padx=2)
b4.bind("<Button-1>", press)

b5 = Button(f2, fg="orange", text="00",  font="Stylus 22 bold", bg="BlanchedAlmond" ,relief=RAISED, borderwidth=2.75)
b5.pack(pady=3, padx=2)
b5.bind("<Button-1>", press)

f3 = Frame(root, borderwidth=4, bg="Teal")
f3.pack(side=LEFT, anchor="nw")
b1 = Button(f3, fg="Dark orange", text="/",padx=14,  font="Stylus 22 bold", bg="Gold", relief=RAISED, borderwidth=2.75)
b1.pack(pady=2.5, padx=1.75)
b1.bind("<Button-1>", press)

b2 = Button(f3, fg="orange", text="9",padx=10,   font="Stylus 22 bold", bg="BlanchedAlmond" ,relief=RAISED, borderwidth=2.75)
b2.pack(pady=3, padx=2)
b2.bind("<Button-1>", press)

b3 = Button(f3, fg="orange", text="6",padx=10,   font="Stylus 22 bold", bg="BlanchedAlmond" ,relief=RAISED, borderwidth=2.75)
b3.pack(pady=3, padx=2)
b3.bind("<Button-1>", press)

b4 = Button(f3, fg="orange", text="3",padx=10,   font="Stylus 22 bold", bg="BlanchedAlmond" ,relief=RAISED, borderwidth=2.75)
b4.pack(pady=3, padx=2)
b4.bind("<Button-1>", press)

b5 = Button(f3, fg="orange", text=".", padx=13.5,  font="Stylus 22 bold", bg="BlanchedAlmond" ,relief=RAISED, borderwidth=2.75)
b5.pack(pady=3, padx=2)
b5.bind("<Button-1>", press)

f4 = Frame(root, borderwidth=4, bg="Teal")
f4.pack(side=LEFT, anchor="nw")
b1 = Button(f4, fg="Dark orange", text="*",  padx=14, font="Stylus 22 bold", bg="Gold", relief=RAISED, borderwidth=2.75)
b1.pack(pady=2.5, padx=1.75)
b1.bind("<Button-1>", press)

b2 = Button(f4, fg="Dark orange", text=" - ",padx=14,  font="Stylus 22 bold", bg="Gold" ,relief=RAISED, borderwidth=2.75)
b2.pack(pady=3, padx=2)
b2.bind("<Button-1>", press)

b3 = Button(f4, fg="Dark orange", text=" + ", pady=35, font="Stylus 22 bold", bg="Gold" ,relief=RAISED, borderwidth=2.75)
b3.pack(pady=3, padx=2)
b3.bind("<Button-1>", press)

b4 = Button(f4, fg="orange", text=" = ",  font="Stylus 22 bold", bg="BlanchedAlmond" ,relief=RAISED, borderwidth=2.75)
b4.pack(pady=3, padx=2)
b4.bind("<Button-1>", press)
root.mainloop()