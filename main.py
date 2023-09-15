contacts = {}

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command format"
    return wrapper

@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Added {name} with phone {phone}"

@input_error
def change_phone(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return f"Changed phone for {name} to {new_phone}"
    else:
        raise KeyError

@input_error
def get_phone(name):
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}"
    else:
        raise KeyError

@input_error
def show_all_contacts():
    if not contacts:
        return "No contacts found"
    else:
        result = "Contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()

def main():
    print("How can I help you?")
    
    while True:
        command = input().strip().lower()
        
        if command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            try:
                _, name, phone = command.split()
                print(add_contact(name, phone))
            except ValueError:
                print("Invalid command format. Usage: add [name] [phone]")
        elif command.startswith("change"):
            try:
                _, name, new_phone = command.split()
                print(change_phone(name, new_phone))
            except ValueError:
                print("Invalid command format. Usage: change [name] [new_phone]")
        elif command.startswith("phone"):
            try:
                _, name = command.split()
                print(get_phone(name))
            except ValueError:
                print("Invalid command format. Usage: phone [name]")
        elif command == "show all":
            print(show_all_contacts())
        else:
            print("Invalid command. Type 'hello' to see available commands.")

if __name__ == "__main__":
    main()
