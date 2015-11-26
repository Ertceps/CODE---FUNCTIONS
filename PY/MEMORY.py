# --------------------------------------
# MEMORY
# --------------------------------------

# -+- IMPORT -+-
import time
import os


def details(dev):
    global free_memory
    fulldir = "/media/pi/KINGSTON/VACUUM_CONTROLLER"+dev

    disk = os.statvfs(fulldir)

    print("")
    print"Driver name " + fulldir
    print("")

    total_bytes = float(disk.f_bsize*disk.f_blocks)
    print "total space: %.2f GB" % (total_bytes/1024/1024/1024)

    total_used_space = float(disk.f_bsize*(disk.f_blocks-disk.f_bfree))
    print "used space: %.2f GB" % (total_used_space/1024/1024/1024)

    total_avail_space = float(disk.f_bsize*disk.f_bfree)
    print "available space: %.2f GB" % (total_avail_space/1024/1024/1024)

    free_memory = total_avail_space

    print("------------------------------")

    time.sleep(5)
