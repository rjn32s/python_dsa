# LEsts Create the Node Class


class Node:
    def __init__(self,data = None , next = None):
        self.data = data
        self.next = next
        
# create the Class LinkedList
class linked_list:
    def __init__(self):
        self.head = None
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node
    def print(self):
        if self.head is None:
            print("Linked List is EMPTY !!!")
            return
        itr = self.head
        lstr = ''
        while itr:
            lstr += str(itr.data) + '-->'
            itr = itr.next
        print(lstr)
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr =self.head
        while  itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count
    def remaove_at(self, index):
        if index <0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index ==0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1
    def insert_at(self,index,data):
        if index <0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index ==0:
            self.insert_at_begining(data)
        count = 0
        itr = self.head
        while itr:
            
            if count == index -1: 
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count +=1
            
    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert , self.head.next)
            return
        
        
        # Search for first Occurence of data_after
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
                break
            itr = itr.next
    def remove_value(self,data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
            
        itr = self.head
        while itr:
            if itr.next.data == data:
                #node = Node(data_to_insert,itr.next)
                itr.next = itr.next.next
                break
            itr = itr.next
    
                
            
        
        
    
        
        
            
            
            
        
        
        
if __name__ == '__main__':
    l1 = linked_list()
    # l1.insert_at_begining(100)
    # l1.insert_at_begining(50)
    
    # l1.insert_at_end(120)
    # l1.insert_at_begining(150)
    # l1.insert_at_end(500)
    # l1.print()
    l1.insert_values([10,20,30,40,50])
    l1.print()
    l1.remaove_at(2)
    #print(l1.get_length())
    l1.print()
    l1.insert_at(2,"hello")
    l1.print()
    l1.insert_after_value(20,"I am")
    l1.print()
    l1.remove_value("hello")
    l1.print()    