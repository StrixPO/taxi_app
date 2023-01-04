# import modules and files
import tkinter as tk
from tkinter import END, font as tkfont


# main base class
class DriverHome(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # main screen where number of frames will be stored
        # the frames shall be interchangable without the need t create a new window
        tk.Tk.minsize(self, width=350, height=650)
        screen = tk.Frame(self)
        screen.pack(side="top", fill="both", expand=True)
        screen.grid_rowconfigure(0, weight=1)
        screen.grid_columnconfigure(0, weight=1)

        # frames list
        self.frames = {}

        for F in (Appointment, Profile, Settings, WorkHistory):
            page_name = F.__name__
            frame = F(parent=screen, controller=self)
            self.frames[page_name] = frame

            # the different pages are below
            # pages will be stacked and the chosen will be displayed on top
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Appointment")

    def show_frame(self, page_name):
        '''Show a frame for the chosen page'''
        frame = self.frames[page_name]
        frame.tkraise()


class Appointment(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # nav-bar configuration
        nav_bar = tk.PanedWindow(self, bg="white")
        nav_bar.pack(fill="x", side="top")

        Appointment_btn = tk.Button(nav_bar, text="Appointment", command=lambda: controller.show_frame("Appointment"))
        WorkH_btn = tk.Button(nav_bar, text="WorkHistory", command=lambda: controller.show_frame("WorkHistory"))
        Profile_btn = tk.Button(nav_bar, text="Profile", command=lambda: controller.show_frame("Profile"))
        Settings_btn = tk.Button(nav_bar, text="Settings", command=lambda: controller.show_frame("Settings"))

        Appointment_btn.grid(row=0, column=0)
        Profile_btn.grid(row=0, column=1)
        WorkH_btn.grid(row=0, column=2)
        Settings_btn.grid(row=0, column=3)

        # map configuration
        # top window
        top_pan = tk.PanedWindow(self, bg="black", height=350)
        top_pan.pack(fill="x", side="top")

        # form configuration
        # second window
        sec_pan = tk.PanedWindow(self, )
        sec_pan.pack(fill="x", expand=1, padx=10)

        def pickT_click(event):

            pickTime_in.config(state="normal")
            if pickTime_in.get() == "Arrival Time: ":
                pickTime_in.delete(0, END)
            else:
                pass

        def pickL_click(event):

            pickLocation_in.config(state="normal")
            if pickLocation_in.get() == "Arrival Location: ":
                pickLocation_in.delete(0, END)
            else:
                pass

        def destination_click(event):

            destination_in.config(state="normal")
            if destination_in.get() == "Destination Location: ":
                destination_in.delete(0, END)
            else:
                pass

        pickTime_in = tk.Entry(sec_pan, width=100)
        pickTime_in.insert(0, "Arrival Time: ")
        pickTime_in.config(state="disabled")
        pickTime_in.pack(padx=35, pady=15, ipady=2)

        pickTime_in.bind("<Button-1>", pickT_click)

        pickLocation_in = tk.Entry(sec_pan, width=100)
        pickLocation_in.insert(0, "Destination Location: ")
        pickLocation_in.config(state="disabled")
        pickLocation_in.pack(padx=35, pady=15, ipady=2)

        pickLocation_in.bind("<Button-1>", pickL_click)

        destination_in = tk.Entry(sec_pan, width=100)
        destination_in.insert(0, "Enter your email address: ")
        destination_in.config(state="disabled")
        destination_in.pack(padx=35, pady=15, ipady=2)

        # def show():
        #     text = clicked.get()
        #     controller.show_frame(text)

        # menu_options = [
        #     "Profile",
        #     "RequestHistory",
        #     "Ssettings"
        # ]

        # clicked = tk.StringVar()

        # drop = tk.OptionMenu(self, clicked, *menu_options,command=show())
        # drop.pack()


class WorkHistory(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Request History", )
        label.pack(side="top", fill="x", pady=10)


class Profile(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # nav-bar configuration
        nav_bar = tk.PanedWindow(self, bg="white")
        nav_bar.pack(fill="x", side="top")

        Home_btn = tk.Button(nav_bar, text="Go to home", command=lambda: controller.show_frame("Home"))

        RequestH_btn = tk.Button(nav_bar, text="Request History",
                                 command=lambda: controller.show_frame("RequestHistory"))
        Profile_btn = tk.Button(nav_bar, text="Profile", command=lambda: controller.show_frame("Profile"))
        Settings_btn = tk.Button(nav_bar, text="Settings", command=lambda: controller.show_frame("Settings"))

        Home_btn.grid(row=0, column=0)
        Profile_btn.grid(row=0, column=1)
        RequestH_btn.grid(row=0, column=2)
        Settings_btn.grid(row=0, column=3)

        label = tk.Label(self, text="This page 1", )
        label.pack(side="top", fill="x", pady=10)

        # store screen width

        top_pan = tk.PanedWindow(self, bg="white")
        top_pan.pack(fill="both", expand=True)

        screen_width = top_pan.winfo_screenwidth() // 2

        main_lb = tk.Label(top_pan, text="Profile", width=40)
        main_lb.grid(column=1, row=0, pady=35)

        name_lb = tk.Label(top_pan, text="Name: ", width=80)
        name_lb.grid(column=0, row=1, pady=20)

        name_in = tk.Entry(top_pan, width=80)
        name_in.grid(column=2, row=1, pady=15, ipady=4)

        num_lb = tk.Label(top_pan, text="Phone number: ", width=80)
        num_lb.grid(column=0, row=2, pady=20)

        num_in = tk.Entry(top_pan, width=80)
        num_in.grid(column=2, row=2, pady=15, ipady=4)

        pass_lb = tk.Label(top_pan, text="Password: ", width=80)
        pass_lb.grid(column=0, row=3, pady=20)

        pass_in = tk.Entry(top_pan, width=80)
        pass_in.grid(column=2, row=3, pady=15, ipady=4)

        carmodel_lb = tk.Label(top_pan, text="Car Model: ", width=80)
        carmodel_lb.grid(column=0, row=4, pady=20)

        carmodel_in = tk.Entry(top_pan, width=80)
        carmodel_in.grid(column=2, row=4, pady=15, ipady=4)

        lisence_lb = tk.Label(top_pan, text="Lisence Number: ", width=80)
        lisence_lb.grid(column=0, row=5, pady=20)

        lisence_in = tk.Entry(top_pan, width=80)
        lisence_in.grid(column=2, row=5, pady=15, ipady=4)


class Settings(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This page 2", )
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to home",
                           command=lambda: controller.show_frame("Home"))
        button.pack()


if __name__ == "__main__":
    app = DriverHome()
    app.mainloop()








