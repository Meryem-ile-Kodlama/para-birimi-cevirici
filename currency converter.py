from currency_converter import CurrencyConverter
from tkinter import *
from tkinter import messagebox
# pip install CurrencyConverter

c = CurrencyConverter()

def convert():
    amount_input = int(amount_e.get())
    input_c = inputc_e.get()
    output_c = outputc_e.get()
    amount_output = c.convert(amount_input,input_c,output_c)
    messagebox.showinfo("Output","{} {} = {} {}".format(amount_input,input_c,amount_output,output_c))

root = Tk()
root.geometry("400x360")
root.title("Currency Converter")
root.configure(bg="white")

title = Label(root,text="Currency Converter",font="Arial 20 bold",fg="#1c34bb",bg="white")
title.pack(pady=20)

amount_l = Label(root,text="Amount: ",font="Arial 16 bold",fg="#1c34bb",bg="white")
amount_l.pack()
amount_e = Entry(root)
amount_e.pack(pady=5)

inputc_l = Label(root,text="Input Currency: ",font="Arial 16 bold",fg="#1c34bb",bg="white")
inputc_l.pack()
inputc_e = Entry(root)
inputc_e.pack(pady=5)

outputc_l = Label(root,text="Output Currency: ",font="Arial 16 bold",fg="#1c34bb",bg="white")
outputc_l.pack()
outputc_e = Entry(root)
outputc_e.pack(pady=5)

convert_b = Button(root,text="convert",font="Arial 16 bold",fg="#1c34bb",bg="white",command=convert)
convert_b.pack(pady=20)

root.mainloop()