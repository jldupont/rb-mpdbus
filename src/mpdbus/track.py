"""
    @author: jldupont

    Created on 2010-02-10
"""
from mbus import Bus
import rhythmdb  #@UnresolvedImport


class TrackHelper(object):
    
    def hDb(self, _, db):
        self.db=db
        
    def findTrackEntry(self, artist, title):
        """
        Finds a specific track (artist, title)
        in the database and returns the corresponding
        db Entry
        """
        query = self.db.query_new()
        self.db.query_append(query, [rhythmdb.QUERY_PROP_EQUALS, rhythmdb.PROP_TYPE, self.db.entry_type_get_by_name('song')]
                                    ,[rhythmdb.QUERY_PROP_EQUALS, rhythmdb.PROP_ARTIST, artist]
                                    ,[rhythmdb.QUERY_PROP_EQUALS, rhythmdb.PROP_TITLE, title]
                                    )
        tracksQuery=self.db.query_model_new(query)
        self.db.do_full_query_async_parsed(tracksQuery, query)
        
    def setRating(self, entry, rating):
        """
        Sets the "rating" parameter associated with an entry
        """
        if not entry: #paranoia
            print "setRating: invalid entry supplied"
            return
        
        ## float(5.0) == float("5.0")
        ##  another reason why I love Python
        try:    
            fvalue=float(rating)
            self.db.set(entry, rhythmdb.PROP_RATING, fvalue)
            print "setRating: rating(%s)" % fvalue
        except Exception,e:
            print "setRating: expecting a float for 'rating', got: %s" % rating
            print "setRating: exception(%s)" % str(e)
        
    def setRatings(self, entries, rating):
        """
        Set the rating of a batch of entries
        """
        def _rate(model, _path, iter):
            entry=model.get(iter, 0)[0]
            self.db.set(entry, rhythmdb.PROP_RATING, rating)
            
        entries.foreach(_rate)

    
th=TrackHelper()
Bus.subscribe("db",     th.hDb)
    
    

class TrackHandler(object):
    def __init__(self, trackHelper):
        self.th=trackHelper
        self.currentEntry=None
    
    def hEntryPlaying(self, _, entry, _entryDic):
        """
        Intercepts the current playing entry
        """
        self.currentEntry=entry

    def hRateCurrent(self, _, rating):
        """
        Apply a 'rating' to the currently playing track
        """
        self.th.setRating(self.currentEntry, rating)
    
    """
    def hRating(self, _, artist, title, rating):
        pass
    """
    
    
thdl=TrackHandler(th)
##Bus.subscribe("track-rating", thdl.hRating)
Bus.subscribe("entry-playing", thdl.hEntryPlaying)
Bus.subscribe("rate-current",  thdl.hRateCurrent)

