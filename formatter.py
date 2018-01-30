#A quick and simple program to make Telegram logs look more streamline

#Started Jan 29,2018, written by Blanchettwa



#Firstly, get the right file.
try:

    #Import the system so that the python version can be checked. This is for the input used later. 
    import sys

    #Now get the version, it will be a string

    verString = sys.version

    #Split the string by spaces to isolate the version number
    verArray = verString.split()

    #The first item is what is needed. Only the first four characters are needed as well 
    versionString = verArray[0][0:3]

    #Convert the string into a float so it can be compared and used. 
    ver = float(versionString)
    
except VersionError: 
    print ("Error determining Python version")

try:
    if (ver > 3.0):
        filename = input("Please name the filename to format, (eg, text.txt): " )
        outfn = input("Please name the file to output (eg, out.txt): ") 
    else:
        filename = raw_input("Please name the filename to format (eg. text.txt): ")
        outfn = raw_input("Please name the file to output (eg. out.txt): ") 

except FileError:
    print ("Error loading files")

try:

    oldLog = open(filename)
    newLog = open(outfn,"w+")

    #Write all of the lines into an array for easy management

    messageList = []

    for line in oldLog:
        messageList.append(line)

    #Now that the lines have been saved, we need to manipulate them 
    #Telegram messages follow a pattern of three. The first is the name and timestamp
    #The second is the message and the third is a blank space. Thus for the first three lines, funcion in this manner. 

    #Decide how many cycles of three there are. The last message will have just two lines. 
    numLines = len(messageList)
    numMessages = numLines // 3
    
    #iterate through the main cycles of the messages. 
    msg = 0

    for x in range(0,numMessages):
        #The first line is the name and timestamp. We just want the name.
        nameList = messageList[msg]

        #The first line is formatted so that the name is followed by a comma. We can use this
        nameAr = nameList.split(",")
        nam = nameAr[0]

        #The second line is the actual message. 
        msg += 1
        tx = messageList[msg]

        #Now parse it all into one string to be written. 
        writeString = nam + ": " + tx + "\n"

        #Write the new string to the output file. 
        newLog.write(writeString)

        #Skip the blank line and set up for the next message
        msg += 2

    #Get the last message. Repeat the previous steps one last time. 
    LnameList = messageList[msg]
    LnameAr = LnameList.split(",")
    Lnam = LnameAr[0]
    msg += 1
    Ltx = messageList[msg]

    finalWrite = Lnam + ": " + Ltx + "\n"
    newLog.write(finalWrite)

    #The new file has been created. Close both files now. 
    oldLog.close()
    newLog.close()

except OperationError:
    print ("Encountered errors")
