

# An iphone is always a phone
# How do we make this a subclass of phone
# we want the methods and attributes that phones have
# we pass the parent of super class to the ()
from Phone import Phone

class IPhone(Phone):
    def __init__(self, model, carrier,contacts):
        self.os = "iOS"
        self.make = "Apple"

        super().__init__(self.make, model , carrier, self.os, contacts )
        # super = the parent class
      

    def open_facetime(self):
        print("Opening facetime...")

    # overriding = allows us to override a method from a parent / super class

    def open_app_store(self):
        print("This is the Apple App Store")
    
    
        