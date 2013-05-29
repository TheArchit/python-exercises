#!/usr/bin/env python

# TODO:
#   * take a list of devices
#   * create a mountpoint for each partition
#   * possibly mkfs and mount the partition
#   * dump a suitable fstab containing all partitions

import re
import subprocess
import os

#def fdisk():
#    """ Runs fdisk and returns a list of device partitions """
#    dev = []
#    cmd = subprocess.Popen('./fdisk',
#            stdout=subprocess.PIPE)
#
#    for line in cmd.communicate()[0].splitlines():
#        try:
#            if line[0] == '/':
#                dev.append(line.split()[0])
#
#        except:
#            pass
#
#    return dev

def fdisk():
    """ Runs fdisk and returns a list of device partitions """
    cmd = subprocess.Popen(['./dummy_fdisk', '-l', 'sda'],
            stdout=subprocess.PIPE)

    return filter(None,map(lambda dev: re.findall('^/[^ ]+', dev),
        cmd.communicate()[0].splitlines()))

def main():
    for i in fdisk():
        dirname = 'mnt/' + i[0].split('/')[-1]
        try:
            os.makedirs(dirname)
        except:
            pass

if __name__ == '__main__':
    main()

