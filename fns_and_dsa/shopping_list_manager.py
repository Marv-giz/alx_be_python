def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []  # required: must be defined as an array/list

    while True:
        display_menu()  # required: must call display_menu()

        try:
            choice = int(input("Enter your choice: "))  # required: must convert to NUMBER
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} added.")

        elif choice == 2:
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed.")
            else:
                print("Item not found in the shopping list.")

        elif choice == 3:
            print("Current Shopping List:")
            if not shopping_list:
                print("The list is empty.")
            else:
                for item in shopping_list:
                    print(item)

        elif choice == 4:
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
