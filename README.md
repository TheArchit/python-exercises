Solutions to challenges kindly laid down by 'gagomes'
(https://github.com/gagomes) for me to resolve in Python and learn the
language.

insbd.py:
--------
Connects to a MySQL database, creates a table if there isn't one, checks if
a row for the effective UNIX user exists, adds one if not and finally updates a
counter for the user.

lpart.py:
--------
Lists the partitions for the device passed via ARGV.

mkmnt.py:
--------
Creates a filesystem mountpoint for each of the partitions listed in the output
of fdisk.
