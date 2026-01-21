# A list of dictionaries to store contacts
CONTACTS = [
    {"name": "Alice", "phone": "123-456", "tags": ["work", "friend"]},
    {"name": "Bob", "phone": "987-654", "tags": ["family"]}
]

def add_contact(name, phone, tags):
    """
    Creates a new contact dictionary and adds it to the list.
    """
    # TODO: Create a dictionary like {"name": ..., "phone": ..., "tags": ...}
    # TODO: Append it to the global CONTACTS list
    print(f"Adding {name}...")

def find_by_tag(tag_name):
    """
    Returns a list of names of contacts who have the specific tag.
    """
    found_names = []
    # TODO: Loop over CONTACTS
    # TODO: Check if tag_name is IN the contact's 'tags' list
    # TODO: If yes, append contact['name'] to found_names
    return found_names

def print_summary():
    """
    Prints a summary line for each contact.
    Format: "Name (Phone) [Tags]"
    """
    print("\n--- Contact Summary ---")
    # TODO: Loop over CONTACTS
    # TODO: Print the details
    print("-----------------------")

if __name__ == "__main__":
    # 1. Test Adding
    add_contact("Charlie", "555-0199", ["work"])
    add_contact("Dave", "555-0000", ["gym", "friend"])

    # 2. Test Finding
    print("\nLooking for 'work' contacts:")
    results = find_by_tag("work")
    print(results)  # Should contain Alice and Charlie

    # 3. Test Summary
    print_summary()
