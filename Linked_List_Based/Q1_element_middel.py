# Define a class for each node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define a class for the linked list
class LinkedList:
    def __init__(self):
        self.head = None

    # Add a new node to the linked list
    def addNode(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next

        currentNode.next = newNode

    # Print the middle of the linked list
    def printMiddle(self):
        slowPointer = self.head
        fastPointer = self.head

        while fastPointer is not None and fastPointer.next is not None:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next

        print("The middle of the linked list is:", slowPointer.data)

# Example usage
linked_list = LinkedList()
linked_list.addNode(1)
linked_list.addNode(2)
linked_list.addNode(3)
linked_list.addNode(4)
linked_list.addNode(5)

linked_list.printMiddle()
