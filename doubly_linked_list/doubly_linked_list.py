"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, node):
        self.prev = node

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, node):
        self.next = node

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        self.value = None
        self.prev = None
        self.next = None


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value=None, node: ListNode = None):
        if self.head:
            if node is None:
                new_node = ListNode(value=value, next=self.head)
            else:
                new_node = node
            self.head.insert_after(new_node)
            self.head = new_node
        else:
            self.head = ListNode(value=value)
            self.tail = self.head
            
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.length == 0:
            self.head = None
            return None

        if self.head:
            if self.head.next:
                self.head.next.prev = None
                temp_val = self.head.value
                self.head = self.head.next
            else:
                temp_val = self.head.value
                self.head = None
        else:
            return None

        self.length -= 1
        return temp_val

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value=None, node: ListNode = None):
        if self.tail:
            if node is None:
                new_node = ListNode(value=value, next=self.head)
            else:
                new_node = node
            self.tail.insert_before(new_node)
            self.tail = new_node
        else:
            self.tail = ListNode(value=value)
            self.head = self.tail

        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.length == 0:
            self.tail = None
            return None 

        if self.tail.prev:
            self.tail.prev.next = None
            temp_val = self.tail.value
            self.tail = self.tail.prev
        else:
            temp_val = self.tail.value
            self.tail = None

        self.length -= 1
        return temp_val

    def stitch(self, node_a, node_b):
        # Stitch node_a -> node_b
        if node_a:
            node_a.next = node_b
        if node_b:
            node_b.prev = node_a

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        self.stitch(node.prev, node.next)
        self.add_to_head(node=node)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        self.stitch(node.prev, node.next)
        self.add_to_tail(node=node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        self.stitch(node.prev, node.next)
        node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        temp_node = self.head
        max_val = None
        for _ in range(self.length):
            if max_val == None:
                max_val = temp_node.value
            else:
                max_val = max([max_val, temp_node.value])
            print(temp_node.value)
            if temp_node.next:
                temp_node = temp_node.next
            else:
                break
        return max_val


if __name__ == "__main__":
    llist = DoublyLinkedList()

    for i in range(10):
        llist.add_to_head(i)
    
    for j in range(10, 20):
        llist.add_to_tail(j)

    print(llist.get_max())