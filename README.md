dotsync
=======

Copy your dotfiles (or anyfiles) from one machine, to exactly the same location on a remote machine. Making replicating configurations easy.


TODO
--------
* ~~Impliment reading from extnal file which contains pre-defined file paths~~ Done
* ~~Impliment checks for file existance before opening file~~
* ~~Make absolute file paths be sent~~ Done
* ~~Impliment replacement of username in absolute file paths~~ Done
* Impliment error catching

Known Issues
------------
* Binding the receiving machine to any other address other than *localhost* or *0.0.0.0* fails to assign requested address.
