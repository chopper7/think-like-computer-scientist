
'''
Although Python provides us with many list methods, it is good practice and
very instructive to think about how they are implemented. Implement a Python
function that works like the following:
count, in, reverse, index, insert

(I'm also trying not to use ANY list methods inside these functions.)
'''

# I skipped "count" and "reverse" and just did the ones that challenged me.


## in
def in_list(L, target):
    found = False
    idx = 0
    while idx < len(L) and not found:
        if L[idx] == target:
            found = True
            break
        else:
            idx += 1
    return found

# in Answer Code
def is_in(obj, lst):  # cannot be called in() because in is a reserved keyword
    for e in lst:
        if e == obj:
            return True
    return False



## index
def get_index(L, e):
    idx = None
    for i in range(len(L)):
        if L[i] == e:
            idx = i
            break
    if not idx:
        print('Not in list')
    return idx
# (I avoided return -1 because -1 could be used as index of last item in list)

## index Answer Code
def index(obj, lst):
    for i in range(len(lst)):
        if lst[i] == obj:
            return i
    return -1



## insert
def list_insert(L, n, o):
    '''L: list, n: index, o: object to insert'''
    newList = []
    if n >= len(L):
        # Python's own list.insert() method doesn't throw exception when
        # index out of range; it just appends item to list silently.
        newList = L + [o]
    else:
        newList = L[0:n] + [o] + L[n:]
    if len(newList) <= len(L):
        return IndexError
    else:
        return newList

## insert Answer Code
def insert(obj, index, lst):
    newlst = []
    for i in range(len(lst)):
        if i == index:
            newlst.append(obj)
        newlst.append(lst[i])
    return newlst
