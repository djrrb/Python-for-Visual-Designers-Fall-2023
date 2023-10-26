import csv
myInch = 72
with open('Fantasy Conference - Sheet 1.csv', encoding='utf-8') as myFile:
    myCSV = csv.reader(myFile)
    for myRow in myCSV:
        myName, myCompany, myRole = myRow
        print(myName)
        newPage(3.5*myInch, 2*myInch)
        font('Minion Pro', 18)
        openTypeFeatures(smcp=True)
        #rect(20, 70, width()-110, 50)
        textBox(myName, (20, 70, width()-110, 50))
        fill(1, 0, 0)
        openTypeFeatures(smcp=False)
        fontSize(12)
        text(myCompany, (20, 30))
        scale(.4)
        image('https://universityinnovation.org/images/5/5c/Cooper_union_logo.png', (420, 130))
        
        