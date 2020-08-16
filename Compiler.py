# C Programming Language Compiler by Nicholas Arnold

# Python code to identify elements of a simplified C language (Let's Call it C--) 
# using reserved words lists.  7 categories for simplicity. Varnames + values identified
#separately through processes rather than lists


#set up our string to make the necessary spaces for tokenization
inputS = input("Please enter some C-- Code\n")

inputT = inputS.replace("'", " ' ") 
inputT = inputS.replace('"', ' " ') 
inputT = inputT.replace("{", " { ")
inputT = inputT.replace("}", " } ")
inputT = inputT.replace("(", " ( ")
inputT = inputT.replace(")", " ) ")
inputT = inputT.replace(";", " ; ")
inputT = inputT.replace("[", " [ ")
inputT = inputT.replace("]", " ] ")
inputT = inputT.replace(":", " : ")
inputT = inputT.replace("//", " // ")
inputT = inputT.replace("/*", " /* ")
inputT = inputT.replace("*/", " */ ")



inputT = inputT.lower() #lower case to eliminate case differences


tokens = inputT.split()

typeID = ["int", "float", "string", "bool", "char"]

reserveAction = ["read", 
            "print", 
            "true", 
            "false",
            "break"]

operators = ["+", "-", "*", "/", "%", "+=", "-=", "="]

comparitors = [">=", "<=", "==", '>', '<', '!=']

terminals = ['(', ')', 
             "[", "]",
             "'", ";", 
             "{", "}", ":"]

visibility = ["public", "private"]

conditional = ["if", 'while', 'then', 'else', 'for', 'endif', 'do']


#usedVarnames keeps track of variables I've already declared
usedVarnames = []

#nextToken list stores the reserved word type of each token
#also serves as a reference for identifying types like variable names.

nextToken = []



#Make variable values an independent function to be called if typeID is positive!
#increment tknctr, print the type in the language array, continue loop as normal.

tknctr = 0
listctr = 0



while tknctr < len(tokens):
    
    #if statement catches comments, jumps to end if present
    if tokens[tknctr].find("/") != -1 and tokens[tknctr + 1].find("/") != -1:
        nextToken.append("Comment")
        print("Comment: ", end=" ")
        while tknctr < len(tokens):
            print(tokens[tknctr], end=" ") #print the full comment
            tknctr = tknctr + 1
        print("\n")
        break
    elif tokens[tknctr].find("/") != -1 and tokens[tknctr + 1].find("*") != -1:
        nextToken.append("Comment")
        print("Comment: ")
        while tknctr < len(tokens):
            print(tokens[tknctr], end=" ")
            tknctr = tknctr + 1
        print("\n")
        break
    
  
    listctr = 0 #reset listctr for next list comparison    
    
    
     #check token against typeID list
    while listctr < len(typeID):  
        if tokens[tknctr] == typeID[listctr]:
            print("Type identification: ", tokens[tknctr])
            nextToken.append("typeID")
            tknctr = tknctr + 1 #we know the next token will be a variable name
            print("Variable Name: ", tokens[tknctr]) #declare it
            nextToken.append("Varname")
            usedVarnames.append(tokens[tknctr]) #save variable name for later reuse
        listctr = listctr + 1
        
    listctr = 0 #reset listctr for next list comparison
    
            #check token against reserveAction list
    while listctr < len(reserveAction): 
        if tokens[tknctr] == reserveAction[listctr]:
            if nextToken[-2] == "typeID":  #check if it is illegal variable name
                nextToken[-1] = ("ILLEGAL RESERVED VARNAME!!!")
                print("\nERROR! VARNAME IS RESERVED!!!\n")
                tknctr = tknctr + 1
            else:
                nextToken.append("Reserved Action")
                print("Reserved Action: ", tokens[tknctr])
        listctr = listctr + 1
    
    listctr = 0 
    
    #check token against conditionals list
    while listctr < len(conditional):
        if tokens[tknctr] == conditional[listctr]:
            print("Conditional: ", tokens[tknctr])
            nextToken.append("Conditional")
        listctr = listctr + 1
    
    listctr = 0 #reset listctr for next list comparison
    
  
    #Check token against operators list
    while listctr < len(operators): 
        if tokens[tknctr] == operators[listctr]:
            print("Operator: ", tokens[tknctr])
            nextToken.append("Operator")
        listctr = listctr + 1
    
    listctr = 0 
    
    while listctr < len(comparitors): #check token against comparitors list
        if tokens[tknctr] == comparitors[listctr]:
            print("Comparitor: ", tokens[tknctr])
            nextToken.append("comparitors")
        listctr = listctr + 1
    
    listctr = 0 
    
    #check token against terminals list
    while listctr < len(terminals): 
        if tokens[tknctr] == terminals[listctr]:
            print("Terminal Symbol: ", tokens[tknctr])
            nextToken.append("Terminal Symbol")
        listctr = listctr + 1
    
    listctr = 0 
    
    #Check against visibility list
    while listctr < len(visibility): 
        if tokens[tknctr] == visibility[listctr]:
            print("Visibility set to: ", tokens[tknctr])
            nextToken.append("Visibility Modifier")
        listctr = listctr + 1
    
    listctr = 0 
        
    #Check whether the item is an integer or float
    try:
        val = int(tokens[tknctr])
        print("Integer: ", val)
        nextToken.append("Int Value")
    except ValueError:
        try:
            val = float(tokens[tknctr])
            print("Float ", val)
            nextToken.append("Float Value")
        except ValueError:
            listctr = 0
   
 
    #if statement catches text variable values
    if tokens[tknctr].find("'") != -1:
        tknctr = tknctr + 1 #skip the ' since it's already been noted
        nextToken.append("Text Value")
        print("Text value: ", end=" ")
        while tknctr < len(tokens):
            print(tokens[tknctr], end=" ") #print the full string
            tknctr = tknctr + 1
            if tokens[tknctr].find("'") != -1:
                nextToken.append("Terminal Symbol") #make sure ending ' is noted
                print("\nTerminal Symbol: ", tokens[tknctr])
                break

    #check whether the item is a reused variable name
    while listctr < len(usedVarnames):
        if nextToken[-2] != "typeID": #experimental line
            if tokens[tknctr] == usedVarnames[listctr]:
                nextToken.append("Variable Name")
                print("Variable Name: ", tokens[tknctr])
        listctr = listctr + 1

                    
    tknctr = tknctr + 1

print("Symbols we tokenized: \n ", tokens)
print("Order of operations: \n", nextToken)



