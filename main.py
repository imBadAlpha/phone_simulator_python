from Contacts import Contacts

contacts = []


def show_all_message():
    if len(contacts) > 0:
        name = input("Please enter the name of the Contact:")
        does_exist = False
        for con in contacts:
            if name == con.name:
                does_exist = True
                if len(con.message) == 0:
                    print("No Message to show yet...\n")
                else:
                    con.show_all_message()

        if not does_exist:
            print("Name does not exist in the list of Contacts...\n")
    else:
        print("Your Contacts List is empty.")

    main_menu()


def send_new_message():
    name = input("Please enter the name of the recipient: ")
    does_exist = False
    for con in contacts:
        if name == con.name:
            does_exist = True
            text = input("Enter your message: ")
            con.add_message(text)

    if not does_exist:
        print("The recipient does not exist on the list of Contacts...")

    main_menu()


def manage_messages():
    ans = input("Please Select One:"
                "\n\t1. Show All Messages"
                "\n\t2. Send a New Message"
                "\n\t3. Go Back\n")
    if ans == "1":
        show_all_message()
    elif ans == "2":
        send_new_message()
    elif ans == "3":
        main_menu()
    else:
        print("ERROR!")
        manage_messages()


def show_all_contacts():
    if len(contacts) > 0:
        for con in contacts:
            con.get_details()
            print("*********************************")
        show_all_contacts()
    else:
        print("Your Contacts List is empty...")
        show_all_contacts()


def add_contact():
    name = input("Adding new Contact..."
                 "\nPlease enter the name: ")
    number = input("Please enter the number: ")
    email = input("Please enter the email: ")

    if name == "" or number == "" or email == "":
        print("Please enter all the information")
        add_contact()
    else:
        does_exist = False
        for con in contacts:
            if name == con.name:
                does_exist = True

        if does_exist:
            print("We have a contact named " + name + " saved on this device. The contact was not added.\n")
            add_contact()
        else:
            contacts.append(Contacts(name, number, email))
            print("Contact Added Successfully!...\n")
    main_menu()


def delete_contact():
    name = input("Please enter the Contact's name: ")
    if name == "":
        print("Input is empty")
        delete_contact()
    else:
        does_exist = False
        i = 0
        for con in contacts:
            if con.name == name:
                does_exist = True
                contacts.pop(i)
                print("Contact Deleted!...\n")
            i += 1

        if not does_exist:
            print("This name does not exist in the list of Contacts.")

    main_menu()


def search_contact():
    name = input("Please enter a name: ")
    if name == "":
        print("Input is empty!")
        search_contact()
    else:
        does_exist = False
        for con in contacts:
            if con.name == name:
                con.get_details()
                does_exist = True

        if not does_exist:
            print("There is no such name in your contacts.")

    search_contact()


def manage_contacts():
    ans = input("Please Select One:"
                "\n\t1. Show All Contacts"
                "\n\t2. Add New Contact"
                "\n\t3. Delete Contact"
                "\n\t4. Search for Contact"
                "\n\t5. Go Back\n")

    if ans == "1":
        show_all_contacts()
    elif ans == "2":
        add_contact()
    elif ans == "3":
        delete_contact()
    elif ans == "4":
        search_contact()
    elif ans == "5":
        main_menu()
    else:
        print("ERROR!")
        manage_contacts()


def main_menu():
    ans = input("Please Select One:"
                "\n\t1. Manage Contacts"
                "\n\t2. Messages"
                "\n\t3. Quit\n")

    if ans == "1":
        manage_contacts()
    elif ans == "2":
        manage_messages()
    else:
        print("ERROR!")
        main_menu()


main_menu()

