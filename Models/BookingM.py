class Booking(object):
    book_id = client_id = pickup_time = pickup_date = pickup_location = drop_location = None

    def __init__(self, pickup_time=None, pickup_date=None, pickup_location=None, drop_location=None):
        self.book_id = 0
        self.client_id = 0
        self.pickup_time = pickup_time
        self.pickup_date = pickup_date
        self.pickup_location = pickup_location
        self.drop_location = drop_location

    def getpickup_time(self):
        return self.pickup_time

    def setpickup_time(self, pickup_time):
        self.pickup_time = pickup_time

    def getpickup_date(self):
        return self.pickup_date

    def setpickup_date(self, pickup_date):
        self.pickup_date = pickup_date

    def getpickup_location(self):
        return self.pickup_location

    def setpickup_location(self, pickup_location):
        self.pickup_location = pickup_location

    def getdrop_location(self):
        return self.drop_location

    def setdrop_location(self, drop_location):
        self.drop_location = drop_location

    def getbook_id(self):
        return self.book_id

    def setbook_id(self, book_id):
        self.book_id = book_id

    def getclient_id(self):
        return self.client_id

    def setclient_id(self, client_id):
        self.client_id = client_id
