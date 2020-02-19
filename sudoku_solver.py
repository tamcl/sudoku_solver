import numpy as np
import re
import json

def readStructure(input):
    rows = input.split("\n")
    rows = np.array(rows)
    Values = np.zeros((9,9)).astype(int)    #row, column
    ValueIndex = 0
    index = 0
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

def InitialPossibleFactors(inputStructure):
    possibleValue = {}
    for row in range(9):
        for column in range(9):
            if inputStructure[row, column] == 0:
                possibleValue[str(row)+"+"+str(column)] = [1,2,3,4,5,6,7,8,9]
    return possibleValue

def FixedFactor(inputStructure):
    FixedFactor = {}
    for row in range(9):
        for column in range(9):
            if inputStructure[row, column] != 0:
                FixedFactor[str(row)+"+"+str(column)] = inputStructure[row,column]
    return FixedFactor

def initialElimination(inputStructure,fixedValues, possibleValues):
    #TODO rows
    fixedValues, possibleValues = checkRows(fixedValues, possibleValues)
    #TODO column
    fixedValues, possibleValues = checkColumns(fixedValues, possibleValues)
    #TODO block
    fixedValues, possibleValues = checkBlocks(fixedValues, possibleValues)
    return fixedValues, possibleValues

def checkRows(fixedValues, possibleValues):
    for row in range(9):
        for number in range(9):
            ExistNumber = False
            for column in range(9):
                try:
                    if number == fixedValues[str(row)+"+"+str(column)]:
                        ExistNumber = True
                except:
                    pass
            if ExistNumber == True:
                for column in range(9):
                    try:
                        possibleValues[str(row)+"+"+str(column)].remove(number)
                    except:
                        pass
    return fixedValues, possibleValues

def checkColumns(fixedValues, possibleValues):
    for column in range(9):
        for number in range(9):
            ExistNumber = False
            for row in range(9):
                try:
                    if number == fixedValues[str(row)+"+"+str(column)]:
                        ExistNumber = True
                except:
                    pass
            if ExistNumber == True:
                for row in range(9):
                    try:
                        possibleValues[str(row)+"+"+str(column)].remove(number)
                    except:
                        pass
    return fixedValues, possibleValues

def checkBlocks(fixedValues, possibleValues):
    blockCR = [0, 3, 6]
    for Brow in blockCR:
        for Bcolumn in blockCR:
            #gives all coordinates of start of the blocks
            for number in range(9):
                ExistNumber = False
                for row in range(3):
                    for column in range(3):
                        try:
                            if fixedValues[str(Brow+row)+"+"+str(Bcolumn+column)] == number:
                                ExistNumber = True
                        except:
                            pass
                if ExistNumber == True:
                    for row in range(3):
                        for column in range(3):
                            try:
                                possibleValues[str(Brow+row)+"+"+str(Bcolumn+column)].remove(number)
                            except:
                                pass
    return fixedValues, possibleValues

def printFixed(fixedValues):
    Structure = ''
    for row in range(9):
        for column in range(9):
            try:
                target = fixedValues[str(row)+"+"+str(column)]
                target = int(target)
                target = str(target) + " "
            except:
                target = 'X '
            
            if column in [2, 5]:
                Structure = Structure + target + "| "
            else:
                Structure = Structure + target
        Structure = Structure + "\n"
        if row in [2, 5]:
            Structure = Structure + "------+-------+------\n"
    return Structure

#TODO valid row
#TODO valid column
#TODO valid block
#TODO transfer

def brute(fixedValues, possibleValues, row = 0, column = 0):

    # if column < 9:
    #     column = column + 1
    # elif row < 9:
    #     column = 0
    #     row = row + 1
    # else:
    #     pass
    return fixedValues, possibleValues

f = open("input.txt","r")
input = f.read() #get the str 
f.close()

InputValues = ['1', '2', '3', '4', '5', '6' ,'7' ,'8' ,'9']

inputStructure = readStructure(input)
fixedFactors = FixedFactor(inputStructure)
possibleFactors = InitialPossibleFactors(inputStructure)

fixedFactors, possibleFactors = initialElimination(inputStructure, fixedFactors, possibleFactors)

print(fixedFactors)
print(possibleFactors)