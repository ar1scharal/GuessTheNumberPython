from tkinter import*
import random
import time
window=Tk()
window.title("Guess the number")
window.geometry("600x600")
window.configure(bg='grey')
logo = PhotoImage(file="UpArrow.png")
logo = logo.subsample(2)
logo2 = PhotoImage(file="DownArrow.png")
logo2 = logo2.subsample(2)
logo3 = PhotoImage(file="Correct.png")
logo3 = logo3.subsample(2)

a=random.randint(0,100)
def check(event):
    global a,txt
    b=txt.get()
    if int(b)==a:
        lbl3.configure(image=logo3)
        txt.delete(0,END)
        txt.configure(state='disabled')
    if int(b) > a:
        lbl3.configure(image=logo2)
        txt.delete(0,END)
    if int(b) < a:
        lbl3.configure(image=logo)
        txt.delete(0,END)
def restart():
    global a,lbl3
    a=random.randint(0,100)
    lbl3.configure(text="press enter",image="")
    txt.configure(state='normal')
    for i in range(0, 15):
        c = random.randint(0, 100)
        lbl7.configure(text=c)
        lbl7.update()
        time.sleep(0.1)
        lbl7.configure(text="")

lbl=Label(window,text="Guess the number ",bg="grey",fg="#11FFF8",font=("Times New Roman",30))
lbl.grid(row=0,column=1,columnspan=3)
lbl2=Label(window,text="Find the secret number",bg="grey",fg="#11FFF8",font=("Times New Roman",30))
lbl2.grid(row=2,column=1,columnspan=3)
txt=Entry(window,width=5,fg="#11FFF8",font=("Times New Roman",30))
txt.grid(row=4,column=1,pady=20)
lbl3=Label(window,text="press enter",bg="grey",fg="#11FFF8",font=("Times New Roman",20))
lbl3.grid(row=4,column=3,pady=20)
btn=Button(window,text="Exit",command=exit,bg="grey",fg="#11FFF8",font=("Times New Roman",30))
btn.grid(row=6,column=1)
btn2=Button(window,text="Restart",bg="grey",fg="#11FFF8",font=("Times New Roman",30),command=restart)
btn2.grid(row=6,column=3)
lbl4=Label(window,text="",bg="grey")
lbl4.grid(row=1,column=0)
lbl5=Label(window,text="",bg="grey")
lbl5.grid(row=3,column=0)
lbl6=Label(window,text="",bg="grey")
lbl6.grid(row=5,column=0)
lbl7=Label(window,text="",bg="grey",fg="#11FFF8",font=("T   imes New Roman",30))
lbl7.grid(row=5,column=2)
for i in range(0, 15):
        c = random.randint(0, 100)
        lbl7.configure(text=c)
        lbl7.update()
        time.sleep(0.1)
        lbl7.configure(text="")

window.bind('<Return>',check)
window.mainloop()