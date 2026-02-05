# Unit I
# Concept of Dynamic arrays and its implementation. Linked Lists: Implementation of Singly
# Linked Lists, Doubly Linked Lists, Circular Linked Lists



 ### Dynamic arrays

# 1️⃣ First understand: What is an Array?

# An array is a collection of elements stored in contiguous memory.
# [10, 20, 30, 40]

# 2️⃣ Problem with normal (static) arrays

# In low-level languages (C/C++), arrays have fixed size.

# Example:

# size = 3
# [10, 20, 30]


# Now you want to add 40 😢
# No space → need to create new array and copy.

# This is inefficient.

# 👉 Solution = Dynamic Array


# 3️⃣ What is a Dynamic Array?

# A dynamic array automatically resizes itself when it becomes full.

# Python list = Dynamic Array 🎉

# arr = [10,20,30]
# arr.append(40)  # list automatically grows


# You don’t see resizing — but internally it happens.

# 4️⃣ How Dynamic Array works internally

# This is VERY IMPORTANT for interviews.

# Step 1 — Start with small capacity

# Suppose capacity = 2

# [ _ , _ ]
# size = 0
# capacity = 2


# Add elements:

# append(10) → [10, _]
# append(20) → [10, 20]


# Now array is FULL.

# Step 2 — Resize when full

# When we add 30:

# Create new array of double capacity

# Copy old elements

# Add new element

# Old: capacity = 2 → [10,20]
# New: capacity = 4 → [10,20,_,_]
# Add 30 → [10,20,30,_]


# This doubling strategy makes append fast ⚡