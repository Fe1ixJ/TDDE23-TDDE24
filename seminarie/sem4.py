lst=[1, -1, 45.3, 4711, -273.15]

def pos(lst):
    return [x for x in lst if x > 0]

print(pos(lst))

lst2=["Apa", "Banan", "Citron"]

def first_letter_number(lst2):
    lst3 = []
    for i in range(len(lst2)):
        x = lst2[i]
        lst3.append(ord(x[0]))
    return lst3
print(first_letter_number(lst2))

lst4 = [[17, 4, 8], [9, 14, 2, 7], [33, 14]]

def sec_smallest_num_in_list(lst4):
    result = []
    for sublist in lst4:
        if len(sublist) <2:
            result.append(None)
        else:
            sorted_sublist = sorted(sublist)
            result.append(sorted_sublist[1])
    return result


print(sec_smallest_num_in_list(lst4))

lst5 = ['apelsin', 'banan', 'citron']

def replace(lst5):
    result = []

    for word in lst5:
        for i in word:
            if i == 'a':
                word = word.replace('a', '*')
                if word not in result:
                    result.append(word)
            
    return result

print(replace(lst5))

lst6 = [x for x in range(1, 101)]
def divthing(lst6):
    result = [] 
    for i in lst6:
        if (i% 3 == 0 or i % 5 == 0) and i % 15 != 0:
            result.append(i)
    return result

print(divthing(lst6))


# Teachers thing
def all_positives(nums):
    return [num for num in nums if num >= 0]

def first_letter_number(words):
    return [ord(word[0]) for word in words]

def nested_list_comp(nested_nums):
    return [sorted(sublist)[1] for sublist in nested_nums]

def kill_a(words):
    return [word.replace('a', '*') for word in words if 'a' in word]

def odd_fizzbuzz():
    return [x for x in range(100) if x%15 != 0 and x%3 == 0 and x%5 == 0]

def i_matrix():
    return [[1 if x==y else 0 for y in range(5)] for x in range(5)]

print(i_matrix())

def sort_and_remove_list(nums):
    return [nums[i] for i in range(len(nums)) if nums[i] > max(nums[:i])]

#print(sort_and_remove_list([3,1,2,4,5]))
def stalin_sort(nums):
    return [nums[i] for i in range(len(nums)) if i == 0 or nums[i] >= nums[i-1]]
def flatten_list(nested_nums):
    return [num for sublist in nested_nums for num in sublist]

def all_palindromes(words):
    return [word for word in words if word == word[::-1]]

def transpose(matrix): #Vända på ett matrix linjer blir kolumner Linjär algebra
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))] #För varje rad i matrisen, ta element i och gör en ny rad

def check_pnr_2(pnr):
    return(sum([x*2//10 +x*2%10 for x in pnr[0:-1:2]]+pnr[1:-1:2]) + pnr[-1]) % 10 == 0

print(check_pnr_2([0,4,0,8,2,1,3,8,1,7]))

result = []
def add_hit(x):
    result.append(x)
    result.sort()
    return result

add_hit(312)
add_hit(123)
print(result)
