import sys
from tkinter import messagebox

import mysql.connector
import self as self

from Database import connection
from Models import clientM


class Bclient():
    def __init__(self, customer):
        self.customer = customer

    import mysql.connector

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
                result['content'] = 'No matching email and password found.'
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

    def regcust(self):
        conn = None
        sql = """INSERT INTO customer(name,number,email, password, address) 
        VALUES (%s,%s,%s,%s,%s) """

        values = (
            self.customer.getname(),
            self.customer.getaddress(),
            self.customer.getemail(),
            self.customer.getnumber(),
            self.customer.getpassword()
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
