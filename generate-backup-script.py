#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, getopt

def readOptions(argv):
   unisonwd = ''
   unison = ''
   filt = ''
   try:
      opts, args = getopt.getopt(argv,"hw:u:f:",["workingdir=","unison=","filter="])
   except getopt.GetoptError:
      printHelp()
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         printHelp()
         sys.exit()
      elif opt in ("-w", "--workingdir"):
         unisonwd = arg
      elif opt in ("-u", "--unison"):
         unison = arg
      elif opt in ("-f", "--filter"):
         filt = arg
   if unisonwd == '':
      print 'Mising argument -w'
      printHelp()
      sys.exit(2)   
   if unison == '':
      print 'Mising argument -u'
      printHelp()
      sys.exit(2)         
   return unisonwd, unison, filt   

def printOption(i, prf):
    print 'echo -e "\t'+ str(i) +') '+prf + '"'
    
def unisonCommand(i, unison, prf, logfile):
    print 'if [[ "$option" -eq "' + str(i) + '" || "$option" -eq "0" ]]; then'
    print "\t"+'echo Synchronizing '+prf
    print "\t"+'echo'
    print "\t"+unison+ " " + prf + " " +  "-batch &>>"+ " " +  logfile
    print 'fi'
    print
    
def printHelp():
    print 'generate-backup-script.py -w <unison_working_dir> -u <path_to_unison> [-f <filter>]'

def main(argv):
   unisonwd, unison, filt = readOptions(argv)                  
   logfile = unisonwd + "/last.log"      
   
   print '#!/bin/bash'
   print '#Unison working directory: ', unisonwd
   print '#Log file is: ', logfile
   print '#Path to unison:', unison 
   print 'echo Unison backup script'
   print 'echo'
   print 'echo Options:'   
   print 'echo -e "\t0) ALL"'
   for dirname, dirnames, filenames in os.walk(unisonwd):    
    i=1
    for filename in filenames:
      if filename.endswith('.prf') and filt in filename:
	printOption(i,filename.replace(".prf", ""))
	i=i+1
    print
    print 'echo Type an option and press enter:'
    print 'read option'
    print 'echo'
    print
    print 'rm '+logfile
    print 'touch '+logfile
    print
    i=1
    for filename in filenames:
      if filename.endswith('.prf') and filt in filename:
	#print i,os.path.join(dirname, filename)		
	unisonCommand(i, unison, filename.replace(".prf", ""), logfile)	
	i=i+1

if __name__ == "__main__":
   main(sys.argv[1:])

