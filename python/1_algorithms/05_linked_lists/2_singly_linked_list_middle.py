class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def find_middle(self):
        if self.head is None:
            return None

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


def main():
    linked_list = LinkedList()
    (linked_list.append(x) for x in [1, 2, 3, 4, 5, 6])
    sth = linked_list.find_middle()
    print(f"sth: {sth}")


if __name__ == "__main__":
    main()
