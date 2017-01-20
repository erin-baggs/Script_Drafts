#!/usr/bin/env python
# coding=utf-8

import sys 
#print (sys.argv) useful in de-bugging
import csv

Chromo = set()
chromopairs= set()

with open(sys.argv[1]) as file1:
    for row in csv.reader(file1, delimiter= '\t'):    #for row in fi:
        Chromo.add(row[0].strip())

        #return Chromo 
#print (Chromo) #
        
with open(sys.argv[2]) as file2:
    for row in csv.reader(file2, delimiter='\t'):
        if row[0].startswith("#"):
            continue 
    	#could I do a sed before csv reader and convert . to 
        attributes=row[8]
        d={} # Here means will make new dictionary for each line
        for item in attributes.split(';'):
            if item: 
                pair=(item.split('='))  
                d[pair[0]] = pair[1]    
                Gid=d['ID'].split('.')[0]   
        
                if Gid in Chromo:
                    chromopairs.add(row[0]+'\t'+Gid)
                    
for pair in sorted(chromopairs):
    print (pair)
            #colon only needed when cahnge into a different block include def and class