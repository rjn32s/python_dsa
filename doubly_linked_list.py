class Node:
    def __init__(self,prev,data,next):
        self.prev = prev
        self.data = data
        self.next = next
        
class dbly_linked_list:
    def __init__(self):
        self.head = None
    def insert_at_begining(self,data):
        self.head = Node(None,data,self.head)
    def forward_print(self):
        if self.head is None:
            print("Linked List is EMPTY !!!")
            return
        itr = self.head
        lstr = ''
        while itr:
            lstr += str(itr.data) + '-->'
            itr = itr.next
        print("Linked list in Forward",lstr)
    def backward_print(self):
        if self.head is None:
            print("Linked List is EMPTY !!!")
            return
        itr = self.get_to_last()
        lstr = ''
        while itr:
            lstr += str(itr.data)+'-->'
            itr = itr.prev
        print("Link list in reverse: ",lstr)
            
    def get_to_last(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count +=1
        return count
    def insert_at_begining(self,data):
        if self.head is None:
            self.head = Node(None,data,self.head)
        else:
            node = Node(None,data,self.head)
            self.head.prev=node
            self.head = node
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(None,data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(itr,data,None)
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(itr, data , itr.next)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)        
        
if __name__ == '__main__':
    ll = dbly_linked_list()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.forward_print()
    ll.backward_print()
    ll.insert_at_end("figs")
    ll.forward_print()
    ll.insert_at(0,"jackfruit")
    ll.forward_print()
    ll.insert_at(6,"dates")
    ll.forward_print()
    ll.insert_at(2,"kiwi")
    ll.forward_print()
            
    
    
            
        
         
    
    
        