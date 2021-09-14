userText = input("Text to be encrypted: ")
encrText = ""
for c in userText:
    numChar = ord(c) - 19
    encrChar = chr(numChar)
    encrText += encrChar
print(encrText)