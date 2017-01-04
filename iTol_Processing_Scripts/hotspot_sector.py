#!/usr/bin/env python
# coding=utf-8

import sys
import csv

def iTOLcolours(fi):
    not_seen = set()
    #seen = set()
"""
colour = (',clade,#ff0000,normal,2')
list = colour
    
fi=open(sys.argv[1])
with open(sys.argv[1]) as fi:
 for row in csv.reader(fi, delimiter=','):
        print row + colour     
"""

fi=open(sys.argv[1])
with open(sys.argv[1]) as fi:
    #for line in fi:
     # if not line.startswith('#'):
      #    not_seen.add(line.strip())


#unseenReads = iTOLcolours(sys.stdin)

    for line in fi:
        print (line.strip() +',range,#ff0000,normal,2')

        
"""
        if not row or row[0].startswith('#'):
              
           continue
        #print (row) 
        #elif re.search(',1',row[0]): #pattern, where to search
        if '1' in row:    
            #_id = ','.join(row[0].split(',')[1:])
            not_seen.add(row[0])  
           # print ('added')
    return not_seen    
            

unseenReads = iTOLcolours(sys.stdin)

for row in (unseenReads):
    print (row +',clade,#ff0000,normal,2')

# csv files no empty lines expected 
# if not row (means if a row is empty) or (logical)    
"""
