# Day 1: Python Data Structures & Core Logic

**Goal:** Master the building blocks of Python: Lists, Dictionaries, and Loops. These are the tools you will use 90% of the time.

## 📚 Core Concepts

### 1. The Mighty Dictionary (`dict`)
A dictionary is a Key-Value pair. In other languages, it's a "HashMap" or "Object".
```python
user = {
    "id": 1,
    "name": "Sidharth",
    "is_admin": True
}
# Accessing
print(user["name"])  # "Sidharth"
print(user.get("email", "no-email")) # Safe access (default value)
```

### 2. Lists (`list`)
Ordered collection of items.
```python
users = ["Alice", "Bob", "Charlie"]
# Loop over it
for name in users:
    print(f"Hello {name}")
```

### 3. Mixing Them (List of Dictionaries)
This is how data looks in the real world (JSON from APIs, DB rows).
```python
data = [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"}
]
```

### 4. Functions
Reusable blocks of code.
```python
def get_admin_names(user_list):
    admins = []
    for u in user_list:
        if u["role"] == "admin":
            admins.append(u["name"])
    return admins
```

---

## 🛠️ Hands-On Task: "The Contact Book"

We will build a simple program to manage contacts.

### Step 1: Create `lab_basics.py`
Copy the following starter code into `lab_basics.py` inside `days/day01_fundamentals/`.

```python
# A list of dictionaries to store contacts
CONTACTS = [
    {"name": "Alice", "phone": "123-456", "tags": ["work", "friend"]},
    {"name": "Bob", "phone": "987-654", "tags": ["family"]}
]

def add_contact(name, phone, tags):
    # TODO: Create a dictionary and append it to CONTACTS
    pass

def find_by_tag(tag_name):
    # TODO: Return a list of names that have this tag
    pass

def print_summary():
    # TODO: Loop over CONTACTS and print "Name (Phone) - Tags: X, Y"
    pass

# Test your code
add_contact("Charlie", "555-555", ["work"])
print("Work contacts:", find_by_tag("work"))
print_summary()
```

### Step 2: Implement the TODOs
1.  **`add_contact`**: Create a dict `{"name": name, ...}` and `CONTACTS.append(new_contact)`.
2.  **`find_by_tag`**: Loop through `CONTACTS`. Check `if tag_name in contact["tags"]:`.
3.  **`print_summary`**: Loop and print formatted strings.

### Step 3: Run it
```bash
python lab_basics.py
```
