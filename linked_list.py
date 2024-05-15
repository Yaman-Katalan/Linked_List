from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """
        This function is used to append a new value to the LinkedList.
        """
        node = Node(value) # Create new node.
        

        # If the LinkedList is empty:
        if self.head is None:
            self.head = node
            return True
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
            return True
    # Time complexity = O(n)
    # Space complexity = O(1)

    def delete_node(self, key):
        """
        This function is used to delete an entered value from the LinkedList.
        """
        temp = self.head

        #1. Empty LinkedList
        if temp is None:
            return False
        #2. If target is the first node:
        if temp is not  None:
            if (temp.value == key):
                self.head = temp.next # Now LS is empty
                temp = None
                return True
        # Serach for the key and delete the target node

        while (temp is not None):
            if temp.value == key:
                break
            prev = temp
            temp = temp.next

            #3. the key does not exist in the LinkdList
            if temp is None:
                return False

            prev.next = temp.next
            temp = None

    def __str__(self):
        current = self.head
        values = []
        while current is not None:
            values.append(current.value)
            current = current.next
        return str(values)
    
    def __len__(self):
        """"
        This magic attribute returns the length of the LinkedList
        """
        current=self.head
        count = 0
        while current is not None:
            count+=1
            current = current.next
        return count
    
    def __getitem__(self, index):
        """"
        This magic attribute returns the value for a specific LS item through indexing.
        """
        if index < 0:
            raise IndexError("Index out of range")
        current = self.head
        count = 0
        while current is not None:
            if count == index:
                return current.value
            count += 1
            current = current.next
        raise IndexError("Index out of range")