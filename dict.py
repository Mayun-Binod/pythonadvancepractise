# Creating a dictionary
student = {
    "name": "Binod",
    "age": 25,
    "course": "Computer Science"
}

# Accessing dictionary values using keys
print("Name:", student["name"])        # Output: Binod
print("Age:", student["age"])          # Output: 25
print("Course:", student["course"])    # Output: Computer Science

# Adding a new key-value pair
student["grade"] = "A"
print("Updated Dictionary:", student)

# Removing a key-value pair
del student["age"]
print("After Deletion:", student)