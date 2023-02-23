class Node:

    # Creating a node

    def __init__(self,item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def inserAtBeginning(self,new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.heaf = new_node
    
    def insertAfter(self,prev_node,new_data):

        if prev_node is None:
           # raise "Ensure that there is a node previouslty"
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def inserAtEnd(self,new_data):
        new_node = Node(new_data)

        if self.head is Node:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def deleteNode(self,position):
        if position ==0:
            self.head = temp.next
            temp = None
            return
        for i in range(position-1):
            temp= temp.next
            if temp is None:
                break
        # if temp is None:
        #     return
        if temp or temp.next is None:
            return
        
        next = temp.next.next

        temp.next = None
        temp.next =next
        
        
        
            

        
if __name__ == "__main__":
    linked_list  = LinkedList()

    # Assiing item values
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    linked_list.head.next = second
    second.next  = third


    while linked_list.head:
        print(linked_list.head.item,end="->")
        linked_list.head = linked_list.head.next