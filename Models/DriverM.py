class DriverModel(object):
    driver_id = name = number = email = password = license = carmodel = None

    def __init__(self, name=None, address=None, email=None, number=None, password=None, license = None, carmodel =None):
        self.driver_id = 0
        self.name = name
        self.address = address
        self.email = email
        self.number = number
        self.password = password
        self.license = license
        self.carmodel = carmodel

    def getname(self):
        return self.name

    def setname(self, name):
        self.name = name

    def getaddress(self):
        return self.address

    def setaddress(self, address):
        self.address = address

    def getemail(self):
        return self.email

    def setemail(self, email):
        self.email = email

    def getnumber(self):
        return self.number

    def setnumber(self, number):
        self.number = number

    def getpassword(self):
        return self.password

    def setpassword(self, password):
        self.password = password


    def getlicense(self):
        return self.license

    def setlicense(self, license):
        self.license = license


    def getcarmodel(self):
        return self.carmodel

    def setcarmodel(self, carmodel):
        self.carmodel = carmodel


    def getdriver_id(self):
        return self.driver_id

    def setdriver_id(self, driver_id):
        self.driver_id = driver_id

