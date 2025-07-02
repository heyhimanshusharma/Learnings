first_num = input("Enter  the first number: ")
second_num = input("Enter the second number: ")

try:
    answer = int(first_num) + int(second_num)
except ValueError:
    print(f"please provide both the numbers in numerical form!")
else:
    print(answer)