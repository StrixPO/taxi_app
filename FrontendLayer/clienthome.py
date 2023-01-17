# import system modules
import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from datetime import datetime, timedelta, date
from tkinter import END
from PIL import ImageTk, Image

# import file modules
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

        for F in (Home, ChangeBooking, RequestHistory):  # Add RequestHistory to this list
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


class Home(tk.Frame):  # first frame
    def __init__(self, parent, controller, customer):  # initialization
        customer = customer.getclient_id()  # gain access to customer Id for specified results
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # nav-bar configuration
        self.nav_bar = tk.PanedWindow(self, bg="white")
        self.nav_bar.pack(fill="x", side="top")

        self.Home_btn = tk.Button(self.nav_bar, text="Home", command=lambda: controller.show_frame("Home"))

        self.RequestH_btn = tk.Button(self.nav_bar, text="Request History",
                                      command=lambda: controller.show_frame("RequestHistory"))
        self.Change_btn = tk.Button(self.nav_bar, text="Change Booking", command=lambda: controller.show_frame("ChangeBooking"))

        self.Home_btn.grid(row=0, column=0)
        self.Change_btn.grid(row=0, column=1)
        self.RequestH_btn.grid(row=0, column=2)

        # map configuration
        # top window
        self.top_pan = tk.PanedWindow(self, bg="black", height=350)
        self.top_pan.pack(fill="x", side="top")

        self.top_pan.bg = ImageTk.PhotoImage(file="FrontendLayer/Images/map.jpg")
        self.bg_image = tk.Label(self.top_pan, image=self.top_pan.bg)
        self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)
        # form configuration
        # second window
        self.formPanel = tk.PanedWindow(self, )
        self.formPanel.pack(fill="x", expand=1, padx=10)
        self.formPanel.config(bg="white")

        # series of click events
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

        def destination_click(event):

            self.destination_in.config(state="normal")
            if self.destination_in.get() == "Destination Location: ":
                self.destination_in.delete(0, END)
            else:
                pass

        # Entries for request data
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

    #   function for Request ride
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


class RequestHistory(tk.Frame):  # second frame
    def __init__(self, parent, controller, customer):  # Accept customer object as argument
        tk.Frame.__init__(self, parent)
        self.controller = controller
        customer = customer.getclient_id()  # Store customer object in instance variable

        # nav-bar configuration
        self.nav_bar = tk.PanedWindow(self, bg="white")
        self.nav_bar.pack(fill="x", side="top")

        self.Home_btn = tk.Button(self.nav_bar, text="Home", command=lambda: controller.show_frame("Home"))

        self.RequestH_btn = tk.Button(self.nav_bar, text="RequestHistory",
                                      command=lambda: controller.show_frame("RequestHistory"))
        self.Change_btn = tk.Button(self.nav_bar, text="Change Booking", command=lambda: controller.show_frame("ChangeBooking"))

        self.Home_btn.grid(row=0, column=0)
        self.Change_btn.grid(row=0, column=1)
        self.RequestH_btn.grid(row=0, column=2)

        self.table_panel = tk.PanedWindow(self)
        self.table_panel.pack(side="top", fill="both", pady=40, padx=40)
        self.table_panel.config(bg="#62929e")

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

        self.table.heading('book_id', text="ID", )
        self.table.heading('pickup_time', text='Pickup Time')
        self.table.heading('pickup_date', text='Pickup Date')
        self.table.heading('pickup_location', text='Pickup Location')
        self.table.heading('drop_location', text='Drop Location')

        book = Booking()
        book.setclient_id(customer)
        b = BBook(book)
        a = b.show_data()

        #    loop for data insertion
        for i in range(len(a)):
            self.table.insert(parent='', index='end', values=(a[i][0], a[i][1], a[i][2], a[i][3], a[i][4]))

        self.table.pack()

        # # self.table.bind('<Double-Button-1>',self.GetValue())


class ChangeBooking(tk.Frame):  # third frame
    def __init__(self, parent, controller, customer):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.customer = customer
        self.config(bg="#62929e")
        # nav-bar configuration
        self.nav_bar = tk.PanedWindow(self, bg="white")
        self.nav_bar.pack(fill="x", side="top")

        self.Home_btn = tk.Button(self.nav_bar, text="Home", command=lambda: [controller.show_frame("Home")])
        self.RequestH_btn = tk.Button(self.nav_bar, text="Request History",
                                      command=lambda: [controller.show_frame("RequestHistory")])
        self.Change_btn = tk.Button(self.nav_bar, text="Change Booking", command=lambda: controller.show_frame("ChangeBooking"))

        self.Home_btn.grid(row=0, column=0)
        self.Change_btn.grid(row=0, column=1)
        self.RequestH_btn.grid(row=0, column=2)


        # form configuration
        # second window
        self.formPanel = tk.PanedWindow(self, )
        self.formPanel.pack(fill="both", expand=1, padx=40, pady=20, ipady=30)
        self.formPanel.config(bg="white")

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

        def destination_click(event):

            self.destination_in.config(state="normal")
            if self.destination_in.get() == "Destination Location: ":
                self.destination_in.delete(0, END)
            else:
                pass

        def book_click(event):

            self.bookid_in.config(state="normal")
            if self.bookid_in.get() == "Booking ID: ":
                self.bookid_in.delete(0, END)
            else:
                pass

        self.bookid_in = tk.Entry(self.formPanel, width=100)
        self.bookid_in.insert(0, "Booking ID: ")
        self.bookid_in.config(state="disabled")
        self.bookid_in.pack(padx=35, pady=15, ipady=2)

        self.bookid_in.bind("<Button-1>", book_click)

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

        self.update_btn = tk.Button(self.formPanel, text="UPDATE", command=self.update)
        self.update_btn.pack(padx=35, pady=15, ipady=2, )

        self.cancel_btn = tk.Button(self.formPanel, text="CANCEL", command=self.cancel)
        self.cancel_btn.pack(padx=35, pady=15, ipady=2)

    # function to update booking details
    def update(self):
        booking_id = self.bookid_in.get()
        pick_up_time = self.pick_time_in.get()
        date_in = self.date_entry2.get_date()
        pick_up_date = date_in.strftime("%Y-%m-%d")  # format to change
        pick_up_location = self.pick_location_in.get()
        drop_location = self.destination_in.get()

        tripdetail = Booking()
        tripdetail.setpickup_time(pick_up_time)
        tripdetail.setpickup_date(pick_up_date)
        tripdetail.setpickup_location(pick_up_location)
        tripdetail.setdrop_location(drop_location)
        tripdetail.setbook_id(booking_id)

        ub = BBook(tripdetail)
        upbook = ub.updatebook()

    # function for cancel // delete booking
    def cancel(self):
        booking_id = self.bookid_in.get()

        tripdetail = Booking()
        tripdetail.setbook_id(booking_id)
        ub = BBook(tripdetail)
        upbook = ub.cancelbook()
