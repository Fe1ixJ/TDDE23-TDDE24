
def count(seq):

    if not seq:
        return 0
    elif isinstance(seq[0], list):
        return count(seq[0]) + count(seq[1:])
    else:
        return 1 + count(seq[1:])


def test_count1():
    try:
        assert count([]) == 0
        assert count([1, 2, 3]) == 3
        assert count([[1, 2], 3]) == 3
        assert count([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) == 8
        #assert count("hej") == 3
    except AssertionError:
        print("Test failed")
    else: 
        print("All tests passed")


def test_count2():
    
    count([[]]) == 0
    count([]) == 0
    count([[1, 2], 3]) == 3
    count([True, True, [ False]]) == 3

    tests = [[[]], [], [[1, 2], 3], [True, True, [False]]]
    results = [1, 0, 3, 3]
    for i in range(len(tests)):
        try:
            assert count(tests[i]) == results[i], "output: " + str(count(tests[i])) + " expected: " + str(results[i])
        except:
            #add things about test failed
            pass




def reverse_pair_rec(seq):
    
    # om tom lista returnera tom lista, udda antal eller jämnt antal element i listan och växla plats på elementen
    if not seq:
        return seq
    if len(seq) < 2:
        return seq
    else:
        return [seq[1], seq[0]] + reverse_pair_rec(seq[2:])

if __name__ == '__main__':
    try:
        assert reverse_pair_rec([]) == []
        assert reverse_pair_rec([1, 2, 'x', 4]) == [2, 1, 4, 'x']
        assert reverse_pair_rec([1,2,3,4,5]) == [2,1,4,3,5]
    except AssertionError:
        print("Test failed")


def reverse_pairs_better(seq):
    for i in range(len(seq//2)):
        seq[2*i], seq[2*i+1] = seq[2*i+1], seq[2*i]
    return seq
''' '''
#Gamaltenta i tdd24 
def merge(seq1, seq2):
    if not seq1:
        return seq2
    if not seq2:
        return seq1
    if seq1[0] < seq2[0]:
        return [seq1[0]] + merge(seq1[1:], seq2)
    else:
        return [seq2[0]] + merge(seq1, seq2[1:])    
    
def mergesort(seq):
    if len(seq) < 2:
        return seq
    if len(seq) == 2:
        if seq[0] > seq[1]:
            return [seq[1], seq[0]]
        else:
            return seq
    else:
        return merge(mergesort(seq[:len(seq)//2]), mergesort(seq[len(seq)//2:]))


if __name__ == '__main__':
    try:
        assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
        assert merge([1, 3, 5], [2, 4, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
        assert merge([1, 3, 5, 7], [2, 4, 6]) == [1, 2, 3, 4, 5, 6, 7]
    except AssertionError:
        print("Test failed")
    else:
        print("All tests passed")