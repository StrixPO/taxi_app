# import python modules
import tkinter as tk
from PIL import Image, ImageTk

# import directory packages
from FrontendLayer.clientregister import ClientRegister
from FrontendLayer.driverregister import DriverRegister


class SelectionPage(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # main window
        self.minsize(width=400, height=600)

        def clientRegister():
            client_register = ClientRegister()

        def driverRegister():
            driver_register = DriverRegister()

        # blank label
        self.back_btn = tk.Label(text="<<", font=("cursive", 10, "bold"), bg="#4A6D7C",
                                 foreground="#4A6D7C", relief="groove", border=0)
        self.back_btn.pack()

        # create panned window
        self.m_panel = tk.PanedWindow(self, width=300, height=500, bg="#393A10")
        self.m_panel.pack(pady=25)

        # add logo
        self.logo_canvas = tk.Canvas(self.m_panel, bg="#393A10", width=120, height=120, border=0, )
        self.logo_canvas.place(x=100, y=48)

        self.logo = Image.open("FrontendLayer/Images/grey_logo.png")
        self.logo = self.logo.resize((130, 130), Image.ANTIALIAS)
        self.re_logo = ImageTk.PhotoImage(self.logo)

        self.logo_canvas.create_image(62, 62, image=self.re_logo)

        self.main_lb = tk.Label(self.m_panel, text="Sign up for ...\n", font=("cursive", 24, "bold"),
                                background="#393A10",
                                foreground="#B0B59F")
        self.main_lb.place(x=60, y=220)

        # add driver logo with button under it

        # for driver button
        self.driver_btn = tk.Button(self.m_panel, text="", width=10, height=5, background="#393A10",
                                    command=lambda: [self.destroy(), driverRegister()])
        self.driver_btn.place(x=30, y=350)

        # for driver logo
        self.driver_logo = tk.Canvas(self.m_panel, bg="#393A10", width=75, height=40, border=0, )
        self.driver_logo.place(x=30, y=350)

        self.d_logo = Image.open("FrontendLayer/Images/driver_logo.png")
        self.d_logo = self.d_logo.resize((80, 100), Image.ANTIALIAS)
        self.d_re_logo = ImageTk.PhotoImage(self.d_logo)

        self.driver_logo.create_image(42, 22, image=self.d_re_logo)

        # add client logo with button

        # for clinet button

        self.client_btn = tk.Button(self.m_panel, text="", width=10, height=5, background="#393A10",
                                    command=lambda: [self.destroy(), clientRegister()])
        self.client_btn.place(x=190, y=350)

        # for logo
        self.client_logo = tk.Canvas(self.m_panel, bg="#393A10", width=75, height=40, border=0, )
        self.client_logo.place(x=190, y=350)

        self.c_logo = Image.open("FrontendLayer/Images/client_logo.png")
        self.c_logo = self.c_logo.resize((80, 80), Image.ANTIALIAS)
        self.c_re_logo = ImageTk.PhotoImage(self.c_logo)

        self.client_logo.create_image(42, 22, image=self.c_re_logo)

        # design window
        self.config(bg="#4A6D7C")

        # execute tkinter
        self.mainloop()
