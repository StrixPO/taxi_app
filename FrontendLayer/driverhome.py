# import system modules
import tkinter as tk
from tkinter import ttk

# import directory modules
from BusinessLayer.Bbook import BBook
from Models.BookingM import Booking

did = 0


class DriverHome:

    def __init__(self, driver):
        global did

        # Initialize the object as a Tkinter frame
        # Set the minimum size of the window
        self.root = tk.Tk()
        # Create a frame to hold other widgets
        self.root.minsize(width=550, height=400)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.config(bg="#62929e")
        did = driver.getdriver_id()

        self.table_panel = tk.PanedWindow(self.root)
        self.table_panel.pack(side="top", fill="both", pady=40, padx=40)
        self.table_panel.config(bg="#62929e")

        # Create a Treeview widget and pack it into the parent widget
        self.table = ttk.Treeview(self.table_panel,
                                  columns=(
                                      'client_id', 'pickup_time', 'pickup_date', 'pickup_location', 'drop_location',))
        self.table.pack(side='left', fill='both', expand=True)

        # Create a Scrollbar widget and pack it into the parent widget
        scrollbar = ttk.Scrollbar(self.table_panel, orient='vertical', command=self.table.yview)
        scrollbar.pack(side='right', fill='y')

        # Set the Treeview widget's scrollcommand to the Scrollbar widget's set method
        self.table.configure(yscrollcommand=scrollbar.set)

        # Insert column headings into the Treeview widget

        self.table.heading('client_id', text="Client ID", )
        self.table.heading('pickup_time', text='Pickup Time')
        self.table.heading('pickup_date', text='Pickup Date')
        self.table.heading('pickup_location', text='Pickup Location')
        self.table.heading('drop_location', text='Drop Location')

        book = Booking()
        book.setdriver_id(did)
        b = BBook(book)
        a = b.driver_show_data()

        #    loop for data insertion
        for i in range(len(a)):
            self.table.insert(parent='', index='end', values=(a[i][4], a[i][0], a[i][1], a[i][2], a[i][3]))

        self.table.pack()
