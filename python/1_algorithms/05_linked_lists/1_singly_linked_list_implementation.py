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
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values)

    def __repr__(self):
        return f"LinkedList([{', '.join(str(x) for x in self)}])"

    def __len__(self):
        return self.length

    def __iter__(self):
        self._iter_node = self.head
        return self

    def __next__(self):
        if self._iter_node:
            current_node = self._iter_node
            self._iter_node = self._iter_node.next
            return current_node.value
        raise StopIteration

    def __getitem__(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def __setitem__(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value

    def __delitem__(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        if index == 0:
            self.head = self.head.next
            if self.length == 1:
                self.tail = None
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
            if index == self.length - 1:
                self.tail = current
        self.length -= 1

    def __contains__(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length += 1

    def pop(self):
        if self.length == 0:
            raise IndexError("Pop from empty list")
        if self.length == 1:
            value = self.head.value
            self.head = self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            value = self.tail.value
            self.tail = current
            self.tail.next = None
        self.length -= 1
        return value

    def pop_first(self):
        if self.length == 0:
            raise IndexError("Pop from empty list")
        value = self.head.value
        self.head = self.head.next
        if self.length == 1:
            self.tail = None
        self.length -= 1
        return value

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0


def main():
    # Initialize an empty LinkedList:
    linked_list = LinkedList()

    # Append Method:
    [linked_list.append(x) for x in (3, 4, 5)]
    print(f"Append Method: {linked_list}")

    # Prepend Method:
    [linked_list.prepend(x) for x in (2, 1, 0)]
    print(f"Prepend Method: {linked_list}")

    # Pop Method:
    popped_value = linked_list.pop()
    print(f"Pop Method: {linked_list}; Popped Value: {popped_value}")

    # Pop First Method:
    popped_first_value = linked_list.pop_first()
    print(f"Pop First Method: {linked_list}; Popped Value: {popped_first_value}")

    # Str Method:
    print(f"Str Method: {linked_list}")

    # Repr Method:
    print(f"Repr Method: {repr(linked_list)}")

    # Get Item Method:
    print(f"Get Item Method at Index 2: {linked_list[2]}")

    # Set Item Method:
    linked_list[len(linked_list) - 1] = 99
    print(f"Set Item Method at Item at Last Index to Value 99: {linked_list}")

    # Delete Item Method:
    del linked_list[len(linked_list) - 1]
    print(f"Delete Item Method at Last Index: {linked_list}")

    # Contains Method:
    print(f"Contains Method with Value 5: {5 in linked_list}")
    print(f"Contains Method with Value 10: {10 in linked_list}")

    # Insert Method:
    linked_list.insert(2, 2.5)
    print(f"Insert Method with Value 2.5 at Index 2: {linked_list}")

    # Len Method:
    print(f"Len Method: {(len(linked_list))}")

    # Delete All Method:
    linked_list.delete_all()
    print(f"Delete all items: {repr(linked_list)}")


if __name__ == "__main__":
    main()
