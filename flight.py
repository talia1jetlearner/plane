from tkinter import*
from tkinter.ttk import*
window= Tk()
window.geometry("420x200")
window.title("Flight Booker")
#c=Combobox(window,values=["xx","xx","xx"],state="readonly",c.set(xx))
d= Label(window,text="Select Destination:",font="Arial 12")
d.grid(column=1,row=0)

def cal():
    global c
    price=""
    if c.get()== "New york":
        price= str(700+clas.get())
    elif c.get()== "Paris":
        price= str(250+clas.get())
    else:
        price= str(500+clas.get())
    tot.configure(text="Total Ticket Price: $"+price)

c=Combobox(window,values=["New york","Paris","London"],state="readonly",width=10)
c.set("New york")
cl= Label(window,text="Select class:")
clas= IntVar()
e= Radiobutton(window,text="Economy",variable=clas,value=0)
b= Radiobutton(window,text="Business (+$200)",variable=clas,value=200)
f= Radiobutton(window,text="First class(+$500)",variable=clas,value=500)
calc= Button(window,text="Calculate Price",command=cal)
tot= Label(window,text="Total Ticket Price: ",font="Arial 20")
c.grid(column=1,row=1)
cl.grid(column=1,row=2)
e.grid(column=0,row=3)
b.grid(column=1,row=3)
f.grid(column=3,row=3)
calc.grid(column=1,row=4)
tot.grid(column=1,row=5)
window.mainloop()