#!/usr/bin/env python
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time

# path to the directory (relative or absolute)
dirpath = sys.argv[1] if len(sys.argv) == 2 else r'.'

# get all entries in the directory w/ stats
entries = (os.path.join(dirpath, fn) for fn in os.listdir(dirpath))
entries = ((os.stat(path), path) for path in entries)

# leave only regular files, insert creation date
entries = ((stat[ST_CTIME], path)
           for stat, path in entries if S_ISREG(stat[ST_MODE]))


all_files_sorted = sorted(entries, reverse=True)

for cdate, path in all_files_sorted[3:]:
    print(time.ctime(cdate), os.path.basename(path), path)
    try:
        os.remove(path)
    except Exception as e:
        print(e)