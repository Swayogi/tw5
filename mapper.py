#!/usr/bin/env python  
import sys   
for line in sys.stdin:  
    line = line.strip().split(",")  
    if len(line) >= 2:  
        dept = line[2]  
        sal = line[3]  
        print '%s\t%s' % (dept, sal)
