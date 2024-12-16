from calc import *
import copy

# Example programs to test for errors
calc1 = ['calc', ['print', 2], ['print', 4]]
calc2 = ['calc', ['if', [3, '>', 5], ['print', 2], ['print', 4]]]
calc3 = ['calc', ['print', [2, "+", 5]]]
calc4 = ['calc', ['if', [8, '=', 8], ['print', [3, '*', 2]], ['print', [10, '/', 2]]]]
calc5 = ['calc', []]  # No statements
calc6 = ['calc', ['if', [8, '!', 8], ['print', [3, '*', 2]], ['print', [10, '/', 2]]]]  # Invalid conditional operator
calc7 = ['calc', ['print', [2, "%", 5]]]  # Invalid binary operator
calc8 = ['calc', ['iff', [3, '>', 5], ['print', 2], ['print', 4]]]  # Invalid keyword
calc9 = ['calc', ['set', 'a', 5], ['print', 'a']]
calc10 = ['calc', ['set', 'x', 7], ['set', 'y', 12], ['set', 'z', ['x', '+', 'y']], ['print', 'z']]
calc11 = ['calc', ['read', 'p1'], ['set', 'p2', 47], ['set', 'p3', 179], ['set', 'result', [['p1', '*', 'p2'], '-', 'p3']], ['print', 'result']]
calc12 = ['calc', ['set', 'a', 10], ['set', 'a', 5], ['print', 'a']]
calc13 = ['calc', ['read', 'n'], ['set', 'sum', 0], ['while', ['n', '>', 0],
        ['set', 'sum', ['sum', '+', 'n']],
        ['set', 'n', ['n', '-', 1]]],
        ['print', 'sum']]


def exec_program(p, var_table=None):
    """
    Executes a program if it has the correct structure.
    Raises an error if there are no statements or if the program format is invalid.
    """
    if var_table is None:
        var_table = {}

    if not is_program(p):
        raise TypeError("Invalid program format.")
    elif len(p) == 2 and empty_statements(p[1]):
        raise ValueError("No statements in the program.")
    else:
        statements = program_statements(p)
        var_table = exec_statements(statements, var_table)
        return var_table


def exec_statements(p, var_table):
    """
    Executes each statement in a list of statements.
    """
    if is_statement(p):
        return var_table
    if is_statements(p):
        statement = first_statement(p)
        var_table = exec_statement(statement, var_table)
        return exec_statements(rest_statements(p), var_table)
    elif empty_statements(p):
        return var_table
    else:
        raise TypeError("Invalid statement format.")


def exec_statement(p, var_table):
    """
    Executes a single statement. Handles conditional statements, output statements, and variable assignments.
    """
    valid_keywords = {"if", "print", "set", "read", "while"}

    if isinstance(p, list):
        keyword = p[0]
        if keyword not in valid_keywords:
            raise ValueError(f"Invalid statement keyword: '{keyword}'. Expected one of {valid_keywords}.")

    if is_selection(p):  # Handles conditional statements
        return exec_selection(p, var_table)
    elif is_output(p):  # Handles print statements
        return exec_output(p, var_table)
    elif is_assignment(p):  # Handles variable assignments
        return exec_assignment(p, var_table)
    elif is_input(p):  # Handles input statements
        return exec_input(p, var_table)
    elif is_repetition(p):  # Handles repetition statements
        return exec_repetition(p, var_table)
    else:
        raise TypeError("Invalid statement type.")


def exec_output(p, var_table):
    """
    Executes an output statement. Prints the value of a variable or a constant.
    """
    if is_constant(p[1]) or is_binaryexpr(p[1]):  # If a constant or binary expression is printed, print the value
        print(eval_expression(output_expression(p), var_table))
    else:  # If a variable is printed, print the variable and its value
        print(p[1], "=", eval_expression(output_expression(p), var_table))
    return var_table


def exec_assignment(p, var_table):
    """
    Executes an assignment statement. Assigns a value to a variable.
    """
    local_table = var_table.copy()
    variable = assignment_variable(p)
    value = eval_expression(assignment_expression(p), var_table)
    local_table[variable] = value
    return local_table


def exec_selection(p, var_table):
    """
    Executes a conditional statement. Evaluates the condition and executes the true or false branch based on the result.
    """
    condition = eval_condition(selection_condition(p), var_table)
    if condition:
        var_table = exec_statements([selection_true_branch(p)], var_table)
    elif selection_has_false_branch(p):
        var_table = exec_statements([selection_false_branch(p)], var_table)
    return var_table


def exec_repetition(p, var_table):
    """
    Executes a repetition statement. Evaluates the condition and executes the statements inside the loop based on the result.
    """
    while eval_condition(repetition_condition(p), var_table):
        for statement in repetition_statements(p):
            var_table = exec_statement(statement, var_table)
    return var_table


def exec_input(p, var_table):
    """
    Executes an input statement. Reads a value from the user and assigns it to a variable.
    """
    local_table = var_table.copy()
    read_variable = input_variable(p)
    user_input = int(input(f"Enter value for {read_variable}: "))
    local_table[read_variable] = user_input
    return local_table


def eval_condition(p, var_table):
    """
    Evaluates a conditional expression. Returns True or False based on the evaluation of the condition.
    """
    if is_condition(p):
        left = eval_expression(condition_left(p), var_table)
        right = eval_expression(condition_right(p), var_table)
        operator = condition_operator(p)

        if operator == ">":
            return left > right
        elif operator == "<":
            return left < right
        elif operator == "=":
            return left == right
        else:
            raise ValueError(f"Unsupported conditional operator: '{operator}'")
    raise TypeError("Invalid condition format.")


def eval_expression(p, var_table):
    """
    Evaluates an expression. Handles constants, binary expressions, and variables.
    """
    if is_constant(p):
        if not isinstance(p, (int, float)):
            raise TypeError("Constant is not a valid number.")
        return p
    elif is_variable(p):  # Retrieves a variable from var_table
        if p in var_table:
            return var_table[p]
        else:
            raise ValueError(f"Variable '{p}' not found in variable table.")
    elif is_binaryexpr(p):
        return eval_binaryexpr(p, var_table)    
    else:
        raise TypeError("Invalid expression format.")
    
def eval_binaryexpr(p, var_table):
    """
    Evaluates a binary expression. Returns the result of the binary operation.
    """
    if is_binaryexpr(p):
        left = eval_expression(binaryexpr_left(p), var_table)
        right = eval_expression(binaryexpr_right(p), var_table)
        operator = binaryexpr_operator(p)
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            return left / right
    raise ValueError(f"Unsupported binary operator: '{operator}'")


# Test cases
if __name__ == '__main__':
    test_cases = [calc1, calc2, calc3, calc4, calc5, calc6, calc7, calc8, calc9, calc10, calc11, calc12, calc13]
    for i, calc in enumerate(test_cases, start=1):
        try:
            var_table = exec_program(calc)
            print(f"calc{i} result: {var_table}")
        except Exception as e:
            print(f"Error in calc{i}: {e}")