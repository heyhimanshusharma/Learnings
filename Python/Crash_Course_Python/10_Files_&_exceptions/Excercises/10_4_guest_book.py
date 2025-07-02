while True:
    print("\nEnter 'q' to end the program.")
    name = input('Type your name to addd to the guest list: ')

    if name == 'q':
        break
    else:
        print(f"welcome to our house {name}")
    
    with open('guest_book.txt', 'a') as file_object:
        file_object.write(f"{name}\n")