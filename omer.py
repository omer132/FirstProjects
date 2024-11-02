import tkinter , random

window=tkinter.Tk()

window.geometry("600x600")

can=5

def a(): 
    global can
    fare=int(inp.get())
    

    if can<=1:
            uya.config(text=f"hakkiniz bitti,doğru cevap :{sayi}")
            but.config(state=tkinter.DISABLED)
            inp.config(state=tkinter.DISABLED)
            bt.pack()
    if can>0:
            if 100>fare > 0:
                if fare!=sayi:
                    can-=1
                    if fare<sayi:
                        uya.config(text=f"daha büyük bir sayi giriniz,kalan hak :{can}")


                    elif fare>sayi:
                        uya.config(text=f"daha küçük bir sayi giriniz,kalan hak :{can}")
                elif fare == sayi :
                    uya.config(text="tebrikler doğru bildiniz")
                    but.config(state=tkinter.DISABLED)
                    inp.config(state=tkinter.DISABLED)
                    bt.pack()
            else:
                can-=1
                uya.config(text=f"lütfen 100 ile 0 arası sayi giriniz,kalan hak{can}")


def tekrar():
    global sayi,can
    
    can=5
    sayi=random.randint(0,100)
    but.config(state=tkinter.NORMAL)
    inp.config(state=tkinter.NORMAL)
    uya.config(text="")
    inp.delete(0,tkinter.END)
    bt.pack_forget()

x=tkinter.Label(text="sayi giriniz :")
x.pack()

inp=tkinter.Entry()
inp.pack()

sayi=random.randint(0,100)

bt=tkinter.Button(text="tekrar oyna",command=tekrar)

but=tkinter.Button(text="onayla",command=a)
but.pack()

uya=tkinter.Label(text="")
uya.pack()

window.mainloop()