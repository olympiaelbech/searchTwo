import sys

# Given a sorted list 'a', and an element 'x' to
#search for, search the index where x was found,
# or -1 if not found

def search(a, x):
    lo = 0
    hi = len(a) - 1
    while lo <= hi: # range is non-empty
        mid = (lo + hi) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            lo = mid + 1 
        else:
            hi = mid - 1
    return -1 # not found

f = open('words')
words = []
for word in f:
    words.append(word.strip())
s = input('Word to find: ')
print(search(words, s))