import sys
from tkinter import messagebox
import re
import mysql.connector

from Database import connection
from Models.clientM import Client


class BClient:
    def __init__(self, customer):
        self.customer = customer

    def authenticate_customer(self):
        conn = None
        sql = """SELECT * FROM customer WHERE email = %s and password= %s"""
        values = (self.customer.getemail(), self.customer.getpassword())
        result = {'status': False, 'content': None}
        try:
            conn = connection.conect_db()
            cursor = conn.cursor()
            cursor.execute(sql, values)
            content = cursor.fetchall()
            if len(content) == 0 or content is None:
                result['status'] = False
                messagebox.showerror("no matching value")
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

    import re

    def check_email(self):
        # Connect to the database
        conn = connection.conect_db()
        cursor = conn.cursor()

        # Validate the email address using a regular expression
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(regex, self.customer.getemail()):
            messagebox.showerror("Error", "This email format is wrong")
            return re.match(regex, self.customer.getemail()) is not None

        # Execute a query to check if the email exists
        cursor.execute("SELECT * FROM customer WHERE email=%s", (self.customer.getemail(),))
        result = cursor.fetchone()

        # Close the connection to the database
        conn.close()

        # Return True if the email exists, False otherwise
        return result is not None

    def regcust(self):
        if not self.check_email():
            messagebox.askretrycancel("Error", "Please try again")
            return False

        conn = None
        sql = """INSERT INTO customer(name,number,email, password, address) 
        VALUES (%s,%s,%s,%s,%s) """

        values = (
            self.customer.getname(),
            self.customer.getnumber(),
            self.customer.getemail(),
            self.customer.getpassword(),
            self.customer.getaddress()
        )
        result = False
        try:
            conn = connection.conect_db()
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
            conn.close()
            cursor.close()
            result = True
            messagebox.showinfo('Done✓', 'Registred successfully')

        except mysql.connector.Error as err:
            # Handle connection errors
            print("Error : ", err)
            messagebox.showerror('Error!', 'Unable to connect to the database.')

        except mysql.connector.IntegrityError as err:
            # Handle integrity errors (e.g. unique constraint violations)
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
