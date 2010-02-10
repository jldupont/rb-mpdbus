"""
    @author: jldupont

    Created on 2010-02-09
"""
from mbus import Bus
import rhythmdb, rb #@UnresolvedImport

PLUGIN_NAME="mpdbus"

class MpDBusPlugin (rb.Plugin):
    
    def __init__ (self):
        rb.Plugin.__init__ (self)
        self.current_entry=None
        self.details=None
        self.db=None
        self.changes_count=0
        self._loadcomplete=False

    def activate (self, shell):
        self.shell = shell
        self.db=shell.props.db
        
        sp = shell.get_player ()
        self.spcb = (
                   sp.connect ('playing-song-changed', self.playing_song_changed)
                   ,
                   )
        self.dbcb = (
                      self.db.connect('entry-changed',        self.entry_changed)
                      ,#self.db.connect('load-complete',       self.load_complete) 
                     )
        

    def deactivate (self, shell):
        self.shell = None
        self.db = None
        sp = shell.get_player()
        
        for id in self.spcb:
            sp.disconnect (id)
            
        db=shell.props.db
        for id in self.dbcb:
            db.disconnect (id)

            
    def playing_song_changed (self, sp, entry):
        """
        Just grab the current playing entry
        The rest of the work will be done through the
        event "playing_changed"
        """
        if entry:
            self.current_entry = sp.get_playing_entry()
            ed = EntryHelper.track_details(self.shell, entry)
            Bus.publish(self, "entry-playing", ed)
        

    def load_complete(self, db):
        self._loadcomplete=True

    def entry_changed(self, db, entry, changes):
        """
        Gets triggered on every entry change
        
        Unfortunately, this includes every entry during
        the "startup phase" which consists in scanning
        all the sources of the library
        """
        if entry:
            ed = EntryHelper.track_details(self.shell, entry)
            Bus.publish(self, "entry-changed", ed)



class EntryHelper:
    """
    Helper functions for song database entries
    """
    props = {   "artist":       rhythmdb.PROP_ARTIST
                ,"album":       rhythmdb.PROP_ALBUM
                ,"track":       rhythmdb.PROP_TITLE
                ,"tracknumber": rhythmdb.PROP_TRACK_NUMBER
                ,"genre":       rhythmdb.PROP_GENRE
                ,"location":    rhythmdb.PROP_LOCATION
                ,"duration":    rhythmdb.PROP_DURATION
                ,"mtime":       rhythmdb.PROP_MTIME
                ,"last-seen":   rhythmdb.PROP_LAST_SEEN
                ,"first-seen":  rhythmdb.PROP_FIRST_SEEN
                ,"last-played": rhythmdb.PROP_LAST_PLAYED
                ,"rating":      rhythmdb.PROP_RATING
                ,"playcount":   rhythmdb.PROP_PLAY_COUNT
             }
    
    @classmethod
    def track_details(cls, shell, entry):
        """
        Retrieves details associated with a db entry
        
        @return: (artist, title)
        """
        db = shell.props.db
        result={}
        try:
            for prop, key in cls.props.iteritems():
                result[prop]=db.entry_get(entry, key)
        except:
            pass
        return result
    
