#!/usr/bin/python3

for i in range(1, 100000001):
    report = ''
    if i % 3 == 0:
       report += "FIZZ"
    if i % 5 == 0:
        report += "BUZZ"
    #if not report:
     #   report = i
    #print(report)
    print(report if report else i)
