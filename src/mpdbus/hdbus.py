"""
    @author: jldupont

    Created on 2010-02-10
"""
import dbus
import dbus.service
from mbus import Bus


class hPlayer(dbus.service.Object):
    """
    DBus signals for the /Player path
    """
    PATH="/Player"
    
    def __init__(self):
        dbus.service.Object.__init__(self, dbus.SessionBus(), self.PATH)

    @dbus.service.signal(dbus_interface="org.freedesktop.MediaPlayer", signature="a{sv}")
    def TrackChange(self, dic):
        pass

    def hEntryPlaying(self, _, ed):
        self.TrackChange(ed)


player=hPlayer()
Bus.subscribe("entry-playing", player.hEntryPlaying)


class hTrack(dbus.service.Object):
    """
    DBus signals for the /Track path
    """
    PATH="/Track"
    
    def __init__(self):
        dbus.service.Object.__init__(self, dbus.SessionBus(), self.PATH)

    @dbus.service.signal(dbus_interface="org.freedesktop.MediaPlayer", signature="a{sv}")
    def Details(self, dic):
        pass
    
    def Rating(self, artist, title, rating):
        """
        Rating Signal
        """
        print ">>> RATING: artist(%s) title(%s) rating(%s)" % (artist, title, rating)

    def hEntryChanged(self, _, ed):
        self.Details(ed)

    
track=hTrack()
Bus.subscribe("entry-changed", track.hEntryChanged)

## Subscribe to the "/Track/Rating" signal
dbus.Bus().add_signal_receiver(track.Rating, signal_name="Rating", dbus_interface="org.freedesktop.MediaPlayer", bus_name=None, path="/Track")