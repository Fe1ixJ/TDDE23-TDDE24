def split_it(x):
    first_message = ""  # Local variables
    second_message = ""

    for i in x:  # Loop directly over the characters in the string
        if i.islower() or i == "ä" or i == "å" or i == "ö" or i == "_" or i == ".":  # Check for lowercase letters (a-z), special characters (ä, å, ö), and underscore ('_')
            first_message += i
        elif i.isupper() or i == "Ä" or i == "Å" or i == "Ö" or i == " " or i == "|":
            second_message += i  # Check for uppercase letters (A-Z), special characters (Ä, Å, Ö), space (' '), or pipe ('|')

    return first_message, second_message


def split_rec(x):
    if not x:
        return "", ""
    
    first_message, second_message = split_rec(x[1:])

    if x[0].islower() or x[0] == "ä" or x[0] == "å" or x[0] == "ö" or x[0] == "_" or x[0] == ".":  # Check for lowercase letters (a-z), special characters (ä, å, ö), and underscore ('_')
        return x[0] + first_message, second_message
    elif x[0].isupper() or x[0] == "Ä" or x[0] == "Å" or x[0] == "Ö" or x[0] == " " or x[0] == "|":
        return first_message, x[0] + second_message
    else:
        return first_message, second_message
    

def interpret(expression, context): 
    if isinstance(expression, str):
        # If the expression is a string, return its value from the context dictionary
        # If the expression is not found in the context, return the expression itself
        return context.get(expression,expression)
    
    if isinstance(expression, list):
        if len(expression) >2:
            if expression[1] == "AND":
                if (interpret(expression[0], context) == True or interpret(expression[0], context) == "true") and (interpret(expression[2], context) == True or interpret(expression[2], context) == "true"):
                    return "true"
                elif expression[0] == "true" and expression[2] == "true":
                    return "true" 
                else: 
                    return "false"
            elif expression[1] == "OR":
                if (interpret(expression[0], context) == True or interpret(expression[0], context) == "true") or (interpret(expression[2], context) == True or interpret(expression[2], context) == "true"):
                    return "true"
                elif expression[0] == "true" or expression[2] == "true":
                    return "true" 
                else:
                    return "false"
        elif expression[0] == "NOT":
            if interpret(expression[1], context) is False or interpret(expression[1], context) == "false":
                return "true"
            else:
                return "false"
