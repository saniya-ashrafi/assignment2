

def inputdata(inpStr):
  charCount = 0
  digitCount = 0
  symbolCount = 0
  for char in inpStr:
    if char.islower() or char.isupper():
      charCount+=1
    elif char.isnumeric():
      digitCount+=1
    else:
      symbolCount+=1
      
  print("Chars = ", charCount, "Digits = ", digitCount, "Symbol = ", symbolCount)
      
inpStr = "P@#yn26at^&i5ve"
print("total counts of chars, digits,and symbols \n")

inputdata(inpStr)