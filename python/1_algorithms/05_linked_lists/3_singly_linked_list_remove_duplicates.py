class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def remove_duplicates(self):
        if self.head is None:
            return None
        node_values = set()
        current_node = self.head
        node_values.add(current_node.value)
        while current_node.next is not None:
            if current_node.next.value in node_values:
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next
        self.tail = current_node


def main():
    linked_list = LinkedList()
    for x in [1, 2, 3, 4, 5, 6, 6]:
        linked_list.append(x)
    print(linked_list)
    linked_list.remove_duplicates()
    print(linked_list)


if __name__ == "__main__":
    main()
