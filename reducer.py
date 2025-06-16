#!/usr/bin/env python
import sys
deptdic = {}
for line in sys.stdin:
    line = line.strip()
    dept, sal = line.split('\t')
    if dept in deptdic:
        deptdic[dept].append(int(sal))
    else:
        deptdic[dept] = []
        deptdic[dept].append(int(sal))
for dept in deptdic.keys():
    sum_sal = sum(deptdic[dept]) * 1.0
    print('%s\t%s' % (dept, sum_sal))
