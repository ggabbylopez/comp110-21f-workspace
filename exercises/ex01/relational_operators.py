"""Using input the terminal asks for a number that is then turned into an integer and the given numbers are put into relation expressions and then printed out.""" 
__author__ = "730407925"

# Program logic
left: str = input("insert a number")
right: str = input("insert a number")
left_num = int(left)
right_num = int(right)
print("Left-hand side: " + left)
print("Right-hand side: " + right)


less_than = str(left_num < right_num)
print(left + " < " + right + " is " + less_than)

greater_or_eq = str(left_num >= right_num)
print(left + " >= " + right + " is " + greater_or_eq)

equal = str(left_num == right_num)
print(left + " == " + right + " is " + equal)

not_equal = str(left_num != right_num)
print(left + " != " + right + " is " + not_equal)