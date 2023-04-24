from collections import Counter
list = [1, 2, 3, 4, 6, 7, 5, 2, 3, 7, 8, 3]
c = Counter()
c.update("1")  # update counter
print(c)
c.update("1")  # update counter again
print(c)