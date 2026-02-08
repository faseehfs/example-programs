class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_LL(head):
    current_node = head
    while current_node:
        print(current_node.data, end = " -> ")
        current_node = current_node.next
    print("None")


node1 = Node(11)
node2 = Node(12)
node3 = Node(13)
node4 = Node(14)
node5 = Node(15)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print_LL(node1)
print_LL(node3)