README
======

This project consists of a Rhythmbox plugin which adds support for DBus signals of the 
interface "org.freedesktop.MediaPlayer" with some extensions.

Roadmap
=======

Version 1.x : support for emitting "TrackChange" and "/Track/Details" signals on user event

Version 2.x : support for emitting "/Track/Details" signal on "/Track/Details?" signal

Features
========

Generates the following signals on DBus from the "interface=org.freedesktop.MediaPlayer":

Supported by Amarok:
--------------------

The following is emitted whenever the current playing track is changed. 

- Path: /Player
  - Member: TrackChange
    - out sig: a{sv}
      - "album", "artist", "title", "tracknumber", "genre", 
        "location", "duration",
        "mtime", "last-seen", "last-played",
        "rating", "playcount"
      
Extension: The parameter "playcount" is added to the output dictionary (array).

Track Details Support:
----------------------

This section details extensions to the MediaPlayer protocol. 

The following signal is emitted whenever the details for a track is changed by the user.
   
- Path: /Track
  - Member: Details
    - out sig: a{sv}
      - "album", "artist", "location", "mtime", "rating", "title", "tracknumber", "playcount"


The plugin subscribes to the following signal:

- Path: /Tracks
  - Member: Details?
    - sig:  "ii"  (uts_start, max_tracks)
    
The plugin responds to the "/Tracks/Details?" signal using a succession of "/Track/Details" signals.
The usage of signals instead of "method calls" and "replies" is to enable other subscribers on DBus
to easily leverage the information exchanged.


Installation
============
There are 2 methods:

1. Use the Ubuntu Debian repository [jldupont](https://launchpad.net/~jldupont/+archive/jldupont)  with the package "rbsynclastfm"

2. Use the "Download Source" function of this git repo and place the "rbmpdbus" folder in ".gnome/rhythmbox/plugins"

Dependencies
============

None
