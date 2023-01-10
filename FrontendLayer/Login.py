# import system modules
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

from FrontendLayer.clienthome import ClientHome
# import file modules
from Models.ClientM import ClientModel
from BusinessLayer.Bclient import BClient
from BusinessLayer.Bdriver import BDriver
from Models.DriverM import DriverModel
from FrontendLayer.selectionpage import SelectionPage


# login page class
class LoginPage:
    # initiallization funcation
    def __init__(self):
        # object for tkinter
        self.root = tk.Tk()
        self.root.minsize(width=400, height=600)
        # root.resizable(False,False)

        # blank label
        self.blankLb = tk.Label(text="<<", font=("cursive", 10, "bold"), bg="#4A6D7C",
                                foreground="#4A6D7C", relief="groove", border=0)
        self.blankLb.pack()

        # create panned window
        self.mPanel = tk.PanedWindow(self.root, width=300, height=500, bg="#393A10")
        self.mPanel.pack(pady=25)

        # add logo
        self.logoCanvas = tk.Canvas(self.mPanel, bg="#393A10", width=120, height=120, border=0, )
        self.logoCanvas.place(x=100, y=48)

        self.logo = Image.open("FrontendLayer/Images/grey_logo.png")
        self.logo = self.logo.resize((130, 130), Image.ANTIALIAS)
        self.re_logo = ImageTk.PhotoImage(self.logo)

        self.logoCanvas.create_image(62, 62, image=self.re_logo)

        # ask for email address
        self.email_lb = tk.Label(self.mPanel, text="Email Address:", font=("cursive", 9, "bold"), background="#393A10",
                                 foreground="white")
        self.email_lb.place(x=20, y=220)

        self.email_in = tk.Entry(self.mPanel, width=43, )
        self.email_in.place(x=20, y=250)

        # ask for password
        self.pass_lb = tk.Label(self.mPanel, text="Password: ", font=("cursive", 9, "bold"), background="#393A10",
                                foreground="white")
        self.pass_lb.place(x=20, y=300)

        self.pass_in = tk.Entry(self.mPanel, width=43, show="*")
        self.pass_in.place(x=20, y=330)

        # login button
        self.client_lg_btn = tk.Button(text="Client", width=7, height=1, command=self.client_authenticate_login)
        self.client_lg_btn.place(x=270, y=460)

        self.driver_lg_btn = tk.Button(text="Driver", width=7, height=1, command=self.driver_authenticate_login)
        self.driver_lg_btn.place(x=75, y=460)

        # sign up route
        self.lb_register = tk.Label(text="Not Registered yet?", background="#393A10", foreground="white")
        self.lb_register.place(x=70, y=500)

        # click me button
        self.sp = tk.Button(text="Click Here!!", relief="groove", border=0, bg="#393A10", foreground="#FFFC31",
                            command=self.open_selection_page)
        self.sp.place(x=180, y=500)

        # design window
        self.root.config(bg="#4A6D7C")

        # execute tkinter
        self.root.mainloop()

    # route function for selection page
    def open_selection_page(self):
        self.root.destroy()  # close the LoginPage window
        selection_page = SelectionPage()  # object for SelectionPage window

    # function for verifying client
    def client_authenticate_login(self):
        email = self.email_in.get()
        passwd = self.pass_in.get()
        cus = ClientModel()
        cus.setemail(email)
        cus.setpassword(passwd)

        b_client = BClient(cus)
        login = b_client.authenticate_client()

        if login['status']:

            messagebox.showinfo("Done!", "Login Successful!")
            self.root.destroy()
            log = login['content']
            customer = ClientModel()
            customer.setclient_id(log[0][0])
            ClientHome(customer)
        else:
            messagebox.showerror('error', "email or password did not match!")

    # function for verifying driver
    def driver_authenticate_login(self):

        email = self.email_in.get()
        passwd = self.pass_in.get()
        cus = DriverModel()
        cus.setemail(email)
        cus.setpassword(passwd)

        b_driver = BDriver(cus)
        login = b_driver.authenticate_driver()

        if login['status']:

            messagebox.showinfo("Done!", "Login Successful!")

            self.root.destroy()
            log = login['content']
            customer = DriverModel()
            customer.setclient_id(log[0][0])
            # ClientHome(customer)
        else:
            messagebox.showerror('error', "email or password did not match!")
