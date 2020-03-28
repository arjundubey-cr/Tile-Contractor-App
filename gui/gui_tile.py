from tkinter import *
from tkinter import messagebox

################################################
rate = 20

root = Tk(className=" Tile Contractor App")
root.geometry("500x200")


def get_answer():
    messagebox.showinfo(title="Info", message="Congratulations! You have grabbed an amazing offer.")
    leng = float(length.get())
    wid = float(width.get())
    area = leng * wid
    costentry.insert(0, area * rate)
    perdiscount = get_discount(area)
    discountam = perdiscount * area * rate * 0.01
    discountentry.insert(0, discountam)
    finalentry.insert(0, (area * rate - discountam))


def get_discount(area):
    discount = 0.00
    if area <= 200:
        discount = 5
    elif area <= 500:
        discount = 10
    elif area <= 1000:
        discount = 15
    else:
        discount = 20
    return discount


label1 = Label(root, text="Enter the value of length(in feet): ").grid(row=1, column=1)
length = StringVar()
entry1 = Entry(root, bd=5, textvariable=length).grid(row=1, column=2)
label2 = Label(root, text="Enter the value of width(in feet): ").grid(row=2, column=1)
width = StringVar()
entry2 = Entry(root, bd=5, textvariable=width).grid(row=2, column=2)

# ADDING BUTTONS
Button(root, text="Calculate", bg='#0052cc', fg='#ffffff', command=lambda: get_answer()).grid(row=3, column=2)
# Button(root, text="Clear", bg='#0052cc', fg='#ffffff', command=lambda: clear()).grid(row=3, column=2)

# OUTPUT WIDGET(TO DISPLAY ANSWER)
totalcost = Label(root, text="Total Cost:").grid(row=6, column=1)
costentry = Entry(root, bd=5)
costentry.grid(row=6, column=2)
discountlabel = Label(root, text="Discount: ").grid(row=7, column=1)
discountentry = Entry(root, bd=5)
discountentry.grid(row=7, column=2)
finalcost = Label(root, text="Final Amount:").grid(row=8, column=1)
finalentry = Entry(root, bd=5)
finalentry.grid(row=8, column=2)

root.mainloop()
