from lib.helpers import (
    list_dogs,
    add_dog,
    delete_dog,
    log_activity,
    view_activities,
    log_health_record,
    view_health_records
)


def main():
    while True:
        print("\n=== Dog Care Tracker CLI ===")
        print("1. List Dogs")
        print("2. Add Dog")
        print("3. Delete Dog")
        print("4. Log Activity")
        print("5. View Activities")
        print("6. Log Health Record")
        print("7. View Health Records")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            list_dogs()
        elif choice == '2':
            add_dog()
        elif choice == '3':
            delete_dog()
        elif choice == '4':
            log_activity()
        elif choice == '5':
            view_activities()
        elif choice == '6':
            log_health_record()
        elif choice == '7':
            view_health_records()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == '__main__':
    main()
