class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_LL(head):
    current_node = head
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print("None")


def delete_node(head, node_to_delete):
    if head == node_to_delete:
        return head.next

    current_node = head
    while current_node.next and current_node.next != node_to_delete:
        current_node = current_node.next

    if current_node.next is None:
        return head

    current_node.next = current_node.next.next
    return head


def insert_node(head, new_node, position):
    if position == 1:
        new_node.next = head
        return new_node

    current_node = head
    for _ in range(position - 2):
        if current_node is None:
            break
        current_node = current_node.next

    new_node.next = current_node.next
    current_node.next = new_node
    return head


node1 = Node(1)  # This is the head.
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Created linked list:")
print_LL(node1)

print("Deleting node 3:")
node1 = delete_node(node1, node3)
print_LL(node1)

print("Inserting a node at index 2 with data 3:")
node1 = insert_node(node1, Node(3), 2)
print_LL(node1)
