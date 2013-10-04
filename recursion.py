def main():
    # print factorial(5)
    # print multiply_list([3, 2, 5])
    # print count_list([])
    # print sum_list([1,2,3])
    # print fibonacci(7)
    # print reverse([1, 2, 3])
    # print find([4,5,6], 7)
    # print palindrome("tq")
    # print fold_paper(30, 60, 6)
    print count_up(50,30)
    
# Multiply all the elements in a list
def multiply_list(l):
    if l == []:
        return 1
    return l[0] * multiply_list(l[1:])

def factorial(l):
    if l <= 1:
        return 1
    return l * factorial(l-1)
# Count the number of elements in the list l
def count_list(l):
    if l == []:
        return 0
    return 1 + count_list(l[1:])

# Sum all of the elements in a list
def sum_list(l):
    if l == []:
        return 0
    return l[0] + sum_list(l[1:])


# Reverse a list without slicing or loops
def reverse(l):
    if len(l) == 0:
        return []
    patch_list_together = [l.pop(0)]
    return reverse(l) + patch_list_together

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    if n <= 2:
        if n == 0:
            return 0
        else:
            return 1

    return fibonacci(n-1) + fibonacci(n-2)

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    if len(l) < 1:
        return False
    if l[0] == i:
        return True
    else:
        l = l[1:]
    return find(l, i)

# Determines if a string is a palindrome
def palindrome(some_string):
    if some_string[0] != some_string[-1]:
        return False
    if len(some_string) <= 2:
        return True
    else:
        some_string = some_string[1:-1]
    return palindrome(some_string)

# Given the width and height of a sheet of paper, and the number of times to fold it, return the final dimensions of the sheet as a tuple. Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    if folds == 0:
        return (width, height)
    if width >= height:
        width = float(width/2)
    elif height > width:
        height = float(height/2)
    return fold_paper(width, height, folds-1)

# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    if n == target:
        return n
    print n
    return count_up(target, n+1)

# Recursion is resisting the irresistible temptation to be nudged towards loopdom.
main()