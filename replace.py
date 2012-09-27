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
                 {'search': u' ב-',	'replace': u' ב־'},
                 
                 {'search': u' ל ',	'replace': u' ל־'},
                 {'search': u' ה ',	'replace': u' ה־'},
                 {'search': u' ש ',	'replace': u' ש־'},
                 {'search': u' כ ',	'replace': u' כ־'},  
                 {'search': u' מ ',	'replace': u' מ־'}, 
                 {'search': u' ו ',	'replace': u' ו־'},
                 {'search': u' ב ',	'replace': u' ב־'},                 
                                  
                 {'search': u'תיקית',	'replace': u'תיקיית'},
                 {'search': u'תיקיה',	'replace': u'תיקייה'},                 
                 {'search': u'מירבי',	'replace': u'מרבי'},                 

                 {'search': u'סיסמה',	'replace': u'ססמה'},                                  
                 {'search': u'סיסמאות',	'replace': u'ססמאות'},                 
                 {'search': u'סיסמתך',	'replace': u'ססמתך'},                 
                                  
                 {'search': u'על-ידי', 	'replace': u'על־ידי'},
                
                 {'search': u'מירבי',	'replace': u'מרבי'},
                 {'search': u'להרשם',	'replace': u'להירשם'},                 
                 {'search': u'הינו',	'replace': u'הנו'},
# לפי כללי הכתיב חסר הניקוד ("כתיב מלא") של האקדמיה ללשון העברית, אין מוסיפים יו"ד לציון ניקוד החיריק במילה שבסיסה מילה שבה לא הוסף יו"ד (כי לא היה בה כלל צליל i). כך לדוגמה, "אמתי" נוצר מאמת, ואין לכתוב "אמיתי". וכך גם צורת הריבוי של "מס" הנה "מסים", ולא "מיסים". יש גם לכתוב "אתו" ולא "איתו", "הנו" ולא הינו", "אטי" ולא "איטי".
                 

                 {'search': u' מסויימים ',	'replace': u' מסוימים '}, 
#  לפי כללי הכתיב חסר הניקוד ("כתיב מלא") של האקדמיה ללשון העברית, יו"ד עיצורית תיכתב בדרך-כלל כ-"יי", אולם היו"ד לא תוכפל ליד אם-קריאה (וזאת בנוסף למספר כללים נוספים שלא זה המקום לדון בהם). לכן המילה "מצוין" תיכתב כך, ולא "מצויין".                                                  
                 {'search': u' מסויימות ',	'replace': u' מסוימות '},                                                   
                 {'search': u' מעונין ',	'replace': u' מעוניין '},                 
                 {'search': u' עידכונים ',	'replace': u' עדכונים '},                                  
                 {'search': u' איזור ',	'replace': u' אזור '},                  
                 {'search': u' מסויים ',	'replace': u' מסוים '}, 
                 {'search': u' תיהיה ',	'replace': u' תהיה '}, 
                 {'search': u' גלובאלי ',	'replace': u' גלובלי '}, 
                 {'search': u' איחסון ',	'replace': u' אחסון '}, 
                 {'search': u' לאכסן ',	'replace': u' לאחסן '}, 
                 {'search': u' איכסון ',	'replace': u' אחסון '}, 
                 ]
                 

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

