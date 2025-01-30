def show_menu():
    print("\nPhonebook Options:")
    print("1. Add Contact")
    print("2. Find Contact")
    print("3. Remove Contact")
    print("4. Display Contacts")
    print("5. Quit")

def add_contact(phonebook):
    name = input("Contact Name: ").strip()
    phone = input("Phone Number: ").strip()
    if name in phonebook:
        print(f"'{name}' already exists in phonebook.")
    else:
        phonebook[name] = phone
        print(f"'{name}' added successfully.")

def find_contact(phonebook):
    name = input("Search for Name: ").strip()
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print(f"'{name}' not found in phonebook.")

def remove_contact(phonebook):
    name = input("Remove Name: ").strip()
    if name in phonebook:
        del phonebook[name]
        print(f"'{name}' removed from phonebook.")
    else:
        print(f"'{name}' not found.")

def display_contacts(phonebook):
    if phonebook:
        print("\nPhonebook Entries:")
        for name, phone in phonebook.items():
            print(f"{name}: {phone}")
    else:
        print("Phonebook is empty.")

def main():
    phonebook = {}
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_contact(phonebook)
        elif choice == "2":
            find_contact(phonebook)
        elif choice == "3":
            remove_contact(phonebook)
        elif choice == "4":
            display_contacts(phonebook)
        elif choice == "5":
            print("Exiting phonebook. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()
