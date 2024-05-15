
# LinkedList Implementation in Python

This project implements a simple linked list data structure in Python. It provides functionalities such as appending elements, deleting nodes, getting the length of the list, and accessing elements by index.

## Usage

### Initialization

```python
from linkedlist import LinkedList

# Create a new linked list
my_list = LinkedList()
```

### Appending Elements

```python
# Append elements to the linked list
my_list.append(1)
my_list.append(2)
my_list.append(3)
```

### Deleting Nodes

```python
# Delete a node with a specific value
my_list.delete_node(2)
```

### Getting Length

```python
# Get the length of the linked list
length = len(my_list)
print(length)  # Output: 2
```

### Accessing Elements by Index

```python
# Access elements by index
print(my_list[0])  # Output: 1
print(my_list[1])  # Output: 3
```

### String Representation

```python
# Get the string representation of the linked list
print(my_list)  # Output: [1, 3]
```