# consumeservice.py
# consumes a method in a service on the dbus

import dbus

bus = dbus.SessionBus()
helloservice = bus.get_object('org.hello.barcodeservice', '/org/hello/helloservice')
hello = helloservice.get_dbus_method('hello', 'org.hello.helloservice')
stoped = helloservice.get_dbus_method('stoped', 'org.stop.stopservice')
print hello()
print stoped()
