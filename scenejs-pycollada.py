#! /usr/bin/env python

# Main entry point for the scenejs-pycollada translator utility.

import collada
import sys
import getopt
import os.path
from translator import translate

def main(argv):
    # Get the command-line options given to the program
    try:                                
        opts, args = getopt.getopt(argv, "hvd", ["help", "verbose"]) 
    except getopt.GetoptError:           
        usage()                          
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print "Translate a Collada file to a JSON formatted SceneJS file"
            usage()     
            sys.exit()
        elif opt == '-d':
            global _debug
            _debug = 1
        elif opt in ("-v", "--verbose"): 
            global _verbose
            _verbose = 1

    if not args:
        print "No input files specified"
        usage();
        sys.exit(2);
    
    # Load and translate each file specified
    for filename in args:
        # Check whether the file exists and try to load it into a collada object
        if not os.path.isfile(filename):
            print "'" + filename + "' is not a valid file path."
            sys.exit(2);
        colladaObj = collada.Collada(filename, ignore=[collada.DaeUnsupportedError])
        
        # Create an output file write the SceneJS scene to
        basePath = os.path.splitext(filename)[0]
        outputFile = open(basePath + ".json","w")
        translate(outputFile, colladaObj)

def usage():
    print "Usage: "
    print "    python scenejs-collada --help"
    print "    python scenejs-collada [OPTION]... [FILE]..."
    print ""
    print "Miscelaneous options:"
    print "  -h, --help                 Display this help message"
    print "  -v, --verbose              Display verbose warnings and translation information"
    print "  -d                         Turn on debug mode"

if __name__ == "__main__":
    main(sys.argv[1:])
