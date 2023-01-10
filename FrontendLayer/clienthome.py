# import system modules
import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from datetime import datetime, timedelta, date

# import file modules
from tkinter import END
from DatabaseLayer.connection import connect_db
from BusinessLayer.Bbook import BBook
from Models.BookingM import Booking

client_id = 0


class ClientHome:

    def __init__(self, customer):
        global client_id

        # Initialize the object as a Tkinter frame
        # Set the minimum size of the window
        self.root = tk.Tk()
        # Create a frame to hold other widgets
        self.root.minsize(width=550, height=400)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        client_id = customer.getclient_id()

        # Create an empty dictionary to store frames
        self.frames = {}

        for F in (Home, Profile, Settings, RequestHistory):  # Add RequestHistory to this list
            page_name = F.__name__
            frame = F(parent=self.root, controller=self, customer=customer)  # Pass customer object as argument
            self.frames[page_name] = frame

            # the different pages are below
            # pages will be stacked and the chosen will be displayed on top
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")
        print(self.frames)

    def show_frame(self, page_name):
        """Show a frame for the chosen page"""
        frame = self.frames[page_name]
        frame.tkraise()
        # if page_name == "RequestHistory":
        #     frame.show_data()


class Home(tk.Frame):
    def __init__(self, parent, controller, customer):
        customer = customer.getclient_id()
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # nav-bar configuration
        self.nav_bar = tk.PanedWindow(self, bg="white")
        self.nav_bar.pack(fill="x", side="top")

        self.Home_btn = tk.Button(self.nav_bar, text="Go to home", command=lambda: controller.show_frame("Home"))

        self.RequestH_btn = tk.Button(self.nav_bar, text="Request History",
                                      command=lambda: controller.show_frame("RequestHistory"))
        self.Profile_btn = tk.Button(self.nav_bar, text="Profile", command=lambda: controller.show_frame("Profile"))
        self.Settings_btn = tk.Button(self.nav_bar, text="Settings", command=lambda: controller.show_frame("Settings"))

        self.Home_btn.grid(row=0, column=0)
        self.Profile_btn.grid(row=0, column=1)
        self.RequestH_btn.grid(row=0, column=2)
        self.Settings_btn.grid(row=0, column=3)

        # map configuration
        # top window
        self.top_pan = tk.PanedWindow(self, bg="black", height=350)
        self.top_pan.pack(fill="x", side="top")

        # form configuration
        # second window
        self.formPanel = tk.PanedWindow(self, )
        self.formPanel.pack(fill="x", expand=1, padx=10)

        def pick_time_click(event):

            self.pick_time_in.config(state="normal")
            if self.pick_time_in.get() == "Arrival Time: ":
                self.pick_time_in.delete(0, END)
            else:
                pass

        def pick_location_click(event):

            self.pick_location_in.config(state="normal")
            if self.pick_location_in.get() == "Arrival Location: ":
                self.pick_location_in.delete(0, END)
            else:
                pass

        # def pick_date_click(event):
        #
        #     self.pick_date_in.config(state="normal")
        #     if self.pick_date_in.get() == "Arrival Date: ":
        #         self.pick_date_in.delete(0, END)
        #     else:
        #         pass

        def destination_click(event):

            self.destination_in.config(state="normal")
            if self.destination_in.get() == "Destination Location: ":
                self.destination_in.delete(0, END)
            else:
                pass

        self.pick_time_in = tk.Entry(self.formPanel, width=100)
        self.pick_time_in.insert(0, "Arrival Time: ")
        self.pick_time_in.config(state="disabled")
        self.pick_time_in.pack(padx=35, pady=15, ipady=2)

        self.pick_time_in.bind("<Button-1>", pick_time_click)

        self.pick_location_in = tk.Entry(self.formPanel, width=100)
        self.pick_location_in.insert(0, "Arrival Location: ")
        self.pick_location_in.config(state="disabled")
        self.pick_location_in.pack(padx=35, pady=15, ipady=2)

        self.pick_location_in.bind("<Button-1>", pick_location_click)

        # self.pick_date_in = tk.Entry(self.formPanel, width=100)
        # self.pick_date_in.insert(0, "Arrival Date: ")
        # self.pick_date_in.config(state="disabled")
        # self.pick_date_in.pack(padx=35, pady=15, ipady=2)
        #
        # self.pick_date_in.bind("<Button-1>", pick_date_click)

        date_today = datetime.now()  # today's date
        max_date = date.today() + timedelta(days=10)
        self.date_entry2 = DateEntry(self.formPanel, selectmode='day', mindate=date_today,
                                     maxdate=max_date, bg="light gray", bd=2)
        self.date_entry2.pack(padx=35, pady=15, ipady=2)

        self.destination_in = tk.Entry(self.formPanel, width=100)
        self.destination_in.insert(0, "Destination Location: ")
        self.destination_in.config(state="disabled")
        self.destination_in.pack(padx=35, pady=15, ipady=2)

        self.destination_in.bind("<Button-1>", destination_click)

        self.request_btn = tk.Button(self.formPanel, text="Request", command=self.request)
        self.request_btn.pack(padx=35, pady=15, ipady=2)

    def request(self):

        pick_up_time = self.pick_time_in.get()
        date_in = self.date_entry2.get_date()
        pick_up_date = date_in.strftime("%Y-%m-%d")  # format to change
        pick_up_location = self.pick_location_in.get()
        drop_location = self.destination_in.get()

        book = Booking()  # set model
        book.setclient_id(client_id)
        book.setpickup_time(pick_up_time)
        book.setpickup_date(pick_up_date)
        book.setpickup_location(pick_up_location)
        book.setdrop_location(drop_location)
        b_book = BBook(book)
        try:
            b_req = b_book.reg_ride()
        except Exception as e:
            messagebox.showerror("Error", "An error occurred while trying to register: {}".format(e))


class RequestHistory(tk.Frame):
    def __init__(self, parent, controller, customer):  # Accept customer object as argument
        tk.Frame.__init__(self, parent)
        self.controller = controller
        customer = customer.getclient_id()  # Store customer object in instance variable

        # nav-bar configuration
        self.nav_bar = tk.PanedWindow(self, bg="white")
        self.nav_bar.pack(fill="x", side="top")

        self.Home_btn = tk.Button(self.nav_bar, text="Go to home", command=lambda: controller.show_frame("Home"))

        self.RequestH_btn = tk.Button(self.nav_bar, text="RequestHistory",
                                      command=lambda: controller.show_frame("RequestHistory"))
        self.Profile_btn = tk.Button(self.nav_bar, text="Profile", command=lambda: controller.show_frame("Profile"))
        self.Settings_btn = tk.Button(self.nav_bar, text="Settings", command=lambda: controller.show_frame("Settings"))

        self.Home_btn.grid(row=0, column=0)
        self.Profile_btn.grid(row=0, column=1)
        self.RequestH_btn.grid(row=0, column=2)
        self.Settings_btn.grid(row=0, column=3)

        self.table_panel = tk.PanedWindow(self)
        self.table_panel.pack(side="top", fill="both", pady=10)

        # label = tk.Label(self.table_panel,text="hello")
        # label.pack()

        # Create a Treeview widget and pack it into the parent widget
        self.table = ttk.Treeview(self.table_panel,
                                  columns=('book_id', 'pickup_time', 'pickup_date', 'pickup_location', 'drop_location'))
        self.table.pack(side='left', fill='both', expand=True)

        # Create a Scrollbar widget and pack it into the parent widget
        scrollbar = ttk.Scrollbar(self.table_panel, orient='vertical', command=self.table.yview)
        scrollbar.pack(side='right', fill='y')

        # Set the Treeview widget's scrollcommand to the Scrollbar widget's set method
        self.table.configure(yscrollcommand=scrollbar.set)

        # Insert column headings into the Treeview widget
        self.table.heading('#0', text='')
        self.table.heading('book_id', text="ID")
        self.table.heading('pickup_time', text='Pickup Time')
        self.table.heading('pickup_date', text='Pickup Date')
        self.table.heading('pickup_location', text='Pickup Location')
        self.table.heading('drop_location', text='Drop Location')

        # book = Booking(self.bpickup_time, self.booking.pickup_date, self.booking.pickup_location,
        #                self.booking.drop_location)
        # b_book = BBook(book)
        # b_book.show_data()
        # Create an instance of the BBook class
        # self.book = BBook(None)
        #
        # # Get the client_id of the logged-in client
        # self.client_id = controller.customer.getclient_id()
        # Call the show_data method of the BBook instance, passing the client_id as an argument
        # Pack the TreeView widget to display it

        book = Booking()
        book.setclient_id(int(client_id))
        b = BBook(book)
        a = b.show_data()
        for i in range(len(a)):
            self.table.insert(parent='', index='end', iid=i, values=(a[i][0], a[i][1], a[i][2], a[i][3], a[i][4], a[i][5]))

        self.table.pack()
        '''table.bind('<Double-Button-1>',self.GetValue())'''

    # def show_data(self):
    #     # Connect to the database
    #     conn = connect_db()
    #     cursor = conn.cursor()
    #
    #     # Execute a SELECT query to retrieve the data for the specified client from the database
    #     sql = "SELECT * FROM booking WHERE cust_id = %s"
    #     values = (
    #         self.getpickup_time,
    #         self.booking.pickup_date, self.booking.pickup_location, self.booking.drop_location)
    #     cursor.execute(sql, values)
    #     rows = cursor.fetchall()
    #
    #     # Clear the table
    #     for i in self.table.get_children():
    #         self.table.delete(i)
    #
    #     # Add the data to the table
    #     for row in rows:
    #         self.table.insert("", "end", values=row)
    #
    #     # Close the connection to the database
    #     conn.close()


class Profile(tk.Frame):
    def __init__(self, parent, controller, customer):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.customer = customer
        # nav-bar configuration
        self.nav_bar = tk.PanedWindow(self, bg="white")
        self.nav_bar.pack(fill="x", side="top")

        self.Home_btn = tk.Button(self.nav_bar, text="Go to home", command=lambda: controller.show_frame("Home"))

        self.RequestH_btn = tk.Button(self.nav_bar, text="Request History",
                                      command=lambda: controller.show_frame("RequestHistory"))
        self.Profile_btn = tk.Button(self.nav_bar, text="Profile", command=lambda: controller.show_frame("Profile"))
        self.Settings_btn = tk.Button(self.nav_bar, text="Settings", command=lambda: controller.show_frame("Settings"))

        self.Home_btn.grid(row=0, column=0)
        self.Profile_btn.grid(row=0, column=1)
        self.RequestH_btn.grid(row=0, column=2)
        self.Settings_btn.grid(row=0, column=3)

        self.label = tk.Label(self, text="Profile", )
        self.label.pack(side="top", fill="x", pady=10)

        # store screen width

        self.top_pan = tk.PanedWindow(self, bg="white")
        self.top_pan.pack(fill="both", expand=True)

        self.name_lb = tk.Label(self.top_pan, text="Name: ", width=80)
        self.name_lb.grid(column=0, row=1, pady=20)

        self.name_in = tk.Entry(self.top_pan, width=80)
        self.name_in.grid(column=2, row=1, pady=15, ipady=4)

        self.num_lb = tk.Label(self.top_pan, text="Phone number: ", width=80)
        self.num_lb.grid(column=0, row=2, pady=20)

        self.num_in = tk.Entry(self.top_pan, width=80)
        self.num_in.grid(column=2, row=2, pady=15, ipady=4)

        self.pass_lb = tk.Label(self.top_pan, text="Password: ", width=80)
        self.pass_lb.grid(column=0, row=3, pady=20)

        self.pass_in = tk.Entry(self.top_pan, width=80)
        self.pass_in.grid(column=2, row=3, pady=15, ipady=4)

        self.change_btn = tk.Button(self.top_pan, text="Change")
        self.change_btn.grid(column=1, row=4, pady=15, ipady=4)


class Settings(tk.Frame):

    def __init__(self, parent, controller, customer):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.customer = customer
        # nav-bar configuration
        self.navigationBar = tk.PanedWindow(self, bg="white")
        self.navigationBar.pack(fill="x", side="top")

        self.Home_btn = tk.Button(self.navigationBar, text="Go to home", command=lambda: controller.show_frame("Home"))

        self.RequestH_btn = tk.Button(self.navigationBar, text="Request History",
                                      command=lambda: controller.show_frame("RequestHistory"))
        self.Profile_btn = tk.Button(self.navigationBar, text="Profile",
                                     command=lambda: controller.show_frame("Profile"))
        self.Settings_btn = tk.Button(self.navigationBar, text="Settings",
                                      command=lambda: controller.show_frame("Settings"))

        self.Home_btn.grid(row=0, column=0)
        self.Profile_btn.grid(row=0, column=1)
        self.RequestH_btn.grid(row=0, column=2)
        self.Settings_btn.grid(row=0, column=3)

        self.label = tk.Label(self, text="This page 2", )
        self.label.pack(side="top", fill="x", pady=10)
