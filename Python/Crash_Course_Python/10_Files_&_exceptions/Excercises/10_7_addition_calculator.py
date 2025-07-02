print("Enter two numbers you want to add")
print("Type 'q' to quit the program")

while True:
    first_num = input("Enter  the first number: ")
    if first_num == 'q':
        break

    second_num = input("Enter the second number: ")
    if second_num == 'q':
        break

    try:
        answer = int(first_num) + int(second_num)
    except ValueError:
        print(f"please provide both the numbers in numerical form!")
    else:
        print(answer)