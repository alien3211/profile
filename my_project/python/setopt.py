#!/usr/bin/python

import sys, getopt

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"ht:s:",["tfile=","sfile="])
    except getopt.GetoptError:
        print sys.argv[0], ' -t <backup_target_dir> -s <backup_source>'
        print '<backup_target_dir> - directory to BACKUP file (one argument)'
        print '<backup_source> - file and directory to BACKUP (one or more argument)'
        sys.exit(2)
    if '-t' in args or '-s' in args:
        print 'backupfile.py -t <backup_target_dir> -s <backup_source>'
        print '<backup_target_dir> - directory to BACKUP file (one argument)'
        print '<backup_source> - file and directory to BACKUP (one or more argument)'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-t", "--tfile"):
            target_dir = arg
        elif opt in ("-s","--sfile"):
            source = arg + ' ' + ' '.join(args)
    print "-t ", target_dir
    print "-s ", source

if __name__ == "__main__":
    main(sys.argv[1:])
