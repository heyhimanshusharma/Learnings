while True:
    print("Enter 'q' to end the program." )
    reason = input("Why do you like programming? ")

    if reason == 'q':
        break

    with open('reasons.txt', 'a') as file_object:
        file_object.write(reason)
