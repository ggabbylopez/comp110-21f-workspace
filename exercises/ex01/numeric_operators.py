# Using input the terminal asks for a number that is then turned into an integer and 
# the given numbers are put into expressions and then printed out
__author__ = "730407925"

# program logic
left: str = input("insert a number")
right: str = input("insert a number")
left_num = int(left)
right_num = int(right)

print("Left-hand side: " + left)
print("Right-hand side: " + right)

# exponential
exponent = str(left_num ** right_num)
print(left + " ** " + right + " is " + exponent)
# division
div = str(left_num / right_num)
print(left + " / " + right + " is " + div)
# int division
int_div = str(left_num // right_num)
print(left + " // " + right + " is " + int_div)
# remainder
remain = str(left_num % right_num)
print(left + " % " + right + " is " + remain)
