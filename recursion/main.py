# recursion = a function that call itself from within
#              helps to visualize a complex problem into basic step,
#              which can be solved more easily iteratively or recursively
#               iterative = faster, complex
#               recursive = slower, easy
#
# def walk(steps):
#         if steps==0:
#             return 0
#
#         walk(steps-1)
#         return print(f"You take steps #{steps}")
#
# walk(100)



# factorial
# iterative
# def factorial(x):
#     result = 1
#     if x > 0:
#         for y in range(1, x+1):
#             result *= y
#         return result

#recursive
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(10))