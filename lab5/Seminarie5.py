#Seminarie5

def count(lst, req):
    count = 0
    for i in lst:
        if req(i):
            count += 1
    return count

is_number = lambda x: isinstance(x, (int, float))
is_positive = lambda x: x > 0
is_even = lambda x: x % 2 == 0
is_negative = lambda x: x < 0
is_a = lambda x: x == "a"
is_twoelementlong = lambda x: len(x) == 2 
is_div3 = lambda x: x % 3 == 0

print(count([17, 3.14, "banan"], is_number))
print(count([17, 3.14, -1, 4532, -52.2], is_positive))
print(count(["a", "B", "c", "a", "d"], is_a))
print(count([["a"], [1, 2], ["b", "c"]], is_twoelementlong))
print(count([1, 2, 3, 4, 5, 6, 9], is_div3))
print(count([1, 2, 3, 4, 5, 6, 9], is_even))
print(count([1, 2, 3, 4, 5, 6, 9], is_negative))


def count_rec(elements, predicate):
    if not elements:
        return 0
    head, tail = elements[0], elements[1:]
    if predicate(head):
        return 1 + count_rec(tail, predicate)
    else:
        return count_rec(tail, predicate)


'''
>>> count(["a", "B", "c", "a", "d"], ___________________)
2
>>> count([["a"], [1, 2], ["b", "c"]], ___________________)
2
>>> count([1, 2, 3, 4, 5, 6, 9], ___________________)
3'''

def funktion(lst):
    # Filter out names that start with 'a', convert to uppercase, and sort by length
    return sorted(map(str.upper, filter(lambda x: x[0].lower() != 'a', lst)), key=len)

print(funktion(["Bert", "August", "Sharah", "Kim"]))


from functools import reduce

def mySum(nums):
    return reduce(lambda x, y: x + y, nums)

print(mySum([1, 2, 3, 4, 5]))

def myMap(foo, elements):
    #Irative version
    res = []
    for elem in elements:
        res.append(foo(elem))
    #return [foo(x) for x in elements]

    #Recursive version
    if not elements:
        return []
    else:
        return [foo(elements[0])] + myMap(foo, elements[1:])
    # listbygggare
    #return list(map(foo, elements))

    #Nästa seminarie kommer vara lite repitition och lite nytt.