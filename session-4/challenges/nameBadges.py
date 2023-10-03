# import the CSV library
import csv

# specify a relative path to our csv file
csvPath = 'Fantasy Conference - Sheet 1.csv'

# make a dictionary mapping attendee roles to colors
roleColors = {
    'Attendee': (1, 0, 1),
    'Speaker': (0, 1, 1),
    }

# the information for drawing a single badge lives in this function
def drawBadge(name, affiliation, role, dimensions):
    
    # do all badge stuff within a saved state
    # this way any transformations we do won’t affect any other badges being drawn
    with savedState():
        
        # define some key measurements 
        margin = .25*inch
        contentWidth = dimensions[0]-margin*2
        contentHeight = dimensions[1]-margin*2
        nameWidth = contentWidth - margin*2
        nameHeight = contentHeight - margin*2
        
        # move to the bottom left margin
        translate(margin, margin)
        
        # set a default color
        fill(0, 1, 0)
        # if our person has a specific role
        # give them a different color
        if role in roleColors:
            fill(*roleColors[role])
        
        
        # draw a background
        rect(0, 0, contentWidth, contentHeight)

        # split the name up into individual words
        words = name.split(' ')
        # make an empty list of lines that we will populate
        lines = []
        # loop through our words
        for word in words:
            # if it is a longer word, make it its own line
            if len(word) > 3:
                lines.append(word)
            # if it is a shorter word, add it to the most recent line
            else:
                lines[-1] += ' ' + word
            
        # make an empty formatted string that we will populate    
        fs = FormattedString()
        for word in lines:
            # set the fontsize to 1 and get the dimensions of the word
            fontSize(1)
            tw, th = textSize(word)
            # if we figure out how many times a 1pt sample will fit into the page width, we know the fontSize we need to fill the page width
            myFontSize = nameWidth / tw 
            
            # prevent the fontsize from getting too big tho
            if myFontSize > 50:
                myFontSize = 50
            # add our word to the formatted string at the
            # appropriate font size 
            fs.append(word+'\n',
                fontSize=myFontSize,
                lineHeight=myFontSize,
                align="center",
                font='Georgia',
                fill=0
            )
    
        # now get the dimensions of the whole dang formatted string 
        tw, th = textSize(fs, width=nameWidth)
        # we will vertically center it by offsetting it
        # subtract the actual space from the space allotted 
        # and divide it by two to get the bottom margin
        yoffset = (nameHeight - th)/2

        # use this dummy rectangle to show the space alotted    
        #fill(1, 0, 0)
        #rect(margin, margin*2, nameWidth, nameHeight-yoffset)
        
        # if we have an affiliation, leave room for it
        if affiliation:
            bottomMargin = margin*2
        else:
            bottomMargin = margin
        # draw the formatted string to the canvas 
        textBox(fs, (margin, bottomMargin, nameWidth, nameHeight-yoffset))

        # draw the affiliation if it exists
        with savedState():
            # for this we can translate to the center of the space
            # and draw a simple text field
            translate(contentWidth/2, margin)
            fill(1)
            fontSize(10)
            # this oval shows us where we are in the space
            #oval(-5, -5, 10, 10)
            
            if affiliation:
                # only draw this stuff if we actually have an affiliation
                # make a line
                stroke(1)
                line((-nameWidth/2, margin), (nameWidth/2, margin))
                # draw the text
                stroke(None)
                text(affiliation, (0, 0), align="center")
        
inch = 72 
dimensions = (8.5*inch/2, 11*inch/4)

        
with open(csvPath, 'r', encoding="utf-8") as csvFile:
    
    # mehhh let’s not split this up as a string
    # but if we wanted to, here’s how we’d do it
    #fileText = csvFile.read()
    #lines = fileText.split('\n')
    #for line in lines:
    #    columns = line.split(',')
    #    print(columns)
    
    # instead get a csv reader object that we can loop through
    reader = csv.reader(csvFile)
    
    # loop through each row in the CSV
    # tick will be the number of the row that we are on
    for tick, row in enumerate(reader):
       
        # skip the first row since it’s the headers
        if tick == 0:
            continue
                       
        # get the contents of the row
        name, affiliation, role = row
        # normalize the role since we need it a certain way
        role = role.title()
        
        newPage(*dimensions)

        # draw the badge twice, for front and back
        with savedState():
            drawBadge(name, affiliation, role, dimensions)
