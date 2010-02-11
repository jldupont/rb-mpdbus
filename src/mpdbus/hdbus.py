"""
    @author: jldupont

    Created on 2010-02-10
"""
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

    def hEntryPlaying(self, _, entry, ed):
        """
        Message Bus handler
        """
        self.TrackChange(ed)

    def sRateCurrentPlaying(self, rating):
        """
        DBus signal handler - /Player/RateCurrentPlaying
        """
        Bus.publish(self, "rate-current", rating)
    

player=hPlayer()
Bus.subscribe("entry-playing", player.hEntryPlaying)
dbus.Bus().add_signal_receiver(player.sRateCurrentPlaying, 
                               signal_name="RateCurrentPlaying", 
                               dbus_interface="org.freedesktop.MediaPlayer", 
                               bus_name=None, 
                               path="/Player")


class hTrack(dbus.service.Object):
    """
    DBus signals for the /Track path
    """
    PATH="/Track"
    
    def __init__(self):
        dbus.service.Object.__init__(self, dbus.SessionBus(), self.PATH)

    @dbus.service.signal(dbus_interface="org.freedesktop.MediaPlayer", signature="a{sv}")
    def Details(self, dic):
        """
        Signal emitter - /Track/Details
        """

    def hEntryChanged(self, _, _entry, ed):
        """
        Just a springboard to the method which generates the DBus signal
        """
        self.Details(ed)
    
    
track=hTrack()
Bus.subscribe("entry-changed", track.hEntryChanged)

