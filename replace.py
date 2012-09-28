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
                 {'search': u'סיסמת',	'replace': u'ססמת'},                 
                 {'search': u'סיסמאות',	'replace': u'ססמאות'},                 
                 {'search': u'סיסמתך',	'replace': u'ססמתך'},                 
                                  
                 {'search': u'על-ידי', 	'replace': u'על־ידי'},
                
                 {'search': u'מירבי',	'replace': u'מרבי'},
                 {'search': u'להרשם',	'replace': u'להירשם'},                 

                 {'search': u'הינך',	'replace': u'הנך'},                 
                 {'search': u'הינו',	'replace': u'הנו'},
# לפי כללי הכתיב חסר הניקוד ("כתיב מלא") של האקדמיה ללשון העברית, אין מוסיפים יו"ד לציון ניקוד החיריק במילה שבסיסה מילה שבה לא הוסף יו"ד (כי לא היה בה כלל צליל i). כך לדוגמה, "אמתי" נוצר מאמת, ואין לכתוב "אמיתי". וכך גם צורת הריבוי של "מס" הנה "מסים", ולא "מיסים". יש גם לכתוב "אתו" ולא "איתו", "הנו" ולא הינו", "אטי" ולא "איטי".
                 

                 {'search': u'מסויימים',	'replace': u'מסוימים'}, 
#  לפי כללי הכתיב חסר הניקוד ("כתיב מלא") של האקדמיה ללשון העברית, יו"ד עיצורית תיכתב בדרך-כלל כ-"יי", אולם היו"ד לא תוכפל ליד אם-קריאה (וזאת בנוסף למספר כללים נוספים שלא זה המקום לדון בהם). לכן המילה "מצוין" תיכתב כך, ולא "מצויין".                                                  
                 {'search': u'מסויימות',	'replace': u'מסוימות'},                                                   
                 {'search': u'מסויימת',	'replace': u'מסוימת'},                  
                 
                 {'search': u'מעונין',	'replace': u'מעוניין'},                 
                 {'search': u'עידכונים',	'replace': u'עדכונים'},                                  
                 {'search': u'איזור',	'replace': u'אזור'},                  
                 {'search': u'מסויים',	'replace': u'מסוים'}, 
                 {'search': u'תיהיה',	'replace': u'תהיה'}, 
                 {'search': u'גלובאלי',	'replace': u'גלובלי'},
                 {'search': u'גלובלים',	'replace': u'גלובליים'},                  
                 
                 {'search': u'דוגמא ',	'replace': u'דוגמה '},
                 {'search': u'לדוגמא',	'replace': u'לדוגמה'},                 
                                                   
                 {'search': u'לצפיה',	'replace': u'לצפייה'},                                  
                 {'search': u'מימד',	'replace': u'ממד'},                  
                 {'search': u'צויינה',	'replace': u'צוינה'}, 
                 {'search': u'צויינו',	'replace': u'צוינו'},                  
                 
                 {'search': u'נסיונות',	'replace': u'ניסיונות'},                  
                 {'search': u'נסיון',	'replace': u'ניסיון'},                  

                 {'search': u'זכרון',	'replace': u'זיכרון'},                 
                 {'search': u'להקבע',	'replace': u'להיקבע'},                                  
                 {'search': u'השניה',	'replace': u'השנייה'},                  
                 {'search': u'עוגיה',	'replace': u'עוגייה'}, 
                 {'search': u'פונקצית',	'replace': u'פונקציית'},                 
                 
                 {'search': u'תאור',	'replace': u'תיאור'},                 
                 {'search': u'הכל ',	'replace': u'הכול '}, 
                 {'search': u'צינזור',	'replace': u'צנזור'},                  
                 {'search': u'להבדק',	'replace': u'להיבדק'}, 
                 {'search': u'להתקל',	'replace': u'להיתקל'},                   

                 {'search': u'להכנס',	'replace': u'להיכנס'},
                 {'search': u'שהינך',	'replace': u'שהנך'},                 
                 {'search': u'לחילופין',	'replace': u'לחלופין'},
                 {'search': u'רשיון',	'replace': u'רישיון'},
                 
                 {'search': u' ילקח',	'replace': u' יילקח'},
                 {'search': u' יבדק',	'replace': u' ייבדק'},
                 {'search': u'פרוייקט',	'replace': u'פרויקט'},
                 {'search': u'פירסום',	'replace': u'פרסום'},
                 {'search': u'סיגנון',	'replace': u'סגנון'},
                 
                 {'search': u'להמחק',	'replace': u'להימחק'},
                 {'search': u'להמנע',	'replace': u'להימנע'},
                 
                 {'search': u'להמצא',	'replace': u'להימצא'},
                 {'search': u'להנתן',	'replace': u'להינתן'},                 
                 {'search': u'להפתח',	'replace': u'להיפתח'},
                 {'search': u'להשאר',	'replace': u'להישאר'},    
                 {'search': u'להכשל',	'replace': u'להיכשל'},
                 {'search': u'להכלל',	'replace': u'להיכלל'},    
                 {'search': u' ירשם',	'replace': u' יירשם'},
                 {'search': u' יכלל',	'replace': u' ייכלל'},    
                 {'search': u' יחשף',	'replace': u' ייחשף'},  

                 {'search': u'ליעוץ',	'replace': u'לייעוץ'},    
                 {'search': u'ליבא',	'replace': u'לייבא'},
                 {'search': u'מדוייקת',	'replace': u'מדויקת'},    
                 {'search': u'מקסימאלי',	'replace': u'מקסימלי'},
                 {'search': u'מקסימלים',	'replace': u'מקסימליים'},    
                 {'search': u'מינימלים',	'replace': u'מינימליים'},  

                 {'search': u'תקח',	'replace': u'תיקח'},    
                 {'search': u'תעזר',	'replace': u'תיעזר'},
                 {'search': u'תלקח',	'replace': u'תילקח'},    
                 {'search': u'תיקנית',	'replace': u'תקנית'},
                 {'search': u'תירגום',	'replace': u'תרגום'},    
                 {'search': u'תיכנן',	'replace': u'תכנן'},                   
                 {'search': u'תיהיו',	'replace': u'תהיו'},    

                 {'search': u'ארוך מידי',	'replace': u'ארוך מדי'},
                 {'search': u'ארוכה מידי',	'replace': u'ארוכה מדי'},    
                 {'search': u'קצרה מידי',	'replace': u'קצרה מדי'},
                 {'search': u'קצר מידי',	'replace': u'קצר מדי'},    
                 {'search': u'קטן מידי',	'replace': u'קטן מדי'}, 
                 
                 {'search': u'גבוה מידי',	'replace': u'גבוה מדי'},
                 {'search': u'קצרים מידי',	'replace': u'קצרים מדי'},    
                 {'search': u'ארוכים מידי',	'replace': u'ארוכים מדי'},
                 {'search': u'גדול מידי',	'replace': u'גדול מדי'},    
                 {'search': u'נפוצות מידי',	'replace': u'נפוצות מדי'},                                   
                 {'search': u'יותר מידי',	'replace': u'יותר מדי'},                  
                 
                 
                 {'search': u'צפיה',	'replace': u'צפייה'},
                 {'search': u'הסיסמא',	'replace': u'הססמה'},
                 {'search': u'צויין',	'replace': u'צוין'},
                 {'search': u'תבדק',	'replace': u'תיבדק'},
                 {'search': u'הרישמי',	'replace': u'הרשמי'},
                 {'search': u'תנתן',	'replace': u'תינתן'},
                 {'search': u'מצויינת',	'replace': u'מצוינת'},

                 {'search': u'גירסאת',	'replace': u'גרסת'},
                 {'search': u'גירסא',	'replace': u'גרסה'},
                 {'search': u'גירסה',	'replace': u'גרסה'},

                 {'search': u'במידה ש',	'replace': u'אם '},                 
                 {'search': u'במידה ו',	'replace': u'במידה ש'},
 
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
#  print content
else:
  print ("Please specify file name as argv[1]")
  filename = sys.stdin.readline() #.rstrip('\n')
  content = run(filename)
  print content

