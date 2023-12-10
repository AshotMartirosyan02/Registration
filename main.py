import registration
import login

while True:
    print("\n    Main Menu    ")
    print("1. Registration  new user")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        registration.register_user()
    elif choice == '2':
        login.login()
    elif choice == '3':
        print("Thank you for using my aplication")
        break
    else:
        print("Invalid choice, please try again.")
