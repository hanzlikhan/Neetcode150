# using nested loop to check if it is contain duplicate or not 

def is_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

# check duplicate by sorting the array 

def is_duplicate_sort(arr):
    arr.sort()
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return True
    return False

# check duplicate by using set

def is_duplicate_set(arr):
    return len(arr) != len(set(arr))

# check duplicate by using hashmap

def is_duplicate_hashmap(arr):
    hashmap = {}
    for i in arr:
        if i in hashmap:
            return True
        hashmap[i] = 1
    return False
