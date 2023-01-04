class Client(object):
    client_id = name = address = email = number = password = None

    def __init__(self, name=None, address=None, email=None, number=None, password=None):
        self.client_id = 0
        self.name = name
        self.address = address
        self.email = email
        self.number = number
        self.password = password

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

    def getclient_id(self):
        return self.client_id

    def setclient_id(self, client_id):
        self.client_id = client_id

