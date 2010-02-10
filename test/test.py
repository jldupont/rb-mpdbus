"""
    @author: jldupont

    Created on 2010-02-10
"""
import gobject
import dbus
import dbus.service

from dbus.mainloop.glib import DBusGMainLoop
DBusGMainLoop(set_as_default=True)


class hPlayer(dbus.service.Object):
    """
    DBus signals for the /Player path
    """
    PATH="/Track"
    
    def __init__(self):
        dbus.service.Object.__init__(self, dbus.SessionBus(), self.PATH)

    @dbus.service.signal(dbus_interface="org.freedesktop.MediaPlayer", signature="ssv")
    def Rating(self, artist, title, rating):
        pass



player=hPlayer()

player.Rating("Depeche Mode", "Little 15", 5.0)


gobject.MainLoop().run()
