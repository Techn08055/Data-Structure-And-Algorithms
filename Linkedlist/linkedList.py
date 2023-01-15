#Classs for Node 
class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

#Class for linkedlist
class LinkedList:
    def __init__ (self):
        self.head = None

    #function to print the linkedlist 
    def printLinkedlist(self):
        if self.head == None:
            print("Linked List is empty")
            return
        iterator = self.head
        list_str = ""
        while iterator:
            list_str += str(iterator.data) + "-->"
            iterator = iterator.next_node
        print(list_str)

    # function to insert at the beginning of the linked list
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node 
    
    #function to insert at the end of the linked list
    def insert_at_the_end(self,data):
        if self.head is None:
            node = Node(data,None)
            self.head = node
            return
        iterator = self.head
        while iterator.next_node:
            iterator = iterator.next_node
        iterator.next_node = Node(data, None)

    #function to count the number of elements in a linkedlist
    def count_length(self):
        count = 0
        iterator = self.head
        while iterator:
            count += 1
            iterator = iterator.next_node
            return count
    
    #function to insert anywhere in the linkedlist
    def insert_anywhere(self, data, idx):
        if idx < 0 or idx > self.count_length():
            raise Exception("Invalid Index")

        if idx == 0:
            insert_at_beginning(data)
            return

        count = 0
        iterator = self.head
        while iterator:
            if count == idx - 1:
                node = Node (data, iterator.next_node)
                iterator.next_node = node
                break
            iterator = iterator.next_node
            count += 1

    #function to data in the linkedlist
    def delete_Data(self, idx):
        if idx < 0 or idx > self.count_length():
            raise Exception("Invalid Index")

        if idx == 0:
            self.head = self.head.next_node
            return

        count = 0
        iterator = self.head
        while iterator:
            if count == idx - 1:
                iterator.next_node = iterator.next_node.next_node
                break
            iterator = iterator.next_node
            count += 1

    #function to search in the linkedlist
    def search_Data(self, data):
        count = 0
        iterator = self.head
        while iterator:
            if iterator.data == data:
                print("Found at :", count)
                return
            iterator = iterator.next_node
            count += 1
        print("not found")

#Driver code 
if __name__ == "__main__":
    list_1 = LinkedList()
    list_1.insert_at_beginning(45)
    list_1.insert_at_the_end(50)
    list_1.insert_anywhere(73,1)
    list_1.printLinkedlist()
    list_1.delete_Data(1)
    list_1.search_Data(5)
    list_1.search_Data(50)
    list_1.printLinkedlist()

