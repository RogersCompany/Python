

def StringChallenge(strParam):

  # There are 5 cond. This 4 cond 
  capitalCond = False
  numCond = False
  punCond = False
  strCond = False
  lastTestIndex = 0

  if len(strParam) < 7 or len(strParam) > 31:
    return False

  for ch in range(0, len(strParam)):
    
    if strParam[ch] == 'd' or strParam[ch] == 'D':
      print("here D")
      if ch >= 7:
        print("here D Len")
        print(strParam[ch-7:ch].lower())
        if strParam[ch-7:ch].lower() == 'password':
          print("here False Len")
          return False
    
    if ord(strParam[ch]) >= 65 and 90 <= ord(strParam[ch]):
      capitalCond = True
    
    if ord(strParam[ch]) >= 48 and 57 <= ord(strParam[ch]):
      numCond = True

    if ord(strParam[ch]) >= 33 and 64 <= ord(strParam[ch]) or ord(strParam[ch]) >= 91 and 96 <= ord(strParam[ch]) or ord(strParam[ch]) >= 123 and 126 <= ord(strParam[ch]):
      punCond = True
    
    if punCond and numCond and capitalCond:
      strParam = True


  # code goes here
  print(strParam)
  return strParam

# keep this function call here 
#print(StringChallenge(input()))

strParam="passWord123!!!!"

StringChallenge(strParam)