from tkinter import*
from math import sqrt

def solver (a,b,c,d,f):
     C=c
     currency=d
     name=f
     while C != 0:
          C = C - 1
          a=a+a*b/100
          A=a
     text ="\n summary you will have: %s"% (A)
     text1 ="\n currency: %s"% (currency)
     text2 ="\n Name and surname: %s"% (name) 
     f = open('bank.txt', 'a')
     f.write(text2+text+text1)
     f.close()
     return text2, text, text1

def inserter(value):
     output.delete("0.0","end")
     output.insert("0.0",value)    

def clear(event):
     caller=event.widget
     caller.delete("0", "end")

def handler():
     try:
          a_val=float(a.get())
          b_val=float(b.get())
          c_val=float(c.get())
          d_val=str(d.get())
          f_val=str(f.get())
          inserter(solver(a_val, b_val, c_val, d_val, f_val))
     except ValueError:
        inserter("check the input data")

root=Tk()
root.title("calculation of bank investments")
root.minsize(200,230)
root.resizable(width=False, height=False)


frame=Frame(root)
frame.grid()

a =Entry(frame, width=7)
a.grid(row=1,column=1,padx=(10,0))
a.bind("<FocusIn>", clear)
a_lab= Label(frame, text="investment").grid(row=1,column=2)

b =Entry(frame, width=3)
b.bind("<FocusIn>", clear)
b.grid(row=1,column=3)
b_lab= Label(frame, text="%").grid(row=1, column=4)

c =Entry(frame, width=3)
c.bind("<FocusIn>", clear)
c.grid(row=1, column=5)
c_lab= Label(frame, text="years").grid(row=1, column=6)

d =Entry(frame, width=3)
d.bind("<FocusIn>", clear)
d.grid(row=1, column=7)
d_lab=Label(frame, text="currency").grid(row=1, column=8)

f =Entry(frame, width=7)
f.bind("<FocusIn>", clear)
f.grid(row=1, column=9)
f_lab=Label(frame, text="Name and surname").grid(row=1, column=10)

but = Button(frame, text="show result", command=handler).grid(row=1, column=11, padx=(10,0))

output = Text(frame, bg="white", font="cocolas 12", width=50, height=10)
output.grid(row=2, columnspan=8)

root.mainloop()
