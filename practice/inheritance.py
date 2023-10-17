# Inheritance is a way in OOP to allow one class to have all the methods and attributes of another

from Phone import Phone
from IPhone import IPhone
from IPhoneX import IPhoneX

jims_phone = Phone('Samsung',"Galaxy S9", "Verizon", "Android", ["Jamie"])
cedricks_phone = Phone('Google',"Pixel 7 Pro", 'EE', "Android", ["Jamie", "Javier"])
konstantins_phone = IPhone("iphone 13","Vodaphone", [])
marias_phone = IPhoneX("AT&T", ["Jose", "David" ])

print(jims_phone.make)


print(cedricks_phone.contacts)
cedricks_phone.call_first_contact()
print(konstantins_phone.carrier)

konstantins_phone.call_first_contact()

konstantins_phone.open_facetime()


marias_phone.call_first_contact()
marias_phone.open_facetime()
marias_phone.show_facial_id()

marias_phone.open_app_store()