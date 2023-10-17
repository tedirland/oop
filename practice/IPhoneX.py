from IPhone import IPhone


class IPhoneX(IPhone):
    def __init__(self, carrier, contacts):
        self.facial_id = True
        super().__init__("iPhoneX", carrier, contacts)
    
    def show_facial_id(self):
        print("Running facial ID")
    
    def open_app_store(self):
        print("This is the Apple App Store for IPhone X")