#Problem 1: Add a .remove method to the LinkedList

#Add a method to the LinkedList class to remove a node from the list.

#The method should take in a string of the value to remove and remove the node with that value from the LinkedList.

class Node:
    def __init__(self, value):
        self.value = value #commonly refered to as data instead of value
        self.next = None
        
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return f"<Node|{self.value}>"
    
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def _get_node(self, value_to_get):
        check = self.head
        while check is not None:
            if check.value == value_to_get:
                return check
            check = check.next
        return None
        
    def push_on(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node
        
    def append(self, new_value):
        new_node = Node(new_value)
        
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node
            
    def insert_after(self, prev_value, new_value):
        prev_node = self._get_node(prev_value)
        if prev_node is None:
            print(f"{prev_value} is not in linked list")
            return
        
        new_node = Node(new_value)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def traverse_list(self):
        node = self.head
        while node:
            print(node) 
            node = node.next
    
    def remove(self, value_to_remove):
        node = self.head #storing a head node
        if node is not None: #if head node is the value we're wanting to remove (not None)
            if node.value == value_to_remove:
                self.head = node.next
                node = None
                return
        while(node is not None):
            if node.value == value_to_remove:
                break
            prev_node = node 
            node = node.next
        if node == None: #if key was not present in Linked list
            return
        prev_node.next = node.next #this is unlinking the node from the list
        node = None 
            
    
weekdays = LinkedList()
list_of_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for day in list_of_days:
    weekdays.append(day)

weekdays.remove('Wednesday')

weekdays.traverse_list()