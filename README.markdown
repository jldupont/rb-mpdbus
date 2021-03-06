README
======

This project consists of a Rhythmbox plugin which adds support for DBus signals of the 
interface "org.freedesktop.MediaPlayer" with some extensions.

Features
========

Generates the following signals on DBus from the "interface=org.freedesktop.MediaPlayer":

TrackChange Signal:
-------------------

This signal is supported by Amarok (and probably others) already. 
The following is emitted whenever the current playing track is changed. 

- Path: /Player
  - Member: TrackChange
    - sig: a{sv}
      - "album", "artist", "title", "tracknumber", "genre", 
        "location", "duration",
        "mtime", "last-seen", "last-played",
        "rating", "playcount"
      
Extension: The parameters "playcount", "last-seen" and "last-played" are added to the output dictionary (array).
Listeners on the signal should be sufficiently flexible as to ignore the parameters which they cannot interpret. 

Track Rating Support:
---------------------

The rating of the currently playing track can be changed using the following signal:

- Path: /Player
  - Member: RateCurrentPlaying
    - sig: "v"  ( a float rating value either in string or float format representation )
   

Track Details Support:
----------------------

This section details extensions to the MediaPlayer protocol. 

The following signal is emitted whenever the details for a track is changed by the user.
   
- Path: /Track
  - Member: Details
    - sig: a{sv}
      - "album", "artist", "title", "tracknumber", "genre", 
        "location", "duration",
        "mtime", "last-seen", "last-played",
        "rating", "playcount"



Installation
============
There are 2 methods:

1. Use the Ubuntu Debian repository [jldupont](https://launchpad.net/~jldupont/+archive/jldupont)  with the package "rbsynclastfm"

2. Use the "Download Source" function of this git repo and use "sudo make install"

Dependencies
============

* DBus python bindings


Future
======

Integration of more signals ( check-out the Totem mpris plugin )
