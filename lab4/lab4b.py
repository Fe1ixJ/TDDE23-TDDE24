def interpret(expression, context): 
    if isinstance(expression, str):
        # If the expression is a string, return its value from the context dictionary
        # If the expression is not found in the context, return the expression itself
        return context.get(expression, expression)
    
    if isinstance(expression, list):
        if len(expression) > 2:
            # If the expression is a list with more than 2 elements, 
            # it could be an "AND" or "OR" expression
            if expression[1] == "AND":
                return interpret_and(expression, context)
            elif expression[1] == "OR":
                return interpret_or(expression, context)
        elif expression[0] == "NOT":
            # If the list starts with "NOT", it is a "NOT" expression
            return interpret_not(expression, context)
        if expression == 0:

            # Placeholder for test interpretation
            return interpret_test(expression, context)

def interpret_and(expression, context):
    # Evaluate the "AND" expression
    # Return "true" if both sides of the expression are true
    if (interpret(expression[0], context) == True or interpret(expression[0], context) == "true") and \
        (interpret(expression[2], context) == True or interpret(expression[2], context) == "true"):
        return "true"
    elif expression[0] == "true" and expression[2] == "true":
        # Special case where both sides are the string "true"
        return "true" 
    else: 
        return "false"

def interpret_or(expression, context):
    # Evaluate the "OR" expression
    # Return "true" if at least one side of the expression is true
    if (interpret(expression[0], context) == True or interpret(expression[0], context) == "true") or \
        (interpret(expression[2], context) == True or interpret(expression[2], context) == "true"):
        return "true"
    elif expression[0] == "true" or expression[2] == "true":
        # Special case where at least one side is the string "true"
        return "true"
    else:
        return "false"

def interpret_not(expression, context):
    # Evaluate the "NOT" expression
    # Return "true" if the expression is false
    value = interpret(expression[1], context)
    return "true" if value is False or value == "false" else "false"

def interpret_test(expression, context):
    return "False Value"