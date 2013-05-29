#!/usr/bin/env python
#
# lpart -- list partitions of given device
#   Example: lstat.py sda

#with open('partitions') as file:
#    dev = [ line.split(None) for line in file ]

# Read devices from /proc/partitions
procpart = 'partitions'
with open(procpart) as file:
    lno, dev = 0, []
    for line in file:
        lno += 1
        if lno > 1:
            dev += line.split()[-1:]

devdict = { i for i in dev if not i.isalpha() }

