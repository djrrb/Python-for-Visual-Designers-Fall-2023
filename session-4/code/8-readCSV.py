# import the CSV library
import csv
# open the csv file as a new variable myFile
with open('Fantasy Conference - Sheet 1.csv', encoding='utf-8') as myFile:
    # use the csv library’s reader
    # to read our CSV into an interator
    myCSV = csv.reader(myFile)
    
    # now we can iterate through the csv
    # row by row
    for myRow in myCSV:
        # unpack each column from the row into a variable name
        myName, myCompany, myRole = myRow
        print(myName)