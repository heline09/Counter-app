import collections

list = [1, 2, 3, 4, 6, 7, 5, 2, 3, 7, 8, 3]
c = collections.Counter(list)
print("list:", list, "\n")
print(c, "\n")

tuple = ("apple", "banana", "cherry", "tangerine", "apple")
c1 = collections.Counter(tuple)
print("\ntuple:", tuple, "\n")
print(c1, "\n")

str = "Python Programming"
c2 = collections.Counter(str)
print("String:", str, "\n")
print(c2, "\n")

dict = {'a':3, 'b':2, 'c':1}
c3 = collections.Counter(dict)
print("\nDictionary:", dict, "\n")
print(c3, "\n")


