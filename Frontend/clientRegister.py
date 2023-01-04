# import ykinter modules and files
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from Models import clientM
from Business.Bclient import Bclient


# Create class
class Clregister(tk.Tk):
    def __init__(self):

        # oject for tkinter
        self.minsize(width=1000, height=650)
        self.resizable(False, False)

        def name_click(event):

            self.name_in.config(state="normal")
            if self.name_in.get() == "Enter your name: ":
                self.name_in.delete(0, tk.END)
            else:
                pass

        def num_click(event):

            self.num_in.config(state="normal")
            if self.num_in.get() == "Enter your phone number: ":
                self.num_in.delete(0, tk.END)
            else:
                pass

        def email_click(event):

            self.email_in.config(state="normal")
            if self.email_in.get() == "Enter your email address: ":
                self.email_in.delete(0, tk.END)
            else:
                pass

        def pass_click(event):

            self.pass_in.config(state="normal")
            if self.pass_in.get() == "Enter your password: ":
                self.pass_in.delete(0, tk.END)
            else:
                pass

        def address_click(event):

            self.address_in.config(state="normal")
            if self.address_in.get() == "Enter your address: ":
                self.address_in.delete(0, tk.END)
            else:
                pass

                # left panned window

        self.l_panel = tk.PanedWindow(width=450, height=650)
        self.l_panel.pack(side="left")

        # left panel image
        self.reg_cnv = tk.Canvas(self.l_panel, bg="#393A10", width=550, height=690, border=0, )
        self.reg_cnv.pack()

        self.reg_img = Image.open("Images/taxi_page.jpg")
        self.reg_img = self.reg_img.resize((550, 690), Image.ANTIALIAS)
        self.resize_regimg = ImageTk.PhotoImage(self.reg_img)

        self.reg_cnv.create_image(278, 345, image=self.resize_regimg)

        # right panned window
        self.r_panel = tk.PanedWindow(background="#4A6D7C", width=450, height=650)
        self.r_panel.pack(side="right")

        # right panel contents

        # create panned window
        self.m_panel = tk.PanedWindow(self.r_panel, width=400, height=615, bg="#393A10")
        self.m_panel.pack(pady=35, padx=25)

        # add logo
        self.logo_canvas = tk.Canvas(self.m_panel, bg="#393A10", width=120, height=120, border=0, )
        self.logo_canvas.pack(pady=60)

        self.logo = Image.open("Images/grey_logo.png")
        self.logo = self.logo.resize((140, 140), Image.ANTIALIAS)
        self.re_logo = ImageTk.PhotoImage(self.logo)

        self.logo_canvas.create_image(62, 62, image=self.re_logo)

        # #ask for name

        self.name_in = tk.Entry(self.m_panel, width=60, )
        self.name_in.insert(0, "Enter your name: ")
        self.name_in.config(state="disabled")
        self.name_in.pack(padx=35, pady=25, ipady=5)

        # binding the function to the entry
        self.name_in.bind("<Button-1>", name_click)

        # ask for phone number

        self.num_in = tk.Entry(self.m_panel, width=60)
        self.num_in.insert(0, "Enter your phone number: ")
        self.num_in.config(state="disabled")
        self.num_in.pack(padx=35, pady=25, ipady=5)

        self.num_in.bind("<Button-1>", num_click)

        # ask for address

        self.address_in = tk.Entry(self.m_panel, width=60)
        self.address_in.insert(0, "Enter your address: ")
        self.address_in.config(state="disabled")
        self.address_in.pack(padx=35, pady=25, ipady=5)

        self.address_in.bind("<Button-1>", address_click)

        # ask for email address

        self.email_in = tk.Entry(self.m_panel, width=60)
        self.email_in.insert(0, "Enter your email address: ")
        self.email_in.config(state="disabled")
        self.email_in.pack(padx=35, pady=25, ipady=5)

        self.email_in.bind("<Button-1>", email_click)

        # #ask for password

        self.pass_in = tk.Entry(self.m_panel, width=60, show="*")
        self.pass_in.insert(0, "Enter your password: ")
        self.pass_in.config(state="disabled")
        self.pass_in.pack(padx=35, pady=25, ipady=5)

        self.pass_in.bind("<Button-1>", pass_click)
        # register button
        self.reg_btn = tk.Button(self.m_panel, text="Register", width=7, height=1, relief="groove",
                              command=self.Register)
        self.reg_btn.pack(pady=15)

        # execute window
        self.root.mainloop()

    def Register(self):
        from Models.clientM import Client
        name = self.name_in.get()
        address = self.address_in.get()
        email = self.email_in.get()
        number = self.num_in.get()
        password = self.pass_in.get()

        cus = Client(name, address, email, number, password)
        b_client = Bclient(cus)
        try:
            b_cus = b_client.regcust()
            if b_cus:
                self.openhome()
                self.root.destroy()

        except Exception as e:
            messagebox.showerror("Error", "An error occurred while trying to register: {}".format(e))

    def openhome(self):
        from Frontend.clientHome import ClientHome
        home = ClientHome()




