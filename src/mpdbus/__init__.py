"""
    @author: Jean-Lou Dupont
"""
from dbus.mainloop.glib import DBusGMainLoop
DBusGMainLoop(set_as_default=True)

from mbus import Bus
import hdbus

class Logger(object):
    def __call__(self, msg):
        print msg

Bus.logger=Logger()
Bus.debug=False

## Order is important here
import track
from main import *

