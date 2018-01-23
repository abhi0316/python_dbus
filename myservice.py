
import gtk
import sys
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
count=0
print sys.argv[1]
class MyDBUSService(dbus.service.Object):
    def __init__(self):
        bus_name = dbus.service.BusName('org.hello.helloservice', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/org/hello/helloservice')

    @dbus.service.method('org.hello.helloservice')
    def hello(self,var):
       	return var
    @dbus.service.method('org.stop.stopservice')
    def stoped(self):
	return "stopped"
DBusGMainLoop(set_as_default=True)
myservice = MyDBUSService()
gtk.main()

