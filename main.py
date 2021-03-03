import random
from tkinter import Tk, Label, Canvas, END, Button, Entry, IntVar, Radiobutton, PhotoImage
from tkinter.ttk import Combobox

# Declare colours
primaryColor = "#fff"
secondaryColor = '#000'

# Creating GUI
root = Tk()
root.title('Password Generator')
root.geometry('640x480+500+100')
root.config(borderwidth=0)
root.resizable(height=False, width=False)

# Declare instance variables
oneVar = IntVar()
twoVar = IntVar()

labelBg = Label(root, bg=primaryColor, bd=0, highlightthickness=0, width=640, height=480)
labelBg.pack()

# Declaring the options
radio_lo_up = Radiobutton(root, text='LowerCase and UpperCase',
                          variable=oneVar, value=0, bg=primaryColor,
                          fg=secondaryColor, activebackground=secondaryColor,
                          activeforeground=secondaryColor)
radio_lo_up.place(x=105, y=90)
radio_spl = Radiobutton(root, text='LowerCase, UpperCase and Numbers',
                        variable=oneVar, value=1, bg=primaryColor,
                        fg=secondaryColor, activebackground=secondaryColor,
                        activeforeground=secondaryColor)
radio_spl.place(x=105, y=130)
radio_num = Radiobutton(root, text='LowerCase, UpperCase, Numbers and Special Characters',
                        variable=oneVar, value=2, bg=primaryColor,
                        fg=secondaryColor, activebackground=secondaryColor,
                        activeforeground=secondaryColor)
radio_num.place(x=105, y=170)

# Length of the Password
c_label = Label(root, text='Length', bg=primaryColor, fg=secondaryColor)
c_label.place(x=105, y=230)
combo = Combobox(root, textvariable=twoVar, width=5)
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.place(x=170, y=230)

# Password input
r_pwd = Label(root, text='Password', fg=secondaryColor, bd=0, highlightthickness=0, bg=primaryColor)
r_pwd.place(x=105, y=280)
entry = Entry(labelBg, bg=primaryColor)
entry.place(x=170, y=275)


# Main Function
def rnd_pwd():
    entry.delete(0, END)
    length = twoVar.get()
    lower = "abcdefghijklmnopqrstuvwxyz "
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    upper_lower = lower + upper[:len(upper) - 2]
    numbers = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    special = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ''

    if oneVar.get() == 0:
        for i in range(length):
            password += random.choice(upper_lower)
        return password
    elif oneVar.get() == 1:
        for i in range(length):
            password += random.choice(numbers)
        return password
    elif oneVar.get() == 2:
        for i in range(length):
            password += random.choice(special)
        return password
    else:
        print('Select an option')


def generate():
    password = rnd_pwd()
    entry.insert(10, password)


gn_btn = Button(labelBg, text='Generate Password',
                bg=primaryColor, activebackground=primaryColor,
                borderwidth=0, command=generate)
gn_btn.place(x=250, y=360)
root.mainloop()
