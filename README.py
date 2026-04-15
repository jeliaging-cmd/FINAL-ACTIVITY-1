# FINAL-ACTIVITY-1
Part 1
# 1. Tuple of 5 favorite fruits
fruits = ("apple", "banana", "mango", "grapes", "orange")

# 2. List of 5 daily tasks
tasks = ["wake up", "eat breakfast", "study", "exercise", "sleep"]

# 3. Set of unique numbers from the list
numbers_list = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers_list)

# 4. Dictionary with keys: name, age, course
student = {
    "name": "John",
    "age": 18,
    "course": "Computer Science"
}

# Print outputs
print("Tuple:", fruits)
print("List:", tasks)
print("Set:", unique_numbers)
print("Dictionary:", student)
Part 2
# Initial data
fruits = ("apple", "banana","mango","grapes", "orange")
tasks = ["wake up","eat breakfast","study", "exercise","sleep"]
numbers_list = [1, 2, 2, 3, 4, 4, 5]

# convert list to set (removes duplicates)
unique_numbers = set(numbers_list)

student = {
    "name": "John",
    "age": 18,
    "course": "Information Technology"
}

# --- List Tasks ---
print("Original tasks:", tasks)

# Add a new task
tasks.append("do homework")

# Remove a task (check first so no error)
if "study" in tasks:
    tasks.remove("study")

# Sort the list
tasks.sort()

print("Updated tasks:", tasks)


# --- Tuple Tasks ---
print("\nFruits tuple:", fruits)

# Example (cannot change tuple)
# fruits[0] = "pineapple"  # this will give an error

print("Note: Tuple cannot be changed (immutable)")


# --- Set Tasks ---
print("\nOriginal set:", unique_numbers)

# Add a number
unique_numbers.add(6)

# Remove a number safely
if 2 in unique_numbers:
    unique_numbers.remove(2)

print("Updated set:", unique_numbers)
print("Set removes duplicates automatically:", set(numbers_list))
