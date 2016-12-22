#!/usr/bin/env python
# coding=utf-8

import sys
import csv

def iTOLcolours(fi):
    not_seen = set()
    seen = set()
    for row in csv.reader(fi, delimiter=','):
        
        if not row or row[0].startswith('#'):
              
           continue
        #print (row) 
        #elif re.search(',1',row[0]): #pattern, where to search
        if '.' or ' ' or '[A-Z]' in row :     
            #_id = ','.join(row[0].split(',')[1:])
            not_seen.add(row[0])  
           # print ('added')
    return not_seen    
            

unseenReads = iTOLcolours(sys.stdin)

for row in (unseenReads):
    print (row +',range,#0000ff,normal,2')

# csv files no empty lines expected 
# if not row (means if a row is empty) or (logical)    
