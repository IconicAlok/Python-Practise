# Sorting in python .sort() or sorted()
# List[], Tuple(), Dictionaies{"":""}, Objects

fruit = ["Banana", "Orange", "Apple", "Coconut"]
fruits = ("Banana", "Orange", "Apple", "Coconut")
fruits = {"Banana":105,
            "Orange":73,
            "Apple":72,
            "Coconut":354}

# for list
# fruit.sort()
# fruit.sort(reverse=True)

# # for tuple
# fruits.sort()
# error 'tuple' object has no attribute 'sort'
# fruits = tuple(sorted(fruits))
# fruits = tuple(sorted(fruits, reverse = True))

# # for Dictionary
# fruits = dict(sorted(fruits.items()))
# # item method return each keys values fair as a tuple, in my dictionary
# fruits = dict(sorted(fruits.items(),key=lambda item:item[0], reverse = True))
# fruits = dict(sorted(fruits.items(),key= lambda item:item[1])) # sorted by value
# fruits = dict(sorted(fruits.items(),key= lambda item:item[1], reverse= True)) # sorted by value

# print(fruits)


# sroting technique for object
class Fruit:
    def __init__(self,name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"{self.name}:{self.calories}"

fruits = [Fruit("Banana", 105),
          Fruit("Apple", 72),
          Fruit("Orange",73),
          Fruit("Coconut", 354)]

# fruits = sorted(fruits, key=lambda fruit: fruit.name)
# fruits = sorted(fruits, key=lambda fruit: fruit.name, reverse=True)
# fruits = sorted(fruits, key=lambda fruit: fruit.calories)
fruits = sorted(fruits, key=lambda fruit: fruit.calories, reverse= True)

print(fruits)

