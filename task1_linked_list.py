class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def reverse(self):
        prev = None
        cur = self.head
        while(cur is not None):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def insertion_sort(self):
        
        sorted_head = None
        cur = self.head

        while cur:
            next_node = cur.next

            if sorted_head is None or sorted_head.data >= cur.data:
                cur.next = sorted_head
                sorted_head = cur
            else:
                cur_sorted = sorted_head
                while cur_sorted.next and cur_sorted.next.data < cur.data:
                    cur_sorted = cur_sorted.next
                cur.next = cur_sorted.next
                cur_sorted.next = cur

            cur = next_node

        self.head = sorted_head

    def merge_lists(self, ll1, ll2):
        dummy_n = Node()
        elem = dummy_n

        while True:
            if ll1 is None:
                elem.next = ll2
                break
            if ll2 is None:
                elem.next = ll1
                break

            if ll1.data <= ll2.data:
                elem.next = ll1
                ll1 = ll1.next
            else:
                elem.next = ll2
                ll2 = ll2.next

            elem = elem.next

        self.head = dummy_n.next

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next        

llist = LinkedList()
llist2 = LinkedList()
llist3 = LinkedList()

#додаємо вузли на початок 
llist.insert_at_beginning(5)
llist.insert_at_beginning(15)
llist.insert_at_beginning(10)
llist.insert_at_beginning(13)
llist.insert_at_beginning(4)

llist2.insert_at_beginning(23)
llist2.insert_at_beginning(49)
llist2.insert_at_beginning(44)

print("Linked list:")
llist.print_list()

llist.reverse()
print("Reversed linked list:")
llist.print_list()

llist.insertion_sort()
print("Sorted linked list:")
llist.print_list()

llist3.merge_lists(llist.head, llist2.head)
print("Merged linked list:")
llist3.print_list()