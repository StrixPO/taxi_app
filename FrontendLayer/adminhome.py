import tkinter as tk
from tkinter import ttk, END

from BusinessLayer.Bbook import BBook
from BusinessLayer.Bclient import BClient
from BusinessLayer.Bdriver import BDriver
from Models.BookingM import Booking
from Models.ClientM import ClientModel
from Models.DriverM import DriverModel


class AdminHome:
    def __init__(self):
        self.root = tk.Tk()
        # Create a frame to hold other widgets
        self.root.minsize(width=550, height=400)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Create an empty dictionary to store frames
        self.frames = {}

        for F in (ViewAllBooking, ViewAllCustomer, ViewAllDriver):  # Add RequestHistory to this list
            page_name = F.__name__
            frame = F(parent=self.root, controller=self)  # Pass customer object as argument
            self.frames[page_name] = frame

            # the different pages are below
            # pages will be stacked and the chosen will be displayed on top
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("ViewAllBooking")
        print(self.frames)

    def show_frame(self, page_name):
        """Show a frame for the chosen page"""
        frame = self.frames[page_name]
        frame.tkraise()


class ViewAllBooking(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # nav-bar configuration
        self.nav_bar = tk.PanedWindow(self, bg="white")
        self.nav_bar.pack(fill="x", side="top")

        self.Home_btn = tk.Button(self.nav_bar, text="View Bookings",
                                  command=lambda: controller.show_frame("ViewAllBooking"))

        self.RequestH_btn = tk.Button(self.nav_bar, text="View Driver",
                                      command=lambda: controller.show_frame("ViewAllDriver"))
        self.Profile_btn = tk.Button(self.nav_bar, text="View Customer",
                                     command=lambda: controller.show_frame("ViewAllCustomer"))

        self.Home_btn.grid(row=0, column=0)
        self.Profile_btn.grid(row=0, column=1)
        self.RequestH_btn.grid(row=0, column=2)

        self.table_panel = tk.PanedWindow(self)
        self.table_panel.pack(side="top", fill="both", pady=10)
        self.table_panel.config(bg="white")

        # Create Treeview

        self.treeview = ttk.Treeview(self.table_panel)

        self.treeview['show'] = 'headings'

        self.treeview["columns"] = ('book_id', 'pickup_time', 'pickup_date',
                                    'pickup_location', 'drop_location', 'cust_ID', 'driver_id')

        # assigning width, minwidth and anchor to the column

        self.treeview.column("book_id", width=100, minwidth=120, )
        self.treeview.column("pickup_time", width=130, minwidth=100, )
        self.treeview.column("pickup_date", width=130, minwidth=120, )
        self.treeview.column("pickup_location", width=90, minwidth=100, )
        self.treeview.column("drop_location", width=90, minwidth=100, )
        self.treeview.column("cust_ID", width=90, minwidth=100, )
        self.treeview.column("driver_id", width=90, minwidth=100, )

        # assigning texts and anchors to the headings

        self.treeview.heading("book_id", text="Booking ID", )
        self.treeview.heading("pickup_time", text="Pickup Time", )
        self.treeview.heading("pickup_date", text="Pickup Date", )
        self.treeview.heading("pickup_location", text="Pickup Location", )
        self.treeview.heading("drop_location", text="Drop Location", )
        self.treeview.heading("cust_ID", text="Customer ID", )
        self.treeview.heading("driver_id", text="Driver ID", )

        abook = Booking()
        asb = BBook(abook)
        ab = asb.show_admin_table()
        print(ab)

        for i in range(len(ab)):
            self.treeview.insert(parent='', index='end',
                                 values=(ab[i][0], ab[i][1], ab[i][2], ab[i][3], ab[i][4], ab[i][5], ab[i][6]))

        # Pack Treeview
        self.treeview.pack()

        def driver_click(event):

            self.driver_in.config(state="normal")
            if self.driver_in.get() == "Driver ID: ":
                self.driver_in.delete(0, END)
            else:
                pass

        def book_click(event):

            self.book_in.config(state="normal")
            if self.book_in.get() == "Booking ID: ":
                self.book_in.delete(0, END)
            else:
                pass

        self.form_table = tk.PanedWindow(self)
        self.form_table.pack(side="bottom", fill="x")
        self.form_table.config(bg="#62929e")

        self.book_in = tk.Entry(self.form_table, width=100)
        self.book_in.insert(0, "Booking ID: ")
        self.book_in.config(state="disabled")
        self.book_in.pack(padx=35, pady=15, ipady=2)

        self.book_in.bind("<Button-1>", book_click)

        self.driver_in = tk.Entry(self.form_table, width=100)
        self.driver_in.insert(0, "Driver ID: ")
        self.driver_in.config(state="disabled")
        self.driver_in.pack(padx=35, pady=15, ipady=2)

        self.driver_in.bind("<Button-1>", driver_click)

        self.assign_btn = tk.Button(self.form_table, text="Assign", command=self.assign)
        self.assign_btn.pack(padx=35, pady=15, ipady=2)

    def assign(self):

        did = self.driver_in.get()
        bid = self.book_in.get()
        addassign = Booking()
        addassign.setdriver_id(did)
        addassign.setbook_id(bid)
        ad = BBook(addassign)
        assignBook = ad.assign_driver()


class ViewAllCustomer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # nav-bar configuration
        self.nav_bar = tk.PanedWindow(self, bg="white")
        self.nav_bar.pack(fill="x", side="top")

        self.Home_btn = tk.Button(self.nav_bar, text="View Bookings",
                                  command=lambda: controller.show_frame("ViewAllBooking"))

        self.RequestH_btn = tk.Button(self.nav_bar, text="View Driver",
                                      command=lambda: controller.show_frame("ViewAllDriver"))
        self.Profile_btn = tk.Button(self.nav_bar, text="View Customer",
                                     command=lambda: controller.show_frame("ViewAllCustomer"))

        self.Home_btn.grid(row=0, column=0)
        self.Profile_btn.grid(row=0, column=1)
        self.RequestH_btn.grid(row=0, column=2)

        self.table_panel = tk.PanedWindow(self)
        self.table_panel.pack(side="top", fill="both", pady=10)
        self.table_panel.config(bg="white")

        # Create a Treeview widget and pack it into the parent widget
        self.table = ttk.Treeview(self.table_panel,
                                  columns=('cust_ID', 'name', 'number',
                                           'email', 'password', 'address'))
        self.table.pack(side='left', fill='both', expand=True)

        # Create a Scrollbar widget and pack it into the parent widget
        scrollbar = ttk.Scrollbar(self.table_panel, orient='vertical', command=self.table.yview)
        scrollbar.pack(side='right', fill='y')

        # Set the Treeview widget's scrollcommand to the Scrollbar widget's set method
        self.table.configure(yscrollcommand=scrollbar.set)

        # Insert column headings into the Treeview widget

        self.table.heading('cust_ID', text="Customer ID", )
        self.table.heading('name', text='Name')
        self.table.heading('number', text='Number')
        self.table.heading('email', text='Email')
        self.table.heading('password', text='Password')
        self.table.heading('address', text="Address", )

        client = ClientModel()
        b = BClient(client)
        a = b.view_all_client()

        for i in range(len(a)):
            self.table.insert(parent='', index='end',
                              values=(a[i][0], a[i][1], a[i][2], a[i][3], a[i][4], a[i][5]))

        self.table.pack()


class ViewAllDriver(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # nav-bar configuration
        self.nav_bar = tk.PanedWindow(self, bg="white")
        self.nav_bar.pack(fill="x", side="top")

        self.Home_btn = tk.Button(self.nav_bar, text="View Bookings",
                                  command=lambda: controller.show_frame("ViewAllBooking"))

        self.RequestH_btn = tk.Button(self.nav_bar, text="View Driver",
                                      command=lambda: controller.show_frame("ViewAllDriver"))
        self.Profile_btn = tk.Button(self.nav_bar, text="View Customer",
                                     command=lambda: controller.show_frame("ViewAllCustomer"))

        self.Home_btn.grid(row=0, column=0)
        self.Profile_btn.grid(row=0, column=1)
        self.RequestH_btn.grid(row=0, column=2)

        self.table_panel = tk.PanedWindow(self)
        self.table_panel.pack(side="top", fill="both", pady=10)
        self.table_panel.config(bg="white")

        # Create a Treeview widget and pack it into the parent widget
        self.table = ttk.Treeview(self.table_panel,
                                  columns=('driver_id', 'name', 'number',
                                           'address', 'email', 'password', 'lisence_plate', 'car_model'))
        self.table.pack(side='left', fill='both', expand=True)

        # Create a Scrollbar widget and pack it into the parent widget
        scrollbar = ttk.Scrollbar(self.table_panel, orient='vertical', command=self.table.yview)
        scrollbar.pack(side='right', fill='y')

        # Set the Treeview widget's scrollcommand to the Scrollbar widget's set method
        self.table.configure(yscrollcommand=scrollbar.set)

        # Insert column headings into the Treeview widget

        self.table.heading('driver_id', text="Driver ID", )
        self.table.heading('name', text='Name')
        self.table.heading('number', text='Number')
        self.table.heading('address', text='Address')
        self.table.heading('email', text='Email')
        self.table.heading('password', text="Password", )
        self.table.heading('lisence_plate', text="License Plate Number", )
        self.table.heading('car_model', text="Car Model", )

        driver = DriverModel()
        b = BDriver(driver)
        a = b.view_all_driver()

        for i in range(len(a)):
            self.table.insert(parent='', index='end',
                              values=(a[i][0], a[i][1], a[i][2], a[i][3], a[i][4], a[i][5], a[i][6], a[i][7]))

        self.table.pack()
