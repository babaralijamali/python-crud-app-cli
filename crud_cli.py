import sqlite3

# Database connection
conn = sqlite3.connect("app.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
""")
conn.commit()

# CREATE
def create_user(name, email):
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    print("User added successfully!")

# READ
def read_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print("\n--- Users List ---")
    for user in users:
        print(user)

# UPDATE
def update_user(user_id, name, email):
    cursor.execute("UPDATE users SET name=?, email=? WHERE id=?", (name, email, user_id))
    conn.commit()
    print("User updated successfully!")

# DELETE
def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    print("User deleted successfully!")

# Menu
while True:
    print("""
====    CRUD APP CLI Version   ====
====Created by Babar Ali Jamali====

1. Add User
2. View Users
3. Update User
4. Delete User
5. Exit
""")

    choice = input("Select option: ")

    if choice == "1":
        name = input("Enter name: ")
        email = input("Enter email: ")
        create_user(name, email)

    elif choice == "2":
        read_users()

    elif choice == "3":
        user_id = input("Enter user ID: ")
        name = input("Enter new name: ")
        email = input("Enter new email: ")
        update_user(user_id, name, email)

    elif choice == "4":
        user_id = input("Enter user ID: ")
        delete_user(user_id)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")

conn.close()
