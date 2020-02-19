import numpy as np
import re
import json

def readStructure(input):
    rows = input.split("\n")
    rows = np.array(rows)
    Values = np.zeros((9,9))    #row, column
    ValueIndex = 0
    index = 0
    InputValues = ['1', '2', '3', '4', '5', '6' ,'7' ,'8' ,'9']
    for row in rows:
        if index in [0,1,2,4,5,6,8,9,10]:
            rowValue = readRow(row)
            columnIndex = 0
            for individualValue in rowValue:
                if individualValue in InputValues:
                    Values[ValueIndex, columnIndex] = individualValue
                columnIndex = columnIndex + 1
            ValueIndex = ValueIndex + 1
        index = index + 1
    return Values

def readRow(row):
    row = row.replace('|', '')
    row = row.replace('  ', ' ')
    return row.split(' ')

def row valid

f = open("input.txt","r")
input = f.read() #get the str 
f.close()

inputStructure = readStructure(input)
print(inputStructure)