import sys
from tkinter import messagebox

import mysql.connector

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
        sql = """SELECT book_id, pickup_time, pickup_date, pickup_location, drop_location FROM booking WHERE 
        cust_ID=%s """
        values = (self.booking.getclient_id(),)
        val = None
        try:
            conn = connection.connect_db()
            cursor = conn.cursor()
            cursor.execute(sql, values)
            content = cursor.fetchall()
            conn.close()
            # Add the data to the table

            val = content

        except:
            print("Error : ", sys.exc_info())
            messagebox.showerror("Error")
        finally:
            del values
            del sql
            del conn
            return val

    def driver_show_data(self):
        conn = None
        val = None
        try:
            conn = connection.connect_db()
            cursor = conn.cursor()
            sql = """SELECT pickup_time, pickup_date, pickup_location, drop_location,cust_ID FROM booking WHERE 
                   driver_id=%s """
            values = (self.booking.getdriver_id(),)
            cursor.execute(sql, values)
            content = cursor.fetchall()
            print(content)
            conn.close()
            # Add the data to the table

            val = content

        except:
            print("Error : ", sys.exc_info())
            messagebox.showerror("Error")
        finally:
            del values
            del sql
            del conn
            return val

    def updatebook(self):
        conn = None
        result = False
        try:
            conn = connection.connect_db()
            cursor = conn.cursor()
            sql = "Update  booking set pickup_time= %s, pickup_date= %s, pickup_location= %s, drop_location= %s where " \
                  "book_id = %s "
            values = (
                self.booking.getpickup_time(),
                self.booking.getpickup_date(),
                self.booking.getpickup_location(),
                self.booking.getdrop_location(),
                self.booking.getbook_id()
            )
            cursor.execute(sql, values)
            conn.commit()

            result = True
            messagebox.showinfo('Done!', 'Your booking has been updated successfully')
        except mysql.connector.Error as e:
            messagebox.showerror('Error!', 'Booking Already exists.')
        except:
            messagebox.showerror('Error!', 'Unable to update. Please fill in the booking details.')
        finally:
            conn.close()
            return result

    def cancelbook(self):
        conn = None
        sql = " delete from booking where book_id = %s"
        values = (self.booking.getbook_id(),)
        result = False
        try:
            conn = connection.connect_db()
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
            conn.close()
            cursor.close()
            result = True
            messagebox.showinfo('Done!', 'Your booking has been cancelled')

        except:
            print("Error : ", sys.exc_info())
            messagebox.showerror('Error!', 'Unable to cancel.')
        finally:
            del values
            del sql
            return result

    def show_admin_table(self):
        conn = None
        sql = "SELECT * FROM booking"
        val = None
        try:
            conn = connection.connect_db()
            cursor = conn.cursor()
            cursor.execute(sql)
            content = cursor.fetchall()
            conn.close()
            # Add the data to the table

            val = content

        except:
            print("Error : ", sys.exc_info())
            messagebox.showerror("Error")
        finally:
            # del values
            del sql
            del conn
            return val

    def assign_driver(self):
        conn = None
        result = False
        try:
            conn = connection.connect_db()
            cursor = conn.cursor()
            sql = "Update  booking set driver_id= %s where " \
                  "book_id = %s "
            values = (
                self.booking.getdriver_id(),
                self.booking.getbook_id()

            )

            cursor.execute(sql, values)
            conn.commit()

            result = True
            messagebox.showinfo('Done!', 'Driver has been assigned')
        except mysql.connector.Error as e:

            messagebox.showerror('Error!', 'Booking Already exists.')
        except:
            messagebox.showerror('Error!', 'Unable to update. Please fill in the booking details.')
        finally:
            conn.close()
            return result
