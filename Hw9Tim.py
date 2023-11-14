def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Contact not found"
    return wrapper

contacts = {}

@input_error
def hello():
    return "How can I help you?"

@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact {name} added successfully."

@input_error
def change_phone(name, phone):
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for {name} updated successfully."
    else:
        raise IndexError

@input_error
def get_phone(name):
    return contacts[name]

@input_error
def show_all():
    if contacts:
        result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
        return result
    else:
        return "No contacts found."

@input_error 
def parser(command):
    _, name, phone = command.split()
    if command == "hello":
            print(hello())

    elif command.startswith("add"):
        _, name, phone = command.split()
        print(add_contact(name, phone))

    elif command.startswith("change"):
        _, name, phone = command.split()
        print(change_phone(name, phone))

    elif command.startswith("phone"):
        _, name = command.split()
        print(get_phone(name))

    elif command == "show all":
        print(show_all())

    else:
        print("Invalid command. Please try again.")

def main():
    while True:
        command = input("Enter command: ").lower()

        if command == "good bye" or command == "close" or command == "exit":
            print("Good bye!")
            break
        print(parser(command))
        
if __name__ == "__main__":
    main()