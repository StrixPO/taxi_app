import sys
from tkinter import messagebox
from DatabaseLayer import connection


class BBook:
    def __init__(self, booking):
        self.booking = booking

    def reg_ride(self):
        # Connect to the database
        conn = connection.connect_db()
        cursor = conn.cursor()

        # Execute an INSERT query to insert the booking into the database
        sql = """INSERT INTO booking( pickup_time, pickup_date, pickup_location, drop_location, cust_ID) 
        VALUES (%s,%s,%s,%s,%s)"""
        values = (

            self.booking.getpickup_time(),
            self.booking.getpickup_date(),
            self.booking.getpickup_location(),
            self.booking.getdrop_location(),
            self.booking.getclient_id()
        )
        cursor.execute(sql, values)
        conn.commit()

        # Check if the booking was inserted successfully
        if cursor.rowcount == 1:
            messagebox.showinfo('Done✓', 'Request successful')
        else:
            messagebox.showerror('Error!', 'Failed to make request.')

        # Close the connection to the database
        conn.close()


    def show_data(self):
        conn = None
        sql = """SELECT book_id,pickup_time,pickup_date,pickup_location,drop_location,status FROM booking WHERE 
        cust_ID=%s """
        values = (self.booking.getclient_id(),)
        val = None
        try:
            conn = connection.connect_db()
            cursor = conn.cursor()
            cursor.execute(sql, values)
            content = cursor.fetchall()

            val = content

        except:
            print("Error : ", sys.exc_info())
            messagebox.showerror("Error")
        finally:
            del values
            del sql
            del conn
            return val
