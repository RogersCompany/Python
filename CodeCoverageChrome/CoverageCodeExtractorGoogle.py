import json
import sys
from datetime import date


# PYTHON SCRIPT FOR EXTRACT UNUSED CODE AFTER CHROME CONSOLE 

#FORMAT OUT_FILE
def formatFileOut(FILE_NAME, urlName):
    today = date.today()
    curDate = today.strftime("%d_%m_%Y")
    formatURL=urlName.replace("/","-")
    formatURL2=formatURL.replace(":","")
    FILE_OUT=FILE_NAME+"_" + curDate + "_" + formatURL2
    return FILE_OUT
    
#OPEN JSON FILE        
def openFileIn(FILE_NAME: str):
    #OPEN IN FILE
    with open(FILE_NAME) as f:
        dataJson = json.load(f)
        parseFileIn(FILE_NAME, dataJson)
        
# JSON FILE : FOR EVERY URL EXTRACT FROM GOOGLE CHROME COVERAGE CONSOLE
def parseFileIn(FILE_NAME, data): 
    for entry in data:
        pass # print entry['url']
        text = ""
        FILE_OUT=formatFileOut(FILE_NAME, entry['url'])
        for range in entry['ranges']:
            range_start = range['start']
            range_end = range['end']
            text += entry['text'][int(range_start):int(range_end)]+"\n"
               
        with open(FILE_OUT, "w") as text_file:
            print(f"{text}", file=text_file)

########## MAIN ########## 
### READ ARGS FILE NAME ##
n = len(sys.argv)
print("Total arguments passed:", n)
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
    openFileIn(sys.argv[i])
