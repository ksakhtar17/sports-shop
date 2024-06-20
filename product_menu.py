import tkinter as tk
from tkinter import ttk
from tkinter import Label, Frame, PhotoImage, Checkbutton, Button, IntVar, OptionMenu, StringVar
from update_cart import UpdateCart


class Window(tk.Tk):  # class window created and is inheriting from built-in class tk.Tk of tkinter
    def __init__(self, update):  # constructor created for the class
        super().__init__()

        self['background'] = "grey"
        self.title("Sports website")
        self.geometry('600x650+150+50')
        self.sports = Label(text="Welcome to the Online Sports Shop", bg="grey", fg="black", font=("Calibre", 20))
        self.sports.pack()

        # Create a frame for the second label and the dropdown menu
        self.label_dropdown_frame = Frame(self, bg="black")
        self.label_dropdown_frame.pack(pady=10)

        self.sports2 = Label(self.label_dropdown_frame, text="Do you wish to update your sports gear? You are at the right place!",
                             bg="black", fg="white", font=("Arial", 10), relief="raised")
        self.sports2.pack(side="left", padx=10)

        # Options for the dropdown menu
        self.options = ["Checkout", "View cart"]

        # Datatype of menu text
        self.clicked = StringVar()

        # Initial menu text
        self.clicked.set("Checkout")

        # Create Dropdown menu
        self.drop = OptionMenu(self.label_dropdown_frame, self.clicked, *self.options)
        self.drop.pack(side="left")

        # Create a frame for the image
        self.image_frame = Frame(self, bg="#AEC6CF")
        self.image_frame.pack()

        self.img3 = PhotoImage(file='S&K (2).png')
        self.img_lab2 = Label(self.image_frame, image=self.img3)
        self.img_lab2.pack()

        self.tabs = Tabs(self, update)   # instantiating the tab class within the Window class to demonstrate composition relationship

        self.button = Button(self, text='Proceed', command=lambda: self.proceed_and_destroy)
        self.button.pack()

    def proceed_and_destroy(self):
        self.update.save_cart()
        self.destroy()


class Tabs: # class designated for creating tabs
    def __init__(self, parent, update):
        self.notebook = ttk.Notebook(parent)
        self.tabs = [
            ('Cricket Gear', '#000080'),
            ('Football Gear', '#000080'),
            ('Basketball Gear', '#000080'),
            ('Baseball Gear', '#000080'),
            ('Soccer Gear', '#000080'),
            ('Tennis Gear', '#000080'),
            ('Hockey Gear', '#000080'),
            ('Other Gear', '#000080')
        ]

        self.create_tabs()
        self.notebook.pack(fill='both', expand=True)

        self.update = update

    def create_tabs(self):
        for tab_text, tab_color in self.tabs:
            tab = ttk.Frame(self.notebook)
            self.notebook.add(tab, text=tab_text)

            # Create a frame to contain the buttons and checkboxes within the tabs
            button_frame = Frame(tab, bg='#d3d3d3')
            button_frame.pack(side='top', pady=5, fill='x')

            if tab_text == "Cricket Gear":
                var1 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Helmet", var1, 0)

                var2 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Shoes", var2, 1)

                var3 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Jersey", var3, 2)

                var4 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Ball", var4, 3)

                var5 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Bat", var5, 4)

            if tab_text == "Football Gear":
                var6 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Football", var6, 5)

                var7 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Football Jersey", var7, 6)

                var8 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Football shoes", var8, 7)

                var9 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Football nets", var9, 8)

                var10 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Football T-Shirt", var10, 9)

            if tab_text == "Basketball Gear":
                var11 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Basketball", var11, 10)

                var12 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Crew socks", var12, 11)

                var13 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Shooter sleeves", var13, 12)

                var14 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Backpack", var14, 13)

                var15 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Skinny hairband", var15, 14)

            if tab_text == "Baseball Gear":
                var16 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Baseball Cleats", var16, 15)

                var17 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Baseball leg guards", var17, 16)

                var18 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Baseball chest protector", var18, 17)

                var19 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Baseball T-shirt", var19, 18)

                var20 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Baseball bat", var20, 19)

            if tab_text == "Soccer Gear":
                var21 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Soccer Cleats", var21, 20)

                var22 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Soccer Shoes", var22, 21)

                var23 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Soccer pants", var23, 22)

                var24 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Soccer T-Shirt", var24, 25)

                var25 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Soccer ball", var25, 26)

            if tab_text == "Tennis Gear":
                var26 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Tennis ball", var26, 27)

                var27 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Tennis T-shirt", var27, 28)

                var28 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Tennis shoes", var28, 29)

                var29 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Tennis rackets", var29, 30)

                var30 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Tennis P-cap", var30, 31)

            if tab_text == "Hockey Gear":
                var31 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Hockey Jersey", var31, 32)

                var32 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Hockey Hat", var32, 33)

                var33 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Hockey Stick", var33, 34)

                var34 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Hockey ball", var34, 35)

                var35 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Hockey shoes", var35, 36)

            if tab_text == "Other Gear":
                var36 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "T-shirts", var36, 37)

                var37 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Shorts", var37, 38)

                var38 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Jackets", var38, 39)

                var39 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Hoddie", var39, 40)

                var40 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Cleats", var40, 41)

                var41 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Sleeves", var41, 42)

                var42 = IntVar()
                self.create_checkbox_with_buttons(button_frame, "Head Bands", var42, 43)

    def create_checkbox_with_buttons(self, parent, text, var, row): # function created for making the checkboxes functional
        def on_checkbutton_click():
            if var.get() == 0:  # If the checkbox is being checked for the first time

                self.update.increase(var, text)  # Increase the quantity and update the cart

        Checkbutton(parent, text=text, variable=var, fg='black', bg='#d3d3d3', anchor='w', command=on_checkbutton_click).grid(row=row, column=0, sticky='w', padx=5)
        Button(parent, text="+", command=lambda: self.update.increase(var, text), fg='black', bg='#d3d3d3').grid(row=row, column=1, padx=5)
        Label(parent, textvariable=var, fg='black', bg='#d3d3d3', width=3, anchor='e').grid(row=row, column=2, padx=5)
        Button(parent, text="-", command=lambda: self.update.decrease(var, text), fg='black', bg='#d3d3d3').grid(row=row, column=3, padx=5)


u = UpdateCart()
window = Window(u)
window.mainloop()

from view_cart import ViewCart

ViewCart()
