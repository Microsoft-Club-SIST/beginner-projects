#Genin Projects
#How to implement a simple caesar cypher
#understanding the implementations of unicode code point calues in algorithms
def caesarcypher(text,key):
    result = ""
    #We traverse the list and assign 'char' as each character from 'text'
    for i in range(len(text)):
        char = text[i]
        #When the characters are of upper case as the  unicode code point
        #representation of upper and lowe cases are different
        if (char.isupper()):
            #Here we take the unicode code point of  the char in the given string
            #and do the calculations required to implement the cypher
            result += chr(((ord(char) + key-65)%26) + 65) # since ord("A") is 65
        else:
            result += chr(((ord(char) + key-97)%26) + 97) # since ord("a") is 97
    return result

#Driver Code
text = "MeliodasZeldrisEstarosa"
key = 26
print(caesarcypher(text, key))
        
