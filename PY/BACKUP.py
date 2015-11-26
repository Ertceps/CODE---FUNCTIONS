# --------------------------------------
# BACKUP
# --------------------------------------

# -+- IMPORT -+-
import sys
import os
import shutil
import filecmp
import threading

MAXVERSIONS = 100
BAKFOLDER = '.bak'

class ThreadBackup(threading.Thread):
    
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self, tree_top, bakdir_name=BAKFOLDER):

        print "Starting " + self.name
        print "%s: %s" % (threadName, time.ctime(time.time()))
        
        top_dir = os.path.basename(tree_top)
        tree_top += os.sep
        
        for dir, subdirs, files in os.walk(tree_top):

            if os.path.isabs(bakdir_name):
                relpath = dir.replace(tree_top,'')
                backup_dir = os.path.join(bakdir_name, top_dir, relpath)
            else:
                backup_dir = os.path.join(dir, bakdir_name)

            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)

            # To avoid recursing into sub-directories
            subdirs[:] = [d for d in subdirs if d != bakdir_name]
            for f in files:
                filepath = os.path.join(dir, f)
                destpath = os.path.join(backup_dir, f)
                # Check existence of previous versions
                for index in xrange(MAXVERSIONS):
                    backup = '%s.%2.2d' % (destpath, index)
                    abspath = os.path.abspath(filepath)
                    
                    if index > 0:
                        # No need to backup if file and last version
                        # are identical
                        old_backup = '%s.%2.2d' % (destpath, index-1)
                        if not os.path.exists(old_backup): break
                        abspath = os.path.abspath(old_backup)
                        
                        try:
                            if os.path.isfile(abspath) and filecmp.cmp(abspath, filepath, shallow=False):
                                continue
                        except OSError:
                            pass
                    
                    try:
                        if not os.path.exists(backup):
                            print 'Copying %s to %s...' % (filepath, backup)
                            shutil.copy(filepath, backup)
                    except (OSError, IOError), e:
                        pass

    if __name__=="__main__":
        if len(sys.argv)<2:
            sys.exit("Usage: %s [directory] [backup directory]" % sys.argv[0])
            
        tree_top = os.path.abspath(os.path.expanduser(os.path.expandvars(sys.argv[1])))
        
        if len(sys.argv)>=3:
            bakfolder = os.path.abspath(os.path.expanduser(os.path.expandvars(sys.argv[2])))
        else:
            bakfolder = BAKFOLDER
            
        if os.path.isdir(tree_top):
            backup_files(tree_top, bakfolder)
