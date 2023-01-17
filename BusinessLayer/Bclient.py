# import system modules
import sys
from tkinter import messagebox
import re

import mysql.connector

# import file modules
from DatabaseLayer import connection


class BClient:
    # initialization
    def __init__(self, client):
        self.client = client

    # check the validity of email while registering
    def is_valid_email(self):
        regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(regex, self.client.getemail()):
            return True
        return False

    # function for storing client data
    def register_client(self):
        # Check if email is in a valid format
        if not self.is_valid_email():
            messagebox.showerror('Error!', 'Format is wrong!!')
            return False

        conn = None
        sql = """INSERT INTO customer(name,number,email, password, address) 
                VALUES (%s,%s,%s,%s,%s) """

        values = (
            self.client.getname(),
            self.client.getnumber(),
            self.client.getemail(),
            self.client.getpassword(),
            self.client.getaddress()
        )
        result = False
        try:
            conn = connection.connect_db()
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
            conn.close()
            cursor.close()
            result = True
            messagebox.showinfo('Done✓', 'Registred successfully')

        except mysql.connector.Error as err:
            print("ERROR : ", err)
            messagebox.showerror('Error!', 'Unable to connect to the database.')

        except mysql.connector.IntegrityError as err:
            # Handle integrity errors (e.g. unique constraint violations)
            conn = connection.connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM customer WHERE email=%s", (self.client.getemail(),))
            result = cursor.fetchone()
            print("Error : ", err)
            messagebox.showerror('Error!', 'Unable to Register or Email already Exist.')

        except:
            # Catch all other exceptions
            print("Error : ", sys.exc_info())
            messagebox.showerror('Error!', 'An unexpected error occurred.')
        finally:
            del values
            del sql
            return result

    # function connected to login page for verifying client identity
    def authenticate_client(self):
        conn = None
        sql = """SELECT * FROM customer WHERE email = %s and password= %s"""
        values = (self.client.getemail(), self.client.getpassword())
        result = {'status': False, 'content': None}
        try:
            conn = connection.connect_db()
            cursor = conn.cursor()
            cursor.execute(sql, values)
            content = cursor.fetchall()
            if len(content) == 0 or content is None:
                result['status'] = False
                messagebox.showerror("ERROR!", "Email and password cannot be empty!!")
            else:
                result['status'] = True
                result['content'] = content
        except mysql.connector.Error as err:
            result['status'] = False
            result['content'] = str(err)
        except Exception as e:
            result['status'] = False
            result['content'] = str(e)
        finally:
            if conn is not None and conn.is_connected():
                conn.close()
            del values
            del sql
            return result

    def view_all_client(self):

        conn = None
        sql = """SELECT * FROM customer"""
        # values = (self.booking.getclient_id(),)
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
