def StringValidators(userInput):
    
    ## print True if has any alphanumeric characters. 
    
    isalnum = False
    for chars in userInput:
        if (chars.isalnum()) == True:
            print('True')
            isalnum = True
            break  
        
    if isalnum == False:
        print('False')
           
    ## print True if has any alphabetical characters.
    
    isalphaFlag = False
    for chars in userInput:
        if (chars.isalpha()) == True:
            print('True')
            isalphaFlag = True
            break  
        
    if isalphaFlag == False:
        print('False')
    
    ## print True if has any digits
    
    isdigitFlag = False
    for chars in userInput:
        if (chars.isdigit()) == True:
            print('True') 
            isdigitFlag = True
            break 
        
    if isdigitFlag == False:
        print('False')

    ## print True if has any lowercase characters
    
    islowerFlag = False
    for chars in userInput:
        if (chars.islower()) == True:
            print('True') 
            islowerFlag = True
            break 
        
    if islowerFlag == False:
       print('False')
        
    ## print True if has any uppercase characters
    
    isupperFlag = False
    for chars in userInput:
        if (chars.isupper()) == True:
            print('True') 
            isupperFlag = True
            break 
    
    if isupperFlag == False:
        print('False')

if __name__ == "__main__":
    
    StringValidators(input())
