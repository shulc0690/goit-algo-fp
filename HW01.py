class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def sorted_insert(head, node):
    if not head or node.data <= head.data:
        node.next = head
        return node
    else:
        current = head
        while current.next and current.next.data < node.data:
            current = current.next
        node.next = current.next
        current.next = node
    return head


def insertion_sort(head):
    sorted_head = None
    current = head
    while current is not None:
        next_node = current.next
        sorted_head = sorted_insert(sorted_head, current)
        current = next_node
    return sorted_head


def merge_lists(list1, list2):
    dummy = Node(0)
    tail = dummy
    while list1 and list2:
        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 if list1 else list2
    return dummy.next


# Визначимо вузли списків
node1 = Node(10)
node2 = Node(20)
node3 = Node(15)
node1.next = node2
node2.next = node3

node4 = Node(5)
node5 = Node(7)
node6 = Node(25)
node4.next = node5
node5.next = node6

# Реверсування списку
reversed_head = reverse_list(node1)
current = reversed_head
print("Reversed list: ", end="")
while current:
    print(current.data, end=" ")
    current = current.next
print()

# Сортування списку
sorted_head = insertion_sort(reversed_head)
current = sorted_head
print("Sorted list: ", end="")
while current:
    print(current.data, end=" ")
    current = current.next
print()

# Об'єднання двох відсортованих списків
merged_head = merge_lists(sorted_head, node4)
current = merged_head
print("Merged list: ", end="")
while current:
    print(current.data, end=" ")
    current = current.next
print()
