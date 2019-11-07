#!/usr/bin/env python

""" This program will read in an IDX file for Ryerson/EP2 to delete duplicate invoice records and correct the 
pagecount field.

# Programmer: Jeff Wade
# Date Written: 02/2012
"""

import os
import sys
import traceback
import csv
import glob

import time
import datetime
import locale

if __name__ == '__main__':   

    csvfile = csv.reader(open('tul_i.idx'),delimiter='|')
    #csvfile = csv.reader(open(d['infile']),dialect='pipes')
    output = open('tul_o.idx', 'w')
    writer = csv.writer(output,delimiter='|')
    #writer = csv.writer(output,dialect='pipes')
    #print writer
    first = 1
    pagecnt = 0
    recread = 0
    recwrite = 0
    
    for row in csvfile:
        recread += 1
        searchflds = str(row[0]) + str(row[1]) + str(row[2]) + str(row[3]) + str(row[4])

        if first:
           prevrow = row
           prevrow[6] = 0
           prevsearch = searchflds
           first = 0        
        
        if searchflds != prevsearch:
            recwrite += 1
            writer.writerow(prevrow)
            searchflds = str(row[0]) + str(row[1]) + str(row[2]) + str(row[3]) + str(row[4])
            pagecnt = int(row[6])
            prevrow = row
            prevsearch = searchflds
        else:
            pagecnt += 1
            prevrow[6] = pagecnt
            
    recwrite += 1
    writer.writerow(prevrow)  #  Write the last record
    
        