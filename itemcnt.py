from collections import Counter

fruits = ("pineapple", "watermelon", "passion", "blueberries", "passion")
# instance of a counter
c = Counter(fruits)
item = "passion"
print("Fruits:", c[item])


