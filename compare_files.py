#!/usr/bin/env python
# coding=utf-8

import sys
import csv

"""
fi1 = open(sys.argv[1])
with open(sys.argv[1]) as fi1, open(sys.argv[2]) as fi2:
    do_stuff()
"""    


Clade = set()

with open(sys.argv[1]) as file1:
    for line in file1:
    #for row in fi:
        #print row.strip()
        #break
        #continue 
        Clade.add(line.strip())
        
with open(sys.argv[2]) as file2:
    for row in csv.reader(file2, delimiter=','):
        if row[0] in Clade:
            print row
        

"""
def NLRs(fi):
def NLR_IDs(fi):

    NLR_IDsfound = set()
for row in csv.reader(fi, delimiter=','):
    for row in NLRs(fi):
        if row[0] == row[0] in NLR_IDs(fi):
            _id=.add(row[0])
            NLR_IDsfound.add(_id)
            continue
        continue

    return NLR_IDsfound 

NLR_IDsfound = NLR_IDs($1)
NLRs = NLRs($2)
for row in NLR_IDsfound:
    print row

  #  NLR_IDsfound = set()

    #for row in csv.reader(fi, delimiter=','):
     #   if row[0].startswith('#'):
      #      if row[0].startswith('# Query: '):
       #         _query = '.'.join(row[0].split()[2:])
        #        continue
         #   elif row[0].startswith('# 0 hits found'):
          #      not_seen.add(_query)
           #     continue
           # continue
       # evalue, alen, pid = map(float, (row[10], row[3], row[2]))
        #if alen >= 200 and pid >= 85: 
         #   seen.add(_query)
          #  continue
      #  if not _query in seen:
      #      not_seen.add(_query)
   # return not_seen

"""
