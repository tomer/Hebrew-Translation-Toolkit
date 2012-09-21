#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import os
import shutil
import re

def readfile(filename):
	f = open(filename, 'r')
	content = f.read().decode("utf-8")
	f.close()
	return content

def writefile(filename, content):
#  shutil.copy(filename, filename +'.bak')
  directory = os.path.dirname(filename)
  if not os.path.exists(directory):
    os.makedirs(directory)
  f = open(filename, 'w')
  f.write(content.encode('utf-8'))
  f.close()
	
def replace(content, searchfor, replacement):
	return content.replace(searchfor, replacement)
	
replacements = [ {'search': u' ל-',	'replace': u' ל־'},
                 {'search': u' ה-',	'replace': u' ה־'},
                 {'search': u' ש-',	'replace': u' ש־'},
                 {'search': u' כ-',	'replace': u' כ־'},  
                 {'search': u' מ-',	'replace': u' מ־'}, 
                 {'search': u' ו-',	'replace': u' ו־'},
                 {'search': u'תיקית ',	'replace': u'תיקיית '},
                 {'search': u'תיקיה ',	'replace': u'תיקייה '},                 
                 {'search': u' המירבי ',	'replace': u' המרבי '},
                 {'search': u'סיסמה ',	'replace': u'ססמה '},                                  
                 {'search': u'סיסמאות ',	'replace': u'ססמאות '},                 
                 {'search': u' על-ידי ', 	'replace': u' על־ידי '}, ]
                 

def run(filename):
  filename = filename.rstrip('\n')
  filename = filename.lstrip('./')
  content = readfile(filename)
  for r in replacements:
    content = content.replace(r['search'], r['replace'])
  writefile('new/' + filename, content)
  return content.encode('utf-8')

if (len(sys.argv) > 1): 
  content = run(sys.argv[1])
  print content
else:
  print ("Please specify file name as argv[1]")
  filename = sys.stdin.readline() #.rstrip('\n')
  content = run(filename)
  print content

