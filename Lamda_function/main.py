# Lamda function = A small anonymous function for a one time use (Throw awary function)
#                  They take any number of arguments, but have only 1 expression
#                  Helps namespace clean and is usefull with higher order functions
#                  'sort()' 'map()' 'filter()' 'reduce()'
#                  lamda parameter : expression

double = lambda x:x*2
add = lambda x,y: x+y
max_value = lambda x,y: x if x > y else y
min_value = lambda x,y: x if x < y else y
full_name = lambda first_name, last_name : first_name + " " + last_name
is_even = lambda x: x%2 ==0
is_odd = lambda x: x%2 !=0
age_check = lambda age : True if age>=18 else False

print(double(3))
print(add(2,3))
print(max_value(4,5))
print(min_value(8,7))
print(full_name("Spongebob", "Squarepants"))
print(is_even(8))
print(is_odd(9))
print(age_check(11))