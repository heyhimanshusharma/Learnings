print("Give me two numbers I will divide them.")
print("Enter 'q' to quit the program.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by zero")
    else:
        print(answer)

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("you can't divide by zero")