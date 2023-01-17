import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

from BusinessLayer.Bclient import BClient



class ClientRegister(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        # oject for tkinter
        self.minsize(width=900, height=600)
        self.resizable(False, False)

        # button click functions

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

        self.l_panel = tk.PanedWindow(width=450, height=550)
        self.l_panel.pack(side="left")

        # left panel image
        self.splash_cnv = tk.Canvas(self.l_panel, bg="#393A10", width=450, height=550, border=0, )
        self.splash_cnv.pack(fill="both")

        self.splash_img = Image.open("FrontendLayer/Images/taxi_page.jpg")
        self.splash_img = self.splash_img.resize((750, 1150), Image.ANTIALIAS)
        self.resize_splashimg = ImageTk.PhotoImage(self.splash_img)

        self.splash_cnv.create_image(225, 120, image=self.resize_splashimg)

        # right panned window
        self.r_panel = tk.PanedWindow(background="#4A6D7C", width=450, height=550)
        self.r_panel.pack(side="right")

        self.back_btn = tk.Button(self.r_panel, background="#4A6D7C", text="<<~~~~",
                                  foreground="white", relief="groove", border=0,
                                  command=lambda: [self.destroy(), self.back()])
        self.back_btn.pack()

        # create panned window/.
        self.m_panel = tk.PanedWindow(self.r_panel, width=400, height=480, bg="#393A10")
        self.m_panel.pack(pady=25, padx=25)

        # add logo
        self.logo_canvas = tk.Canvas(self.m_panel, bg="#393A10", width=120, height=120, border=0, )
        self.logo_canvas.pack(pady=60)

        self.logo = Image.open("FrontendLayer/Images/grey_logo.png")
        self.logo = self.logo.resize((140, 140), Image.ANTIALIAS)
        self.re_logo = ImageTk.PhotoImage(self.logo)

        self.logo_canvas.create_image(62, 62, image=self.re_logo)

        # #ask for name

        self.name_in = tk.Entry(self.m_panel, width=60, )
        self.name_in.insert(0, "Enter your name: ")
        self.name_in.config(state="disabled")
        self.name_in.pack(padx=35, pady=10, ipady=4)

        # binding the function to the entry
        self.name_in.bind("<Button-1>", name_click)

        # ask for phone number

        self.num_in = tk.Entry(self.m_panel, width=60)
        self.num_in.insert(0, "Enter your phone number: ")
        self.num_in.config(state="disabled")
        self.num_in.pack(padx=35, pady=10, ipady=4)

        self.num_in.bind("<Button-1>", num_click)

        # ask for address

        self.address_in = tk.Entry(self.m_panel, width=60)
        self.address_in.insert(0, "Enter your address: ")
        self.address_in.config(state="disabled")
        self.address_in.pack(padx=35, pady=10, ipady=4)

        self.address_in.bind("<Button-1>", address_click)

        # ask for email address

        self.email_in = tk.Entry(self.m_panel, width=60)
        self.email_in.insert(0, "Enter your email address: ")
        self.email_in.config(state="disabled")
        self.email_in.pack(padx=35, pady=10, ipady=5)

        self.email_in.bind("<Button-1>", email_click)

        # #ask for password

        self.pass_in = tk.Entry(self.m_panel, width=60, show="*")
        self.pass_in.insert(0, "Enter your password: ")
        self.pass_in.config(state="disabled")
        self.pass_in.pack(padx=35, pady=10, ipady=5)

        self.pass_in.bind("<Button-1>", pass_click)
        # register button
        self.reg_btn = tk.Button(self.m_panel, text="Register", width=7, height=1, relief="groove",
                                 command=self.register)
        self.reg_btn.pack(pady=15)

        # execute window
        self.mainloop()

    def register(self):
        from Models.ClientM import ClientModel
        name = self.name_in.get()
        address = self.address_in.get()
        email = self.email_in.get()
        number = self.num_in.get()
        password = self.pass_in.get()

        cus = ClientModel(name, address, email, number, password)
        b_client = BClient(cus)
        try:
            b_cus = b_client.register_client()
            if b_cus:
                self.destroy()
                self.openlogin()


        except Exception as e:
            messagebox.showerror("Error", "An error occurred while trying to register: {}".format(e))

    def openlogin(self):
        from FrontendLayer.Login import LoginPage

        log = LoginPage()

    def back(self):
        from FrontendLayer.selectionpage import SelectionPage

        back = SelectionPage()
