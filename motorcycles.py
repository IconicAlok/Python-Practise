motorcycles = ["Honda","Yamaha","Sujuki"]
print(motorcycles)
motorcycles[0] = "ducati"
print(motorcycles)
motorcycles = ["Honda","Yamaha","Sujuki"]
motorcycles.append('ducati')
print(motorcycles)
motorcycles = []
# print(motorcycles)
motorcycles.insert(0,'dukati')
motorcycles.append("Honda")
motorcycles.append("Yamaha")
motorcycles.append("Sujuki")

print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

motorcycles = ["Honda","Yamaha","Sujuki"]

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ["Honda","Yamaha","Sujuki"]
last_owned = motorcycles.pop()
print(f"The last motorcycle i owned was a {last_owned.title()}.")

motorcycles = ["Honda","Yamaha","Suzuki"]
first_owned = motorcycles.pop(0)
print(f"The first motorcycle i owned was a {first_owned.title()}.")


motorcycles = ["Honda","Yamaha","Sujuki",'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)


motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles[3])

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles[-1])

motorcycles = []
# print(motorcycles[-1])