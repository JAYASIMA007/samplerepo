def append(list1, list2):
    return list1 + list2

def concat(lists):
    result = []
    for lst in lists:
            result += lst
    return result


def filter(function, list):
    result = []
    for x in list:
        if function(x):
            result += [x]
    return result


def length(list):
    count = 0
    for _ in list:
        count += 1
    return count


def map(function, list):
    result = []
    for x in list:
        result += [function(x)]
    return result


def foldl(function, list, initial):
    acc = initial
    for x in list:
        acc = function(acc, x)
    return acc

def foldr(function, lst, initial):
    acc = initial
    for x in reversed(lst):
        acc = function(acc, x)
    return acc

def reverse(list):
    return list[::-1]

