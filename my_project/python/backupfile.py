#!/usr/bin/python
import os
import time
import sys
import getopt
import re



# Colour pattern
color_no = '\x1B[0m'
color_red = '\x1B[0;31m'
color_blue = '\x1B[0;34m'
color_green = '\x1B[0;32m'
color_yellow = '\x1B[0;33m'
color_magenta = '\x1B[0;35m'

def print_help():
    """Print help"""
    print color_blue, '\nbackupfile.py', color_magenta, '-t', color_yellow, '<backup_target_dir>', color_magenta, '-c', color_yellow, '<comment> <backup_source>\n\n'
    print color_green, 'Options:\n'
    print color_yellow, '\t<backup_target_dir>', color_no, '- directory to BACKUP file',color_magenta ,'(one argument)'
    print color_yellow, '\t<comment>', color_no, '- comment to BACKUP',color_magenta ,'(one argument \n\t\t\
    or more arguments between double quotes"<comment>")'
    print color_yellow, '\t<backup_source>', color_no, '- file and directory to BACKUP',color_magenta ,'(one or more argument)',color_no

if len(sys.argv) > 1:
    try:
        opts, args = getopt.getopt(sys.argv[1:],"ht:c:",["tfile=","comment","help"])
    except getopt.GetoptError:
        print_help()
        sys.exit(1)
    if not '-t' in args and len(args) >= 1:
        target_dir = os.getenv("HOME") + os.sep + 'backup'
    elif ('-t' in args ) or len(opts) < 1:
        print_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-t", "--tfile"):
            target_dir = arg
        elif opt in ("-c","--comment"):
            comment = arg
            comment = re.sub(r"\s+",'_',comment)
        elif opt in ("-h","--help"):
            print_help()
            sys.exit(0)
    
    source = ' '.join(args)
    if len(comment) == 0:
        comment = ''
else:
# source from input
    source = raw_input(color_yellow + 'File to BACKUP: ' + color_no)
    target_dir =  raw_input(color_yellow + 'Directory to BACKUP: ' + color_no)
    comment =  raw_input(color_yellow + 'Comment to BACKUP: ' + color_no)
    if len(source) == 0:
        target_dir = os.getenv("HOME")

# name folder
today = target_dir + os.sep + time.strftime('%Y-%m-%d')
# name file zip
now = time.strftime('%H:%M:%S')

# replace any spaces
source.replace(' ','_')
target_dir.replace(' ','_')

# check file exist
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print color_green, "Successfully create directory", target_dir, color_no

# UP
if not os.path.exists(today):
    os.mkdir(today)
    print color_green, "Successfully create directory", today, color_no


# check if comment exist
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment + '.zip'
    target.replace(' ','_')


zip_command = "zip -r {0} {1}".format(target, source)

# Run the Backup
print color_yellow, "Zip command is:"
print color_blue, zip_command
print color_yellow, "Running:", color_magenta
if os.system(zip_command) == 0:
    print color_green, 'Successful BACKUP to', color_blue, target, color_no
else:
    print color_red , 'BACKUP FAILED', color_no

