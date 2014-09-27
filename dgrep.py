#! /usr/bin/python

import sys
import os
import re


progn = os.path.basename(sys.argv[0])
debug = 4

def printdebug(istr=[], level=1, outf=sys.stderr):
    ''' Print Debug

    If the (global) variable "debug" is greater than the argument "level"
    '''

    if int(debug) > int(level):
        print "debug = " , debug
        print "level = " , level
        ostr = "";
        i = 0
        l = len(istr)
        while i < l:
            ostr = ostr + str(istr[i])
            i += 1
        print >> outf, "**" + progn + "** " + ostr 

def pd(*istr):
    printdebug(istr,1,sys.stderr)

def usage():
    print("""
    Usage: """ + progn + """ [OPTIONS]
            -h              help
            -d <dir>        directory
            -s <string>     search string

    """)
    sys.exit(1)


def main(wdir=os.getcwd(),sstr=''):

    global debug
    argc = len(sys.argv)
    if argc < 2 or re.search('(-h|-H)',sys.argv[1]) :
        usage()
    else :  # Parse the args
        i = 1
        while i < argc:
            if sys.argv[i] == "-d":
                wdir = sys.argv[i+1]
                i += 2
                pd("wdir set to ", wdir)
                continue
            elif sys.argv[i] == "-s":
                sstr = sys.argv[i+1]
                i += 2
                pd("sstr set to '" + sstr + "'")
                continue
            elif sys.argv[i] == "-D":
                debug = int(sys.argv[i+1])
                i += 2
                pd("debug set to '" , debug , "'")
                continue
            else:
                pd("Unkown option")
                usage()

    if sstr == "" :
        print "ERROR: string not set"
        sys.exit(2)
    cmd = "find " + wdir + " -type f -print0 | xargs -0 grep " + sstr
    os.system(cmd)

if __name__ == "__main__":
    main()
