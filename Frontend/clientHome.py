# import modules and files
import tkinter as tk
from tkinter import END


# main base class
class ClientHome:
    def __init__(self, name):
        self.name = name
        # Initialize the object as a Tkinter frame
        # Set the minimum size of the window
        self.root = tk.Tk()
        # Create a frame to hold other widgets
        self.root.minsize(width=550, height=400)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Create an empty dictionary to store frames
        self.frames = {}

        for F in (Home, Profile, Settings, RequestHistory):
            page_name = F.__name__
            frame = F(parent=self.root, controller=self)
            self.frames[page_name] = frame

            # the different pages are below
            # pages will be stacked and the chosen will be displayed on top
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")

    def show_frame(self, page_name):
        """Show a frame for the chosen page"""
        frame = self.frames[page_name]
        frame.tkraise()


class Home(tk.Frame):
    def __init__(self, parent, controller):
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
        self.pick_location_in.insert(0, "Destination Location: ")
        self.pick_location_in.config(state="disabled")
        self.pick_location_in.pack(padx=35, pady=15, ipady=2)

        self.pick_location_in.bind("<Button-1>", pick_location_click)

        self.destination_in = tk.Entry(self.formPanel, width=100)
        self.destination_in.insert(0, "Enter your email address: ")
        self.destination_in.config(state="disabled")
        self.destination_in.pack(padx=35, pady=15, ipady=2)

        self.destination_in.bind("<Button-1>", destination_click)


class RequestHistory(tk.Frame):
    def __init__(self, parent, controller):
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

        self.label = tk.Label(self, text="This is Request History", )
        self.label.pack(side="top", fill="x", pady=10)


class Profile(tk.Frame):
    def __init__(self, parent, controller):
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

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

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
