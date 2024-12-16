from match import *
from books import *


def test():
    '''Test function to test the program for errors and completion'''
    pattern1 = ['&', 'och', 'Felix', '--'] #True
    pattern2 = ['Sebastian', 'och', '&', '&', 'inte', '--'] #False
    db = books.db

    seq1 = ['Sebastian', 'och', 'Felix', 'programmerar', 'som', 'gudar']

    '''Test function to test the program for errors and completion'''
    #True
    try:
        match(seq1, pattern1)
    except Exception as e:
        print(f"Error in match: {e}")
    #False
    try:
        match(seq1, pattern2)
    except Exception as e:
        print(f"Error in match: {e}")

    #Valid
    try:
        search([['författare', ['&', 'zelle']], 
                ['titel', ['--', 'python', '--']], ['år', '&']], db)
    except Exception as e:
        print(f"Error in search: {e}")
    #Not valid (without the list)
    try:
        search('författare', '&', 'zelle', 
                'titel', '--', 'python', '--', 'år', '&', db)
    except Exception as e:
        print(f"Error in search: {e}")


def test_match_nested_structures():
    '''Test function to test the program for errors and completion'''
    database = [
        [[1, 2], [3, 4], 5],
        [[1, [2, 3]], [4, 5], 6],
        [7, 8, 9],
        [[10, [11, 12]], [13, 14], [15, 16]]
    ]

    pattern1 = [[1, 2], [3, 4], 5]  # Exact match
    pattern2 = [[1, [2, 3]], [4, 5], 6]  # Exact match with deeper nesting
    pattern3 = [[10, [11, 12]], [13, 14], [15, 16]]  # Deeply nested match
    pattern4 = [[1, 2], [3, 4]]  # Partial match
    pattern5 = [[1, [2, 4]]]  # Incorrect sublist
    
    # Test cases
    print(match(database[0], pattern1))  # Should return True
    print(match(database[1], pattern2))  # Should return True
    print(match(database[3], pattern3))  # Should return True
    print(match(database[0], pattern4))  # Should return False (length mismatch)
    print(match(database[1], pattern5))  # Should return False (incorrect sublist)


    
if __name__ == '__main__':
    test() # Should give error for the search with 10 arg


    pattern1 = ['&', 'och', 'Felix', '--'] #True
    pattern2 = ['Sebastian', 'och', '&', '&', 'inte', '--'] #False
    db = books.db

    seq1 = ['Sebastian', 'och', 'Felix', 'programmerar', 'som', 'gudar']
    #Tests
    print(match(seq1, pattern1)) #True
    print(match(seq1, pattern2)) #False
    print(match([], pattern1)) #False
    print(match([], [])) #True
    print(search([['författare', ['&', 'zelle']], # A working search
                ['titel', ['--', 'python', '--']], ['år', '&']], db)) 
    
    test_match_nested_structures() # Should give 3 True and 2 False
