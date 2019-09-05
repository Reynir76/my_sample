num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int = 0

while num_int > 0:
    #num_int = 0
    number_int = int(input("Enter an integer: "))
    if number_int <= 0:
       break    
    if number_int > max_int:
        max_int = number_int

print("The maximum is", max_int)    # Do not change this line





# number_int = 1
# max_int = 0

# while number_int > 0:
#     number_int = 0
#     number_int = int(input("Enter an integer: "))
#     if number_int <= 0:
#        break    
#     if number_int > max_int:
#         max_int = number_int
    
# print("Maximum number is: ", max_int)