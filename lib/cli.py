from lib.helpers import list_dogs, add_dog, delete_dog

def main():
    while True:
        print("\n=== Dog Management CLI ===")
        print("1. List Dogs")
        print("2. Add Dog")
        print("3. Delete Dog")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            list_dogs()
        elif choice == '2':
            add_dog()
        elif choice == '3':
            delete_dog()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
