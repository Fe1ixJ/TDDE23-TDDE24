import books
db = books.db

def match(seq, pattern):
    """
    Returns whether given sequence matches the given pattern
    """
    if not isinstance(seq, list) or not isinstance(pattern, list):
        raise ValueError('Both seq and pattern must be lists')

    
    if not pattern:
        return not seq
    elif pattern[0] == '--':
        if match(seq, pattern[1:]):
            return True
        elif not seq:
            return False
        else:
            return match(seq[1:], pattern)
    elif not seq:
        return False
    elif pattern[0] == '&':
        return match(seq[1:], pattern[1:])
    elif seq[0] == pattern[0]:
        return match(seq[1:], pattern[1:])
    elif isinstance(seq[0], list) and isinstance(pattern[0], list):
        first = match(seq[0], pattern[0])
        rest = match(seq[1:], pattern[1:])
        return first and rest
    else:
        return False


def search(pattern, database):
    '''Searches a database and returns all seq in the database that is following the pattern'''
    if len(locals()) > 2:
        raise TypeError("search() takes 2 positional arguments but more were given")
    if not isinstance(database, list):
        raise ValueError("Database must be a list")
    if not isinstance(pattern, list):
        raise ValueError("Pattern must be a list")
    
    lst=[]
    for seq in database:
        if match(seq, pattern):
            lst.append(seq)
    return lst



if __name__ == '__main__':
    print(search([['författare', ['&', 'zelle']], 
                ['titel', ['--', 'python', '--']], ['år', '&']], db)) # 2 books
    print(search(['--', ['år', 2042], '--'], db))# []
    print(search(['--', ['titel', ['&', '&']], '--'], db)) # 1 book