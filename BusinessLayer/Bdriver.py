# import system modules
import sys
from tkinter import messagebox
import mysql.connector
import  re

# import file modules
from DatabaseLayer import connection


class BDriver:
    # initiallization
    def __init__(self, driver):
        self.driver = driver

    def is_valid_email(self):
        regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(regex, self.driver.getemail()):
            return True
        return False


    # function for storing Driver data
    def register_driver(self):

        if not self.is_valid_email():
            messagebox.showerror('Error!', 'Invalid email format.')
            return False

        conn = None
        sql = """INSERT INTO driver(name,number,address, email, password, lisence_plate, car_model ) 
                VALUES (%s,%s,%s,%s,%s,%s,%s) """

        values = (
            self.driver.getname(),
            self.driver.getnumber(),
            self.driver.getaddress(),
            self.driver.getemail(),
            self.driver.getpassword(),
            self.driver.getlicense(),
            self.driver.getcarmodel()
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
            messagebox.showinfo('Done✓', 'Registered successfully')

        except mysql.connector.Error as err:
            print("ERROR : ", err)
            messagebox.showerror('Error!', 'Unable to connect to the database.')

        except mysql.connector.IntegrityError as err:
            # Handle integrity errors (e.g. unique constraint violations)
            conn = connection.connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM customer WHERE email=%s", (self.driver.getemail(),))
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

    # function connected to login page for verifying driver identity
    def authenticate_driver(self):
        conn = None
        sql = """SELECT * FROM driver WHERE email = %s and password= %s"""
        values = (self.driver.getemail(), self.driver.getpassword())
        result = {'status': False, 'content': None}
        try:
            conn = connection.connect_db()
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
