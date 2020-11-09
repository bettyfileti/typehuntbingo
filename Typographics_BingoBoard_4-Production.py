#Script rounds up from total boards needed to multiple of 4.
#Next challenge: Create actual frequency rating, and blacklist certain letter/qualifier combinations

from random import random
import random
import math

#Variables
pt = 7.2
totalBoards = 3

totalSheets = int(totalBoards/4) + 1
print ("print pages needed =", totalSheets)

sheetWidth = 85 * pt
sheetHeight = 110 * pt

#Colors
d= 255
mainColor = 0,0,0,1

##Helpers
def fillColor(c):
    """
    a helper function that processes rgba or cymka tuples. 
    I use this because I hate having to switch back and forth between
    color spaces, and splitting up colors from tuples each time.
    """
    if len(c) == 5:
        cmykFill(c[0], c[1], c[2], c[3], c[4])
    elif len(c) == 4:
        fill(c[0], c[1], c[2], c[3])
    else:
        fill(c[0], c[1], c[2])

#Fonts
displayFont = 'Canal-Regular'
displayFontBoldFill = 'FactionCommercial-Black'
displayFontBold = 'FactionCommercial-Outline'
typeSize = 6
displaySize = 28

if displayFont not in installedFonts():
    displayFont = 'Helvetica-Regular'
    displayFont = 'Arial'

if displayFontBold not in installedFonts():
    displayFontBold = 'Helvetica-Bold'
    displayFontBold = 'Arial'
    
#Images
logoMyFonts = "Links/MyFonts_Logo_C_RGB_by_Monotype-01.png"
logoPoliteType = "Links/PoliteType_Logo.png"
imMF = ImageObject(logoMyFonts)
imPT = ImageObject(logoPoliteType)

#Copy
boardCaption = "#TYPEHUNTBINGO. Once you have 5-in-a-row, tag @TypographicsNYC on instagram and show us that\rB-I-N-G-O for your chance to win!"
referenceNumber = "Board #"



#1.0 - Random String Production/Dictionary Builder
totalTileCount = 25 #LEAVE ALONE
rowCount = 5 #LEAVE ALONE
tileCounter = 0

letterTile = ["R", "S","T","L","N","E", "A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "R", "S", "T", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","Ö","À","Ñ", "É","1", "2", "3", "4", "5", "6", "7", "8", "9"]
describeTile = ["in script", "w/ shadow","drawn by Herb Lubalin", "in italics", "sans serifs", "w/ slab serifs", "painted", "on a vehicle", "on a\rbuilding", "by a woman\rdesigner", "in 3D", "on a menu", "on a\rmagazine","handwritten","stenciled","on glass", "in neon", "outlined", "very small", "extremely\rlarge", "on the ground", "on packaging", "on a shirt", "w/ serifs", "written\rillegally", "on a poster", "w/ reverse contrast", "condensed", "wide", "in a fat face", "very thin","oblique","in a style you\r kind of love", "on litter", "in a bold\rweight","in a light\rweight", "in black", "in white", "in red", "in blue","drawn at\rTypographics", "in a\rnewspaper", "on a sign", "in a presentation", "in a type specimen", "drawn by\rTom Carnase", "on a statue", "in metal", "in stone", "in a type specimen", "with the ink\rstill wet", "in calligraphy", "in black", "in red", "in a presentation","made from objects", "handwritten", "in script", "in italics", "sans serifs", "w/ slab serifs", "w/ bifurcated serifs", "ornamented", "in a\rsketchbook","in yellow"]

tileTitle = tileCounter
tileValue = FormattedString()
tileDict = {tileTitle:tileValue}

describeTileCount = len(describeTile)
letterTileCount = len(letterTile)

def buildDict():
    tileCounter = 0
    tileValue = FormattedString()
    for i in range(0,totalTileCount):        
        describePosition = random.randint(0, (describeTileCount - 1))
        letterPosition = random.randint(0, (letterTileCount - 1))
    
        tileValue.append(letterTile[letterPosition],font = displayFontBold, fontSize = displaySize, fill = (0,0,0), align = "center", lineHeight = (1))
        tileValue.append("\r\r\r " + describeTile[describePosition],font = displayFont, fontSize = typeSize, fill = (0,0,0), lineHeight = (7))
    
        tileCounter = tileCounter + 1
        tileDict[tileCounter] = tileValue
    
        tileValue = FormattedString()
buildDict()

#2.0 Draw Bingo Boards

#2.1 Variables
boardWidth = 42.5*pt
boardHeight = 55*pt
sideMargin = 2*pt
bottomMargin = sideMargin * 1.5
outerGrid = boardWidth - (sideMargin * 2)
tileHeight = outerGrid/5
tileWidth = tileHeight

verticalGridShift = 0
textShift = (tileWidth*.005)
boardNumber = 0

#2.2 Pull Values of Tiles & place them in gridded format
def drawTile():
    def getTiles(): 
        save()
        translate(sideMargin,bottomMargin)
        for i in range(1,totalTileCount):
            #tileRow = 1
            def tileGrid(x,y,w,h):
                fill(1,0,1,0)
                stroke(0,0,0)
                strokeWidth(1.5)
                rect(x,y+bottomMargin+verticalGridShift,w,h)
                
                
            if i <= 5:
                x,y,w,h = (0,0, tileWidth, tileWidth)
                tileValue = tileDict.get(i)
                textBox(tileValue,(x,y+textShift,w,h))
                tileGrid(x,y,w,h)
                translate(tileWidth)
            
            #tileRow = 2
            elif i > 5 and i <= 10:
                x,y,w,h = (-tileWidth, tileWidth, tileWidth, tileWidth)
                tileValue = tileDict.get(i)
                tileRow = 2
                textBox(tileValue,(x,y+textShift,w,h))
                tileGrid(x,y,w,h)
                translate(-tileWidth)

            #tileRow = 3
            elif i > 9 and i <=14:
                if i == 11 or i == 12:
                    x,y,w,h = (0,(tileWidth*2), tileWidth, tileWidth)
                    tileValue = tileDict.get(i)
                    textBox(tileValue,(x,y+textShift,w,h))
                    tileGrid(x,y,w,h)
                    translate(tileWidth)
                else:
                    x,y,w,h = (0,(tileWidth*2), tileWidth, tileWidth)
                    tileValue = tileDict.get(i)
                    translate(tileWidth)
                    textBox(tileValue,(x,y+textShift,w,h))
                    tileGrid(x,y,w,h)
                    #translate(tileWidth)
            
            #tileRow = 4       
            elif i > 14 and i <= 19:
                x,y,w,h = (0,(tileWidth*3), tileWidth, tileWidth)
                tileValue = tileDict.get(i)
                tileRow = 4
                textBox(tileDict.get(i),(x,y+textShift,w,h), align='center')
                tileGrid(x,y,w,h)
                translate(-tileWidth)

            #tileRow = 5        
            elif i > 19 and i <= 25:
                x,y,w,h = (tileWidth, (tileWidth*4), tileWidth, tileWidth)
                tileValue = tileDict.get(i)
                textBox(tileDict.get(i),(x,y+textShift,w,h), align='center')
                tileGrid(x,y,w,h)
                translate(tileWidth)
        restore()
    buildDict()
    getTiles()
    
#2.3 Draw Free Square
def drawFreeSquare():
    save()
    translate(0,bottomMargin)
    freeTileRect = tileWidth + 6    
    fillColor(mainColor)
    rect((boardWidth-(freeTileRect))/2,bottomMargin+(tileWidth*2)+(tileWidth/4),freeTileRect, tileWidth/2)
    stroke(0,0,0,0)
    rect(sideMargin+(tileWidth*2),bottomMargin+(tileWidth*2),tileWidth, tileWidth)
    fill(1,1,1)
    tracking(2)
    lineHeight(24)
    fontSize(20)
    stroke(4)
    font(displayFontBold)
    textBox("FREE",(((boardWidth-(freeTileRect))/2)+1.5,bottomMargin+(tileWidth*2)+(tileWidth/4)-1,freeTileRect, tileWidth/2), align = "center")
    restore()

#2.4 Draw Title with Logos
def bingoTitle():
    save()
    translate(sideMargin-1.5,bottomMargin + (tileWidth*4.7))
    fill(0,0,0)
    
    fontSize(68)
    font(displayFontBoldFill)
    textBox("BINGO",(0,0,sheetWidth, tileWidth*2), align = "left")
    
    def logo(img,resizePT,x,y):
        save()
        w,h = imageSize(img)
        w,h = imageSize(img)
        translate(x,y)        
        scale(resizePT)
        image(img,(0,0))
        restore()
    
    logo(imMF,.085,190,52)
    logo(imPT,.15,248,52)
    restore()
        
    
def drawCaption(boardNumber):
    save()
    font(displayFont)
    fontSize(6)
    fill(0,0,0)
    captionVertPos = -(tileWidth*1.3)
    textBox(boardCaption,(sideMargin,captionVertPos,tileWidth*3, tileWidth*2),align = "left")
    textBox(referenceNumber + str(boardNumber),(sideMargin,captionVertPos,boardWidth-(sideMargin*2),tileWidth*2), align = "right")
    restore()

def drawBoard(boardNumber, boardWidth=42.5*pt, boardHeight = 55*pt):
    sheetCount = int(boardNumber/4)
    fill(1,1,1)
    rect(0,0,boardWidth, boardHeight)
    drawFreeSquare()
    drawTile()
    bingoTitle()
    drawCaption(boardNumber)
     

def drawSheets(sheetWidth, sheetHeight, boardNumber, totalSheets, sheetNumber):
    #Make a sheet of 4 boards for printing
    
    #Make the sheetCount tell us what number print page the board is on
    sheetCount = int(boardNumber/4)
    sheetNumber += 1
    
    boardNumber += 1

    if boardNumber%4 == 0:
        sheetCount = sheetCount
    else:
        sheetCount = sheetCount + 1
        
    newPage(sheetWidth, sheetHeight)
    translate(0, boardHeight)
    drawBoard(boardNumber)
    
    boardNumber += 1
    translate (boardWidth, 0)
    drawBoard(boardNumber)
    
    boardNumber += 1
    translate(-boardWidth,-boardHeight)
    drawBoard(boardNumber)      
    
    boardNumber += 1
    translate(boardWidth, 0)
    drawBoard(boardNumber)
    
    
    
    #Draw Crop Marks
    translate(0, 0)
    fill(0,0,1,.5)
    rect(0,0,1,7)
    
    translate(0,sheetHeight-7)
    rect(0,0,1,7)
    
    translate(0,7)
    translate(-boardWidth,-boardHeight)
    rect(0,0,7,1)
    
    translate(sheetWidth-7,0)
    rect(0,0,7,1)
       
for sheetNumber in range(0,totalSheets):
    drawSheets(sheetWidth, sheetHeight, boardNumber, totalSheets, sheetNumber)
    boardNumber = boardNumber + 4
    #drawBoard()
    
    
saveImage("~/Desktop/Typographics_BingoBoard_RF_1-300.pdf")            