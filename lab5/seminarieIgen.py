def sum_satisfying(func, condition):
    return sum(func(x) for x in lst if condition(x))


lst = ["1", "abc", "3125", "YES", "no"]
print(sum_satisfying(int, str.isdigit))
print(sum_satisfying(len, str.isdigit))
print(sum_satisfying(len, str.isupper))

def sum_satisfying2(foo, pred):
    def inner_foo(seq):
        if not seq:
            return 0
        if pred(seq[0]):
            return foo(seq[0]) + inner_foo(seq[1:])
        else:
            return inner_foo(seq[1:])
    return inner_foo

