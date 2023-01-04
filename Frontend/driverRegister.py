# import ykinter modules and files
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


# Create class
class Drregister(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # object for tkinter
        self.minsize(width=1000, height=650)
        self.resizable(False, False)

        # left panned window
        self.l_panel = tk.PanedWindow(width=450, height=650)
        self.l_panel.pack(side="left")

        # left panel image
        self.logo_cnv = tk.Canvas(self.l_panel, bg="#393A10", width=550, height=690, border=0, )
        self.logo_cnv.pack()

        self.logo_img = Image.open("Frontend/Images/taxi_page.jpg")
        self.logo_img = self.logo_img.resize((550, 690), Image.ANTIALIAS)
        self.resize_logoimg = ImageTk.PhotoImage(self.logo_img)

        self.logo_cnv.create_image(278, 345, image=self.resize_logoimg)

        # right panned window
        self.r_panel = tk.PanedWindow(background="#4A6D7C", width=450, height=650)
        self.r_panel.pack(side="right")

        # right panel contents

        # create panned window
        self.m_panel = tk.PanedWindow(self.r_panel, width=400, height=615, bg="#393A10")
        self.m_panel.pack(pady=35, padx=25)

        # add logo
        self.logo_canvas = tk.Canvas(self.m_panel, bg="#393A10", width=120, height=120, border=0, )
        self.logo_canvas.place(x=100, y=48)

        self.logo = Image.open("Frontend/Images/grey_logo.png")
        self.logo = self.logo.resize((550, 690), Image.ANTIALIAS)
        self.re_logo = ImageTk.PhotoImage(self.logo)

        self.logo_canvas.create_image(278, 345, image=self.re_logo)

        # #ask for name
        self.name_lb = tk.Label(self.m_panel, text="Name", font=("cursive", 9, "bold"), background="#393A10",
                                foreground="white")
        self.name_lb.place(x=25, y=190)

        self.name_in = tk.Entry(self.m_panel, width=60)
        self.name_in.place(x=25, y=220)

        # ask for phone number
        self.num_lb = tk.Label(self.m_panel, text="Phone Number", font=("cursive", 9, "bold"), background="#393A10",
                               foreground="white")
        self.num_lb.place(x=25, y=250)

        self.num_in = tk.Entry(self.m_panel, width=60)
        self.num_in.place(x=25, y=280)

        # ask for email address
        self.email_lb = tk.Label(self.m_panel, text="Email Address", font=("cursive", 9, "bold"), background="#393A10",
                                 foreground="white")
        self.email_lb.place(x=25, y=310)

        self.email_in = tk.Entry(self.m_panel, width=60)
        self.email_in.place(x=25, y=340)

        # #
        # name_lb = Label(m_panel,text="Name", font=("cursive",9,"bold"), background="#393A10", foreground="white")
        # name_lb.place(x=25,y=370)

        # name_in = Entry(m_panel, width=60)
        # name_in.place(x=25,y=400)
        # #forgotton password

        # #ask for password
        self.pass_lb = tk.Label(self.m_panel, text="Password: ", font=("cursive", 9, "bold"), background="#393A10",
                                foreground="white")
        self.pass_lb.place(x=25, y=370)

        self.pass_in = tk.Entry(self.m_panel, width=60)
        self.pass_in.place(x=25, y=400)

        # Ask for car model
        self.carModel_lb = tk.Label(self.m_panel, text="Car Model", font=("cursive", 9, "bold"), background="#393A10",
                                    foreground="white")
        self.carModel_lb.place(x=25, y=430)

        self.carModel_in = tk.Entry(self.m_panel, width=60)
        self.carModel_in.place(x=25, y=460)
        # forgotton password

        # Ask for lisence plate number
        self.lisence_lb = tk.Label(self.m_panel, text="Lisence Plate Number", font=("cursive", 9, "bold"),
                                   background="#393A10",
                                   foreground="white")
        self.lisence_lb.place(x=25, y=490)

        self.lisence_in = tk.Entry(self.m_panel, width=60)
        self.lisence_in.place(x=25, y=520)
        # forgotton password

        # login button
        self.reg_btn = tk.Button(self.m_panel, text="Register", width=7, height=1)
        self.reg_btn.place(x=320, y=575)

        # execute window
        self.mainloop()
