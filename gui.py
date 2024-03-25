import tkinter as tk

m= t                                                                                                                                                                                                                                                                                                                                                                                                                           k.Tk()
m.geometry("500x500")
l1=tk.Label(m, text="email",width=10,height=5)
t1=tk.Entry(m,text="enter mail")

l2=tk.Label(m, text="name",width=10,height=5)
t2=tk.Entry(m,text="enter name")


vr=tk.StringVar()
l3=tk.Label(text="gender")
l3.grid(row=2,column=1)
r1=tk.Radiobutton(text="male", value="male" ,variable=vr,)
r1.grid(row=3,column=1)
r2=tk.Radiobutton(text="femlae", value="femlAe",variable=vr,)
r2.grid(row=4,column=1)

a=str(vr.get())



b=tk.Button(m, text="submit",width=10,height=2 )



l1.grid(row=0,column=0)
t1.grid(row=0,column=1)

l2.grid(row=1,column=0)
t2.grid(row=1,column=1)


check=tk.StringVar()

c1=tk.Checkbutton(text="ckeck to check ", variable=check, onvalue=1)
c1.grid()

menu=tk.StringVar()
menu.set("click to seleet")

drop=tk.OptionMenu(m,menu,"red","green","yellow","gray")
drop.grid()

b.grid()





m.mainloop()