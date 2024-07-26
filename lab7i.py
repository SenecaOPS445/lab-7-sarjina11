#!/usr/bin/env python3
# Student ID: skarki28

def function1():
    # This function should not modify the global variable
    global schoolName
    schoolName = 'SICT'
    print('print() in function1 on schoolName:', schoolName)

def function2():
    # This function modifies the global 'schoolName'
    global schoolName
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:', schoolName)

schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)
function1()
print('print() in main on schoolName:', schoolName)
function2()
print('print() in main on schoolName:', schoolName)
